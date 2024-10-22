# Desafio

Nesta seção será descrito sobre o tema de análise a ser feito para a resolução do desafio da sprint presente.

-  Gênero de filmes / series da Squad 2: **Crime / Guerra**

Análises:

- **Quantidade de filmes por década**: A análise envolve contar quantos filmes dos gêneros "crime" ou "guerra" foram lançados ao longo das décadas. Isso requer dividir os filmes em grupos de acordo com suas datas de lançamento (organizados por décadas, por exemplo, 1950-1959, 1960-1969, etc.) e contar quantos filmes do gênero de crime / guerra aparecem ao longo das décadas.

- **Nota média com o passar dos anos**: A análise também deseja deve avaliar a variação na nota média dos filmes desses gêneros ao longo do tempo. A ideia seria verificar como as avaliações desses filmes mudaram ao longo das décadas, observando se houve uma tendência de melhora ou piora nas avaliações.

O intuito dessas analises escolhidas por mim é verificar se houve um aumento na produção de filmes de crime/guerra ao longo das décadas e identiicar as notas, a partir dessa análise é possivel ter indagações como: "Por que houve um aumento/diminuição da produção de filmes desse estilo?", "Por que essa foi a média da nota dos filmes nessa década?", "Por que as pessoas passaram a avaliar melhor/pior esse tipo de gênero?".

## Etapas para a conclusão do desafio após a escolha do tema
- ### Implementação do código python que lê os dois arquivos CSV sem filtrar os dados

[Código python](/Sprint6/Desafio/desafio.py)

- ### Arquivos de docker

[Dockerfile](/Sprint6/Desafio/Dockerfile)
[docker-compose.yml](/Sprint6/Desafio/docker-compose.yml)
[requirements.txt](/Sprint6/Desafio/requirements.txt)

- ### Para realizar a leitura dos arquivos CSV, passei eles para o VSCode para facilitar o processo, então os arquivos ficaram da seguinte forma

![arqs desafio](/Sprint6/Evidências/arqDesafio.png)

- ### Execução do arquivo python e docker e checagem do bucket S3

![desafio1](/Sprint6/Evidências/desafio1.png)
![desafio2](/Sprint6/Evidências/desafio2.png)
![desafio3](/Sprint6/Evidências/desafio3.png)
