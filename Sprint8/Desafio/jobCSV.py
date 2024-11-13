import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import lit, col, when

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Definindo caminhos de entrada e saída
input_path = "s3://desafio-sprint-6/Raw/Local/CSV/Movies/2024/10/21/movies.csv"
output_path = "s3://desafio-sprint-6/Trusted/Local/CSV/Movies"

# Leitura do arquivo CSV
df = spark.read.option("delimiter", "|").csv(input_path, header=True)

df = df.withColumnRenamed("titulopincipal", "tituloprincipal")

# Tratamento de dados
df = df.withColumn("tituloprincipal", when(col("tituloprincipal") != "\\N", col("tituloprincipal")).otherwise(""))
df = df.withColumn("anolancamento", when((col("anolancamento") != "\\N") & (col("anolancamento") != ""), col("anolancamento").cast("int")).otherwise(None))
df = df.withColumn("tempominutos", when((col("tempominutos") != "\\N") & (col("tempominutos") != ""), col("tempominutos").cast("int")).otherwise(None))
df = df.withColumn("genero", when(col("genero") != "\\N", col("genero")).otherwise(""))
df = df.withColumn("notamedia", when((col("notamedia") != "\\N") & (col("notamedia") != ""), col("notamedia").cast("double")).otherwise(None))
df = df.withColumn("numerovotos", when((col("numerovotos") != "\\N") & (col("numerovotos") != ""), col("numerovotos").cast("int")).otherwise(None))
df = df.withColumn("generoartista", when(col("generoartista") != "\\N", col("generoartista")).otherwise(""))
df = df.withColumn("personagem", when(col("personagem") != "\\N", col("personagem")).otherwise(""))
df = df.withColumn("nomeartista", when(col("nomeartista") != "\\N", col("nomeartista")).otherwise(""))
df = df.withColumn("anonascimento", when((col("anonascimento") != "\\N") & (col("anonascimento") != ""), col("anonascimento").cast("int")).otherwise(None))
df = df.withColumn("anofalecimento", when((col("anofalecimento") != "\\N") & (col("anofalecimento") != ""), col("anofalecimento").cast("int")).otherwise(None))
df = df.withColumn("profissao", when(col("profissao") != "\\N", col("profissao")).otherwise(""))
df = df.withColumn("titulosmaisconhecidos", when(col("titulosmaisconhecidos") != "\\N", col("titulosmaisconhecidos")).otherwise(""))

# Adicionando uma coluna de data para particionamento
current_date = datetime.now().strftime("%Y-%m-%d")
df = df.withColumn("data_processamento", lit(current_date))

# Salvando em Parquet na Trusted Zone com particionamento por data de processamento
df.write.mode("overwrite").partitionBy("data_processamento").parquet(output_path)

job.commit()
