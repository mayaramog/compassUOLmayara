import boto3
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
public_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
access_token = os.getenv('AWS_SESSION_TOKEN')
bucket_name = os.getenv('BUCKET_NAME')

# Configurar o cliente boto3 para acessar o S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=public_key,
    aws_secret_access_key=secret_key,
    aws_session_token=access_token
)

# Função para carregar arquivo CSV para o S3
def upload_to_s3(file_path, bucket_name, object_name):
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)  # Use 's3_client' aqui
        print(f"Arquivo {file_path} enviado para o bucket {bucket_name} com sucesso.")
    except Exception as e:
        print(f"Erro ao fazer upload para o S3: {e}")

# Função principal para ler CSVs e carregar para S3
def processar_csv():
    # Caminhos dos arquivos CSV locais (atualizados para o ambiente Docker)
    movies_csv = "/app/csv/movies.csv"
    series_csv = "/app/csv/series.csv"

    # Nome do bucket
    bucket_name = 'desafio-sprint-6'  # Certifique-se de que este nome está correto

    # Data atual para organização dos dados no formato ano/mês/dia
    current_date = datetime.now().strftime('%Y/%m/%d')

    # Definir caminhos no S3 para salvar os arquivos com base na data atual
    movies_s3_path = f"Raw/Local/CSV/Movies/{current_date}/movies.csv"
    series_s3_path = f"Raw/Local/CSV/Series/{current_date}/series.csv"

    # Carregar arquivos CSV para S3
    upload_to_s3(movies_csv, bucket_name, movies_s3_path)
    upload_to_s3(series_csv, bucket_name, series_s3_path)

if __name__ == '__main__':
    processar_csv()
