from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand, udf, col
from pyspark.sql.types import StringType, IntegerType
import random

# Cria uma SparkSession
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

# Lê o arquivo nomes_aleatorios.txt
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeia a coluna "nome" para "Nomes" (caso o nome da coluna seja "nome")
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Imprime o esquema do DataFrame
df_nomes.printSchema()

# Mostra as 10 primeiras linhas
df_nomes.show(10)

# Adiciona a coluna "Escolaridade" com valores aleatórios entre "Fundamental", "Medio" e "Superior"
df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental")
    .when(rand() < 0.66, "Medio")
    .otherwise("Superior")
)

# Lista de países da América do Sul
paises = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador", 
          "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]

# Define uma UDF para escolher um país aleatório
def pais_aleatorio():
    return random.choice(paises)

# Converte a função em uma UDF para uso no Spark
pais_aleatorio_udf = udf(pais_aleatorio, StringType())

# Adiciona a coluna "Pais" usando a UDF
df_nomes = df_nomes.withColumn("Pais", pais_aleatorio_udf())

# Etapa 5: Adiciona a coluna "AnoNascimento" com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * (2010 - 1945) + 1945).cast(IntegerType()))

# Mostra as 10 primeiras linhas para verificar
df_nomes.show(10)

# Etapa 6: Seleciona pessoas que nasceram a partir do ano 2000
df_select = df_nomes.filter(col("AnoNascimento") >= 2000)

# Mostra as 10 primeiras linhas do DataFrame df_select
df_select.show(10)

# Etapa 7: Repete a Etapa 6 usando Spark SQL
# Cria uma visualização temporária
df_nomes.createOrReplaceTempView("pessoas")

# Executa a consulta SQL para selecionar pessoas nascidas a partir do ano 2000
df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")

# Mostra as 10 primeiras linhas do resultado da consulta SQL
df_select_sql.show(10)
