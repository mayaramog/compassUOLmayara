import json
import boto3
import csv
import os
import requests
from datetime import datetime

s3 = boto3.client("s3")
bucket_name = "desafio-sprint-6"
tmdb_api_key = os.getenv("TMDB_API_KEY")  # Certifique-se de que a chave da API esteja configurada

def is_valid_year(year_str):
    """Verifica se a string do ano é válida e representa um número inteiro."""
    try:
        year_float = float(year_str)
        return year_float.is_integer()  # Verifica se o número é um inteiro
    except ValueError:
        return False

def read_movies_from_csv():
    """Função para ler filmes do CSV armazenado no S3."""
    response = s3.get_object(Bucket=bucket_name, Key="Raw/Local/CSV/Movies/2024/10/21/movies.csv")
    csv_data = response["Body"].read().decode("utf-8").splitlines()
    reader = csv.reader(csv_data, delimiter="|")
    
    movies = []
    
    # Ignorar o cabeçalho
    next(reader)

    for row in reader:
        if len(row) >= 4:  # Verifique se a linha tem informações suficientes
            try:
                # Verificar e processar o ano
                ano = row[1].strip()  # Certifique-se de remover espaços em branco
                
                if is_valid_year(ano):
                    year = int(float(ano.split('-')[0]))  # Converte o ano para inteiro
                else:
                    print(f"Ano inválido: {ano}")
                    year = None
                
                movies.append({
                    "titulo": row[0],
                    "ano": year,
                    "nota": float(row[2]) if row[2] else 0.0,
                    "genero_ids": [int(x) for x in row[3].split(",")] if row[3] else []
                })
            except ValueError as e:
                print(f"Erro ao processar linha: {row}. Erro: {e}")  # Log do erro para fins de depuração
    return movies

def fetch_movie_details_from_tmdb(title):
    """Função para buscar detalhes de um filme na API TMDB pelo título."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={title}"
    response = requests.get(url)
    response.raise_for_status()  # Lança um erro se a resposta não for bem-sucedida
    results = response.json().get("results", [])
    return results[0] if results else None  # Retorna o primeiro resultado ou None

def lambda_handler(event, context):
    """Função principal do Lambda."""
    current_date = datetime.now().strftime("%Y/%m/%d")
    decade_movies = {}

    # Lê os filmes do CSV
    csv_movies = read_movies_from_csv()
    
    # Completar os filmes com dados da API TMDB
    for movie in csv_movies:
        title = movie["titulo"]
        tmdb_movie = fetch_movie_details_from_tmdb(title)
        
        if tmdb_movie:
            movie["nota"] = tmdb_movie.get("vote_average", movie["nota"])  # Atualiza a nota se disponível
            movie["genero_ids"] = [genre["id"] for genre in tmdb_movie.get("genre_ids", [])]  # Atualiza os IDs de gênero se disponíveis

    # Agrupar filmes por década
    for movie in csv_movies:
        year = movie["ano"]
        if year:
            decade = (year // 10) * 10
            if decade not in decade_movies:
                decade_movies[decade] = []
            decade_movies[decade].append(movie)

    # Criar arquivos JSON para cada década
    for decade, movies in decade_movies.items():
        top_movies = sorted(movies, key=lambda x: x["nota"], reverse=True)[:10]
        
        # Criar o nome do arquivo JSON para armazenar no S3
        file_name = f"Raw/TMDB/JSON/{current_date}/filmes_{decade}.json"

        # Tentar gravar no S3
        try:
            if top_movies:
                # Incluir título por escrito no JSON
                output_movies = [{"titulo": movie["titulo"], "ano": movie["ano"], "nota": movie["nota"], "genero_ids": movie.get("genero_ids", [])} for movie in top_movies]
                
                s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(output_movies, ensure_ascii=False).encode("utf-8"))
        except Exception as e:
            return {
                "statusCode": 500,
                "body": f"Erro ao gravar no S3: {str(e)}"
            }

    return {
        "statusCode": 200,
        "body": f"Dados gravados com sucesso no S3 para cada década."
    }
