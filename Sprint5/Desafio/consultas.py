import pandas as pd
import boto3
from io import StringIO
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
s3 = boto3.client(
    's3',
    aws_access_key_id=public_key,
    aws_secret_access_key=secret_key,
    aws_session_token=access_token
)

# Informações do bucket e do arquivo
file_key = 'bilheteria-diaria-obras-por-exibidoras-2024-08-s04.csv'
output_key = 'bilheteria-diaria-obras-por-exibidoras-2024-08-s04-consulta.csv'

# Fazer o download do arquivo CSV a partir do S3
obj = s3.get_object(Bucket=bucket_name, Key=file_key)
csv_data = obj['Body'].read().decode('utf-8')

# Carregar o arquivo CSV
df = pd.read_csv(StringIO(csv_data), sep=';')

# 1) Filtrar os dados usando dois operadores lógicos (ex: UF_SALA_COMPLEXO e PUBLICO)
filtro = df[(df['UF_SALA_COMPLEXO'] == 'SP') & (df['PUBLICO'] > 10)]

# 2) Duas funções de agregação (ex: média e soma do público por estado)
agrupado = df.groupby('UF_SALA_COMPLEXO')['PUBLICO'].agg(['mean', 'sum']).reset_index()

# 3) Função condicional (ex: criar uma nova coluna para indicar se o público foi maior que 10)
df['Publico_Maior_Que_10'] = df['PUBLICO'].apply(lambda x: 'Sim' if x > 10 else 'Não')

# 4) Função de conversão (ex: converter a coluna de público de string para float)
df['PUBLICO'] = pd.to_numeric(df['PUBLICO'], errors='coerce')

# 5) Função de data (ex: converter DATA_EXIBICAO para o formato datetime)
df['DATA_EXIBICAO'] = pd.to_datetime(df['DATA_EXIBICAO'], format='%d/%m/%Y')

# 6) Função de string (ex: extrair o ano da data de exibição e criar uma nova coluna)
df['Ano_Exibicao'] = df['DATA_EXIBICAO'].dt.year

# Verificar se o arquivo já existe no bucket
def check_file_exists(bucket_name, key):
    try:
        s3.head_object(Bucket=bucket_name, Key=key)
        return True
    except s3.exceptions.ClientError:
        return False

# Se o arquivo não existir, realizar o upload
if not check_file_exists(bucket_name, output_key):
    # Salvar o DataFrame em um buffer
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False, sep=';')

    # Fazer o upload para o S3
    s3.put_object(Bucket=bucket_name, Key=output_key, Body=csv_buffer.getvalue())
    print(f"Arquivo '{output_key}' enviado para o bucket '{bucket_name}'.")
else:
    print(f"Arquivo '{output_key}' já existe no bucket '{bucket_name}', não foi enviado.")

# Exibir o resultado final
print(df.head())
print(agrupado)
