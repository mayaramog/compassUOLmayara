# Sprint 7 ⋆
## Sumário
- ### [Curso Udemy]()
- ### [Desafios propostos na Sprint 7]()
- ### [Dificuldades encontradas]()
- ### [Pontos a melhorar para a próxima Sprint]()


## Curso Udemy

### Formação Spark com Pyspark

Conteúdos abordados:
````
- Instalação, primeiros passos e bibliotecas adicionais
- DataFrames e RDDs
- Spark SQL
- Criando aplicações
- Otimização, particionamento e bucketing
- Cache e persistência
- Notebooks do jupyter
- Pandas para DataFrame do Spark
- Spark UI
````

## Desafios propostos na Sprint 7

O desafio consistia na utilização do bucket criado na Sprint 6 e a partir do arquivo CSV upado para esse bucket, utilizariamos uma API TMDB para complementar esses dados dos filmes e series do arquivo CSV.

Primeiramente foi necessário criar um perfil e uma política de permissão no IAM:
![iam1](/Sprint7/Evidências/IAMperfil.png)
![iam2](/Sprint7/Evidências/IAMpermissao.png)

Após isso, realizei a zipagem de todas as bibliotecas necessárias para a criação do código python que faria essa filtragem dos arquivos CSV e utilizaria a API TMDB:
![zip](/Sprint7/Evidências/importaAPI.png)

No Lambda da AWS criei a função necessária para rodar o código python, já criei as camadas com os componentes necessários também:
![funcao](/Sprint7/Evidências/funcao.png)

O código processado foi o seguinte: [config.py](/Sprint7/Desafio/config.py)

## Dificuldades encontradas

- Otimização de tempo, não consegui avançar bem nas 3 sprints propostas para enviar, tive muitas dificuldades na sprint 7.

- Tive alguns contratempos com as minhas obrigações nesse meio tempo também, então a sprint foi entregue com atraso e com alguns erros a serem melhorados no código para prosseguir com o desafio final.

## Pontos a melhorar para a próxima Sprint

- Organização de tempo e atividades.