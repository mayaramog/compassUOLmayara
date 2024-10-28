# Exercícios
Este arquivo markdown tem como objetivo organizar a explicação da resolução dos exercícios (feitos através da plataforma da AWS) propostos na sprint 6.


## LAB AWS Athena
- Etapa 1: Configurar Athena
![etapa1](/Sprint6/Exercícios/labAWSAthena/etapa1.png)

- Etapa 2: Criar um banco de dados
![etapa2](/Sprint6/Exercícios/labAWSAthena/etapa2.png)

- Etapa 3: Criar uma tabela
![etapa3](/Sprint6/Exercícios/labAWSAthena/tabelaNomes.png)

- Teste de consulta na tabela criada
![etapa3.1](/Sprint6/Exercícios/labAWSAthena/testeConsulta.png)

- Consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje

-> [Arquivo da query](/Sprint6/Exercícios/labAWSAthena/query.txt)

-> [Resultado da query em formato CSV](/Sprint6/Exercícios/labAWSAthena/queryNomePDecada.csv)


![etapa3.2](/Sprint6/Exercícios/labAWSAthena/query.png)
![etapa3.3](/Sprint6/Exercícios/labAWSAthena/query2.png)


## LAB AWS Lambda

- ### Etapa 1: Criação da função Lambda

![etapa1](/Sprint6/Exercícios/labAWSLambda/etapa1.png)

- ### Etapa 2: Construir o código

O código sugerido e usado no exercício foi esse, apenas atualizando o nome do bucket e pasta:
```
import json
import pandas
import boto3
 
 
def lambda_handler(event, context):
    s3_client = boto3.client('s3')
 
    bucket_name = 'sprint6exerciciosmayara'
    s3_file_name = 'queries/nomes.csv'
    objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    df=pandas.read_csv(objeto['Body'], sep=',')
    rows = len(df.axes[0])
 
    return {
        'statusCode': 200,
        'body': f"Este arquivo tem {rows} linhas"
    }

```

O teste dá erro pois as bibliotecas não estão instaladas:
![etapa2](/Sprint6/Exercícios/labAWSLambda/etapa2teste.png)

- ### Etapa 3: Criar uma Layer

Arquivos Dockerfile e zip com as bibliotecas adicionadas na seguinte pasta:

- [exDocker](/Sprint6/Exercícios/labAWSLambda/exDocker/)

Camada criada com as expecificações necessárias:
![etapa3](/Sprint6/Exercícios/labAWSLambda/etapa3.png)

- ### Etapa 4: Utilizando a Layer

A camada foi adicionada a função mas estava dando erros de permissão, então precisei acessar o IAM para adicionar permissões e ser possível a conclusão do exercício:

![permissaoIAM](/Sprint6/Exercícios/labAWSLambda/permissaoIAM.png)

A permissão foi excluída após a conclusão do exercício.

Função funcionando corretamente:
![etapa4](/Sprint6/Exercícios/labAWSLambda/etapa4.png)