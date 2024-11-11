import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from pyspark.sql.functions import lit
from pyspark.sql.types import *

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

# Definindo o esquema detalhado dos dados
schema = StructType([
    StructField('adult', BooleanType()),
    StructField('backdrop_path', StringType()),
    StructField('belongs_to_collection', StringType()),
    StructField('budget', IntegerType()),
    StructField('genres', ArrayType(StructType([
        StructField('id', IntegerType()),
        StructField('name', StringType())
    ]))),
    StructField('homepage', StringType()),
    StructField('id', IntegerType()),
    StructField('imdb_id', StringType()),
    StructField('original_language', StringType()),
    StructField('original_title', StringType()),
    StructField('overview', StringType()),
    StructField('popularity', FloatType()),
    StructField('poster_path', StringType()),
    StructField('production_companies', ArrayType(StructType([
        StructField('id', IntegerType()),
        StructField('logo_path', StringType()),
        StructField('name', StringType()),
        StructField('origin_country', StringType())
    ]))),
    StructField('production_countries', ArrayType(StructType([
        StructField('iso_3166_1', StringType()),
        StructField('name', StringType())
    ]))),
    StructField('release_date', StringType()),
    StructField('revenue', IntegerType()),
    StructField('runtime', IntegerType()),
    StructField('spoken_languages', ArrayType(StructType([
        StructField('english_name', StringType()),
        StructField('iso_639_1', StringType()),
        StructField('name', StringType())
    ]))),
    StructField('status', StringType()),
    StructField('tagline', StringType()),
    StructField('title', StringType()),
    StructField('video', BooleanType()),
    StructField('vote_average', FloatType()),
    StructField('vote_count', IntegerType())
])

# Leitura dos arquivos JSON com o esquema definido
df = spark.read.schema(schema).json(input_path)

# Adicionando uma coluna de data para particionamento
current_date = datetime.now().strftime("%Y-%m-%d")
df = df.withColumn("data_processamento", lit(current_date))

# Salvando em Parquet na Trusted Zone com particionamento por data de processamento
df.write.mode("overwrite").partitionBy("data_processamento").parquet(output_path)

job.commit()
