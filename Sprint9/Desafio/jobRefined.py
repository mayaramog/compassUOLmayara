import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# --- Lógica de ETL ---

# Paths específicos para as tabelas no S3
path_tabelacsv = "s3://desafio-sprint-6/Trusted/Local/CSV/Movies/data_processamento=2024-11-13/"
path_tabelajson = "s3://desafio-sprint-6/Trusted/TMDB/JSON/TMDB/data_processamento=2024-11-22/"

# Lendo os dados diretamente do S3 em formato Parquet
tabelacsv = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [path_tabelacsv]},
    format="parquet"
).toDF()

tabelajson = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [path_tabelajson]},
    format="parquet"
).toDF()

# Criando a tabela fato e removendo duplicados com base no ID
fato_avaliacoes = tabelacsv.select(
    F.col("id"),
    F.col("notamedia"),
    F.col("numerovotos"),
    (F.floor(F.col("anolancamento") / 10) * 10).alias("decada")
).dropDuplicates(["id"])  # Remove duplicados com base no ID

# Criando a dimensão Filme e removendo duplicados com base no ID do filme
dim_filme = tabelacsv.select(
    F.col("id").alias("id_filme"),
    F.col("tituloprincipal"),
    F.col("titulooriginal"),
    F.col("anolancamento"),
    F.col("tempominutos"),
    F.col("genero")
).distinct().dropDuplicates(["id_filme"])  # Remove duplicados com base no ID do filme


dim_artista_json = tabelajson.select(
    F.col("id").alias("json_id"),  # Renomeando id na tabela JSON
    F.col("nomeartista").alias("nomeartista"), 
    F.col("generoartista").alias("json_generoartista"),
    F.col("anonascimento").alias("json_anonascimento"),
    F.col("anofalecimento").alias("json_anofalecimento"),
    F.col("profissao").alias("json_profissao"),
    F.col("titulosmaisconhecidos").alias("json_titulosmaisconhecidos")
)

# Salvando as tabelas na camada Refined
dim_filme.write.mode("overwrite").partitionBy("anolancamento").parquet("s3://desafio-sprint-6/Refined/dim_filme")
fato_avaliacoes.write.mode("overwrite").partitionBy("decada").parquet("s3://desafio-sprint-6/Refined/fato_avaliacoes")
dim_artista_json.write.mode("overwrite").parquet("s3://desafio-sprint-6/Refined/dim_artista")

job.commit()
