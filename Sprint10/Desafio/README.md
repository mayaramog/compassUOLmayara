# Desafio - Etapa final

Esse README tem o intuito de fornecer detalhes de como foi a construção do desafio final, presente na sprint 10 do programa de bolsas 2024 da empresa COmpass.UOL

## Contextualização

O a ultima etapa do desafio final "Filmes e Séries" (dividido em 5 sprints) consiste na realização de um Dashboard, o consumo de dados. Ou seja, a proposta é extrair insights através de uma ferramenta de visualização, o Quick Sight da AWS que viabilizem um Storytelling a partir dessa criação. Os dados a serem utilizados deveriam ser somente os dados já tratados da camada refined no Bucket S3 (realizado na sprint 9) destinado as atividades do desafio final.

## Entregáveis

- Código, comentários e evidências.
- Arquivo markdown com imagens de evidências da resolução do desafio.
- Imagens dos Dashboards implementados.

## Processo de realização do desafio

1. Planejar o que seria feito

Antes de tudo, decidi planejar de que forma os dados deveriam ser apresentados, quais os tipos de gráficos mais apropriados para apresentar determinadas informações.

Para isso, abri a ferramenta do Windows Whiteboard para esboçar algumas ideias. Dei preferência para essa ferramenta pois já tenho familiaridade com ela, então me senti mais a vontade dessa forma.

Aqui pode ser visto algumas imagens dos dados contidos na minha camada refined e alguns tipos de gráficos. Esse processo foi bem inicial, algumas ideias foram surgindo na hora e não foram anotadas nesse esboço.
![planejamento](/Sprint10/Evidências/esboço%20dashboard.png)

2. Utilização da ferramenta QuickSight

De início, por mais que eu tivesse assistido o curso da udemy, senti uma leve dificuldade de me localizar inicialmente na ferramenta. Mas depois de um tempo consegui.

**DETALHE:** Eu tive alguns problemas iniciais para importar os dados do S3 para a ferramenta com uma consulta SQL (que me possibilitaria a junção da tabela fato com as dimensões), foi algo que acabou me atrasando no processo também (além de eu ter mudado a minha análise de dados). O problema que estava acontecendo com as consultas era a referenciação errada das tabelas, eu estava usando default ao invés de refined, acabei demorando para perceber.

Fui testando também algumas consultas geradas no athena que poderiam ser uteis para o desenvolvimento do meu Dashboard.
![athena](/Sprint10/Evidências/testesAthena.png)

Após isso, fui definindo um Dashboard para cada análise estipulada.

- **1ª análise: Quantidade de avaliações e filmes registrados por década**

![planilha1](/Sprint10/Evidências/quickSight/planilha1.png)
Aqui eu decidi inserir uma tabela com a quantidade de avaliações dos filmes do gênero de Crime/War de cada decada e a nota média de todos esses filmes.

Adicionei também um gráfico de rosca para identificar a nota média de todos os filmes do gênero ao decorrer das decadas. A escolha desse gráfico foi justamente para ilustrar o padrão e semelhança seguido das notas médias dos filmes com o passar das décadas.

Por fim, utilizei gráficos de linha (devido a quantidade e discrepancia dos valores contados) para demonstrar a quantidade de filmes e a quantidade de avaliações do gênero registrados durante as decadas. Queria demonstrar a sincronia desses dois dados, quanto mais filmes mais avaliações tiveram. Além disso, o dado mostra também que a decada de 2010 foi vencedora, com a maior quantidade de filmes e analises (é importante lembrar também que a decada de 2020 aina esta ocorrendo, então os dados podem mudar).


- **2ª análise: Participação feminina nos filmes do gênero no século 21  e sua comparação com os demais artistas**

![planilha2](/Sprint10/Evidências/quickSight/planilha2.png)
Para a segunda analise, eu optei por adicionar alguns dados interessantes já de inicio, a quantidade de artistas femininas registradas que participaram de filmes do gênero Crime/War durante as decdas do século 21 até então.

Adicionei um grafico de pizza que mostra a porcentagem da particiação feminina(actress) e masculina(actor) nos filmes desse gênero no século 21 e um gráfico de barras para possibilitar a vizualização mais detalhada da participação dos artistas durante as décadas.

- **3ª análise: Nota média e duração dos filmes com o passar dos anos**

![planilha3](/Sprint10/Evidências/quickSight/planilha3.png)
Por fim, criei uma tabela com os filmes mais avaliados de cada decada ordenado pela nota média, para possibilitar uma correlação com a duração e sua avaliação.

Adicionei um gráfico de rosca para a média geral da duração desses filmes com o passar das décadas, possibilitando também a visualização do aumento ou diminuição dessa duração com o passar dos anos.

Além disso, um gráfico de barras e linha que compara a avaliação do filme com a sua duração.

## Resultado do desafio

- ### Quantidade de avaliações e filmes registrados por década

![tabela](/Sprint10/Desafio/analise1/tabela.png)
![rosca](/Sprint10/Desafio/analise1/rosca.png)
![linha1](/Sprint10/Desafio/analise1/linha1.png)
![linha2](/Sprint10/Desafio/analise1/linha2.png)

- ### Participação feminina nos filmes do gênero no século 21  e sua comparação com os demais artistas

![dadosgerais](/Sprint10/Desafio/analise2/dadosgerais.png)
![pizza](/Sprint10/Desafio/analise2/pizza.png)
![barras](/Sprint10/Desafio/analise2/barra.png)

- ### Nota média e duração dos filmes com o passar dos anos

![tabela](/Sprint10/Desafio/analise3/tabela.png)
![barralinha](/Sprint10/Desafio/analise3/barralinha.png)
![rosca](/Sprint10/Desafio/analise3/rosca.png)