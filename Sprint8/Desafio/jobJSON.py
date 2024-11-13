import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import lit

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Definindo caminhos de entrada e saída
input_path = "s3://desafio-sprint-6/Raw/TMDB/JSON/2024/11/04/"
output_path = "s3://desafio-sprint-6/Trusted/Local/JSON/TMDB"

# Leitura dos arquivos JSON sem definir o esquema
df = spark.read.json(input_path)

# Adicionando uma coluna de data para particionamento
current_date = datetime.now().strftime("%Y-%m-%d")
df = df.withColumn("data_processamento", lit(current_date))

# Salvando em Parquet na Trusted Zone com particionamento por data de processamento
df.write.mode("overwrite").partitionBy("data_processamento").parquet(output_path)

job.commit()
