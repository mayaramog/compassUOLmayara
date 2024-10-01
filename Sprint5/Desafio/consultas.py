import pandas as pd

# Carregar o arquivo CSV
arquivo_csv = 'bilheteria-diaria-obras-por-exibidoras-2024-08-s04.csv'
df = pd.read_csv(arquivo_csv, delimiter=';')  # Usando o delimitador correto (;)

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


print(df)
