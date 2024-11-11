# Sprint 8 ⋆
## Sumário
- ### [Curso Udemy]()
- ### [Desafios propostos na Sprint 8]()
- ### [Dificuldades encontradas]()
- ### [Pontos a melhorar para a próxima Sprint]()

## Curso Udemy

### Tutoriais Técnicos - Analytics - Português

```
- Transforme seus dados em insights;
- Transforme e catalogue dados com o AWS Glue Parte 1;
- Transforme e catalogue dados com o AWS Glue Parte 2;
- Consulte dados com o AWS Athena;
- Visualize dados com o Amazon Quicksight.
```
## Exercícios propostos na Sprint 8

### Spark Batch: Warm Up
1. Geração e massa de dados:

O primeiro exercício envolvendo Spark Batch consistia em realizar alguns códigos em python (os warm ups) para começar a desenvolver a lógica do exercício em si

Os códigos desenvolvidos a priori foram:

- [Python 1](/Sprint8/Exercícios/Spark%20Batch/numeros.py): Consiste em inicializar uma lista contendo 250 inteiros obtidos de forma aleatória, aplicar o método reverse e imprimir o resultado. Segue a impressão do resutlado no terminal do VSCode:
![numeros](/Sprint8/Evidências/Exercícios/numeros.png)

- [Python 2](/Sprint8/Exercícios/Spark%20Batch/animais.py) : Consiste em declarar uma lista contendo o nome de 20 animais, ordena-la em ordem crescente e iterar sobre os itens imprimindo um a um e armazenar o resultado em um arquivo CSV: [Arquivo gerado com o código](/Sprint8/Exercícios/Spark%20Batch/animais.csv). Segue a impressão do resultado no terminal do VSCode:
![animais](/Sprint8/Evidências/Exercícios/animaisTerminal.png)

- [Python 3](/Sprint8/Exercícios/Spark%20Batch/dataset.py): Por fim, o exercício warm up final consiste em utilizar a biblioteca para gerar nomes aleatórios, importar as bibliotecas random, time e names, definir os parâmetros para a geração do dataset, gerar os nomes aleatórios e armazenar o resultado em um arquivo txt [nomes_aleatorios.txt](/Sprint8/Exercícios/Spark%20Batch/nomes_aleatorios_compac.zip) (o arquivo está compactado devido ao tamanho de arquivos sustentados para subir no github). Segue a imagem de evidência com a geração do arquivo:
![dataset de nomes](/Sprint8/Evidências/Exercícios/datasetNomes.png)

### Spark Batch: Apache Spark

Com o arquivo [nomes_aleatorios.txt](/Sprint8/Exercícios/Spark%20Batch/nomes_aleatorios_compac.zip) gerado nas primeiras etapas do exercício final, será aplicado recursos básicos de manipulação de dataframes através do framework Apache Spark.

Inicialmente eu criei um ambiente virtual na VMBox, foi a maneira que funcionou para mim. A partir disso, iniciei a construção do código python: [ex.py](/Sprint8/Exercícios/Spark%20Batch/ex.py) com as importações do spark necessárias e definindo a sessão spark para habilitar o módulo SQL. As funcionalidades do código requeridas para o exercício estão especificadas dentro do prórpio código através de comentarios. Abaixo tem algumas evidências da impressão do código python no terminal linux:

![spark1](/Sprint8/Evidências/Exercícios/spark1.png)
![spark2](/Sprint8/Evidências/Exercícios/spark2.png)

Checagem do arquivo txt:
![spark3](/Sprint8/Evidências/Exercícios/spark3.png)

### TMDB -> Presente também na Sprint 7

Esseexercício consistia basicamente em criar uma conta no TMDB e solicitar uma chave API. Além disso, foi fornecido um código para testar essa API: [TMDB.py](/Sprint8/Exercícios/TMDB/TMDB.py). Segue o resultado da consulta com o código utilizando dados da API:

![tmdb](/Sprint8/Evidências/Exercícios/TMDB.png)

## Desafios propostos na Sprint 8

Desafio que consiste na 3 etapa do desafio final: Filmes e Séries. Segue o readme explicativo sobre o desafio: [README.md](/Sprint8/Desafio/README.md)

## Dificuldades encontradas
Uma dificuldade que tive e que não consegui resolver (só identifiquei tal problema no final da sprint, mas não consegui identificar a raiz do problema ainda) foi para fazer consultas no Athena a partir das tabelas criadas utilizando crawlers do serviço AWS Glue. As colunas são mostradas normalmente no Athena:
![colunas](/Sprint8/Evidências/Desafio/dificuldade1.png)

Mas quando realizo uma consulta na tabela, mostra o seguinte erro:
![erro tabela consulta](/Sprint8/Evidências/Desafio/dificuldade2.png)

## Pontos a melhorar para a próxima Sprint

- Maior agilidade para resolução de problemas AWS.
- Melhor organização e gestão de tempo.