# 3ª Etapa do desafio final: Filmes e Séries

A 3ª etapa do desafio final consiste em realizar um processamento de dados (carregados para o bucket na etapa passada) para uma camada trusted.

A API utilizada esta sendo a TMDB, por ter sido introduzida aos bolsistas nessa sprint e porque oferece dados de qualidade e é amplamente usada no setor para informações de filmes e séries, excelente para obter mais informações que responderão as questões abordadas no readme da sprint 6: [README.md da Sprint 6](/Sprint6/Desafio/README.md)

Para a realização do desafio proposto, comecei criando a camada trusted no bucket da AWS respectivo do desafio final:
![camadatrusted](/Sprint8/Evidências/Desafio/camadatrusted.png).

A partir disso, é preciso começar a processar e integrar os dados da camada Raw para a camada Trusted. Essa etapa sera feita utilizando Apache Spark no serviço Glue da AWS. Para isso foram criados dois jobs no serviço AWS Glue.

O primeiro job é responsável pelo processamento dos arquivos CSV, o código utilizado na plataforma foi esse: [jobCSV.py](/Sprint8/Desafio/jobCSV.py).
![csv](/Sprint8/Evidências/Desafio/csv.png)

O segundo job é responsável pelo processamento dos dados oriundos da API TMDB, no formato JSON, o código utilizado na plataforma foi esse: [jobJSON.py](/Sprint8/Desafio/jobJSON.py).
![json](/Sprint8/Evidências/Desafio/json.png)

A partir disso, os dados ficarão na camada trusted do bucket no formato parquet, segue a imagem de evidência abaixo:

Dados parquet CSV:
![csvparquet](/Sprint8/Evidências/Desafio/parquetcsv.png)

Dados parquet JSON:
![jsonparquet](/Sprint8/Evidências/Desafio/parquetjson.png)
