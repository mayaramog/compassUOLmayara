# Imagem base Python
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt e instalar dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código Python para dentro do container
COPY . .

# Comando para executar o script Python
CMD ["python", "desafio.py"]
