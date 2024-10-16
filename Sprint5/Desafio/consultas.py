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

# Fazer o download do arquivo CSV a partir do S3
obj = s3.get_object(Bucket=bucket_name, Key=file_key)
csv_data = obj['Body'].read().decode('utf-8')

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(StringIO(csv_data), delimiter=';')

# 1) Dois operadores lógicos
consulta1 = df[(df['PUBLICO'] > 5) & (df['UF_SALA_COMPLEXO'] == 'BA')]

# 2) Duas funções de agregação (soma e contagem)
agrupamento = df.groupby('RAZAO_SOCIAL_EXIBIDORA').agg({
    'PUBLICO': 'sum',  # Função de agregação 1
    'TITULO_ORIGINAL': 'count'  # Função de agregação 2 (contagem de títulos)
})

# 3) Função condicional
df['classificacao'] = df['PUBLICO'].apply(lambda x: 'Público Alto' if x > 50 else 'Público Baixo')

# 4) Função de conversão
df['PUBLICO'] = pd.to_numeric(df['PUBLICO'], errors='coerce')

# 5) Função de data -> data para date time e pega o mês
df['DATA_EXIBICAO'] = pd.to_datetime(df['DATA_EXIBICAO'], errors='coerce', format='%d/%m/%Y')
df['mes'] = df['DATA_EXIBICAO'].dt.month

# 6) Função de String -> nome da exibidora em maiuscula
df['RAZAO_SOCIAL_EXIBIDORA_UPPER'] = df['RAZAO_SOCIAL_EXIBIDORA'].str.upper()

# Exibir o DataFrame modificado
print(df)
