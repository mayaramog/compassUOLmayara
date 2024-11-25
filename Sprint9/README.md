# Sprint 9 ⋆
## Sumário
- ### [Desafio proposto na Sprint 9]()
- ### [Dificuldades encontradas]()
- ### [Pontos a melhorar para a próxima Sprint]()

## Desafio proposto na Sprint 9
O desafio proposto na sprint 9 foi a modelagem dimensional dos arquivos parquet gerados e organizados nas sprints passadas do desafio final. Recapitulando um pouco o desafio final, cada SQUAD foi designada a trabalhar com um genero de filme (na minha no caso os generos foram: Crime and War). Primeiramente recebemos um CSV com informações dos filmes, como nome, id, ano de lançamento, etc. Deois disso precisavamos buscar dados de uma API TMDB e depois tratar os dados enviando para a camada Trusted.

Em suma, a sprint 9 propõe a modelagem multidimensional dessas informações para possibilitar consultas mais eficientes e direcionadas de acordo com a análise escolhida pelo bolsista, no meu caso, quero fazer uma análise voltada nas variações das avaliações dos filmes de Crime e War e porpor possíveis motivos para a variação (melhora ou piora).

### Passos para concluir o desafio

- #### 1 Etapa
Primeiramente pensei em como poderia realizar a modelagem (ainda esta meio nublado a ideia que pensei para a modelagem, pretendo aperfeiçoar na Sprint 10 a modelagem). Como quero fazer uma análise baseada nas avaliações dos filmes de acordo com o passar das decadas então as informações chaves que devem ficar na tabela fatos são: id do filme, nota media, quantidade de avaliações e a decada

A modelagem dimensional ficou assim:
![img1](/Sprint9/Desafio/diagrama.png)

- #### 2 Etapa
Após a modelagem, realizei o job para adicionar os paths respectivos na camada Refined

O job realizado na AWS Glue foi esse: [jobRefined.py](/Sprint9/Desafio/jobRefined.py)

Run do job concluída com sucesso:
![img2](/Sprint9/Evidencias/jobRun.png)

- #### 3 Etapa

Após a implementação do job fui checar se os arquivos foram criados corretamente no bucket S3:
![img3](/Sprint9/Evidencias/camadaRefined.png)

Então, no AWS Glue criei um database "refined" e um crawler para criar as tabelas no database:
![img4](/Sprint9/Evidencias/crawlers.png)

As tabelas foram criadas corretamente:
![img4](/Sprint9/Evidencias/tabelas.png)

Por fim, fui até o AWS Athena para chegar se os dados não haviam sido corrompidos e estavam sendo consultados devidamente:
![img](/Sprint9/Evidencias/verificaAthena.png)

## Dificuldades encontradas
Pensar em uma modelagem multidimensional com base na minha análise escolhida. A modelagem entregue foi o que consegui pensar durante a sprint 9, mas pretendo refina-la na sprint 10 para concluir o desafio final.

Ademais, tive dificuldades para conciliar o final do semestre da faculdade com as entregas do estágio.

## Pontos a melhorar para a próxima Sprint
Criar um pensamento mais direcionado e crítico para realizar as análises propostas por mim devidamente.