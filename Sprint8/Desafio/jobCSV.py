import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import lit

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

# Adicionando uma coluna de data para particionamento
current_date = datetime.now().strftime("%Y-%m-%d")
df = df.withColumn("data_processamento", lit(current_date))

# Salvando em Parquet na Trusted Zone com particionamento por data de processamento
df.write.mode("overwrite").partitionBy("data_processamento").parquet(output_path)

job.commit()