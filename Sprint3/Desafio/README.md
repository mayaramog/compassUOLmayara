# Desafio

O desafio da Sprint 3 consiste em utilizar as bibliotecas pandas e matplotlib para realizar pesquisas e gerar gráficos dessas pesquisas em cima de um arquivo googleplaystore.csv.

O arquivo .csv é dividido em colunas, estas que deve se basear para realizar os códigos.

Além disso, o código foi feito a partir de células com a extensão Jupyter no VSCode, ou seja, foi gerado um arquivo .ipynb.

## Preparação e Entregaveis
Antes de tudo, precisei fazer pesquisas por fora, então chequei os seguintes sites:

- [Alura](https://www.alura.com.br/artigos/python?srsltid=AfmBOopQVSo8arQA0Lw52O6gkWo97nRZQvgjNex2_mMUIAzIuQEatAlW)
- [hashtagtreinamentos](https://www.hashtagtreinamentos.com)
- Além de alguns vídeos do Youtube

### 1. Configurar o ambiente do VSCode com a extênsão Jupyter
Apenas instalei a extensão e criei um arquivo . ipynb

### 2. Entregáveis
- [desafio1.ipynb](/Sprint3/Desafio/desafio1.ipynb)
- [googleplaystore.csv](/Sprint3/Desafio/googleplaystore.csv)

## Desenvolvimento

### 1. Importação das bibliotecas panda e matplotlib

Instalei as que faltavam e chequei se estava tudo correto pelo terminal:

![checagem](/Sprint3/Evidências/Desafio/bibliotecas.png)

Após a checagem, importei as bibliotecas e li o arquivo googleplaystore.csv. Comecei imprimindo uma tabela com o comando head() para checar a disposição dos elementos e colunas no arquivo:

![importação](/Sprint3/Evidências/Desafio/re0.png)

### 2. Gráfico de Barras - Top 5 Apps por número de instalação

O gráfico pedido ficou da seguinte forma:

![2](/Sprint3/Evidências/Desafio/re1.png)

Como foi feito o codigo:
- Transformei a coluna "Installs" em string para manusear
- removi caracteres extra ("+", ",")
- Transformei os elementos da coluna em inteiro
- Condigurei o gráfico de barras
- Me confundi pelas barras estarem do mesmo tamanho, então pesquisei um meio de adicionar a quantidade de instalações no gráfico

### 3. Gráfico de Pizza - Frequência de categorias

Nesse exercício possuia as categorias mais importantes = 
[
    "FAMILY", "GAME", "TOOLS", "MEDICAL", "BUSINESS", "PRODUCTIVITY", "PERSONALIZATION", "COMMUNICATION", "SPORTS" 
]

as demais deveriam estar na categoria "Outros", no gráfico:

![3](/Sprint3/Evidências/Desafio/re2.png)

Como foi feito o código:
- Transformei a coluna "Category" em string para manusear
- Fiz uma função que recebe uma categoria e checa se essa categoria é importante ou não
- A função é aplicada a cada categoria
- Realiza a contagem por categoria
- onfigurei o gráfico de pizza

### 4. App mais caro existente

O resultado:

![4](/Sprint3/Evidências/Desafio/re4.png)

Como foi feito o codigo:
- Transformei a coluna "Price" em string para manusear
- Removo o simbolo "$" e transformo a coluna "Price" em float
- Encontro o valor mais caro com a função max()
- Imprimo a resposta na tela

### 5. Quantos Apps são classificados como "Mature 17+"

O resultado:

![5](/Sprint3/Evidências/Desafio/re5.png)

Como foi feito o codigo:
- Removi as duplicatas do df (por mais que eu já tivesse feito isso antes, ainda havia valores repetidos, não endendi o motivo)
- Como a coluna "Rating" já é string, filtro as mensagens
- Conto a quantidade de Apps

### 6. Top 10 Apps por número de reviews

O resultado:

![6](/Sprint3/Evidências/Desafio/re6.png)

Como foi feito o codigo:
- Transformo a coluna "Reviews" para int (não possuia nenhum caractere especial, então dava para transformar direto)
- Removo duplicatas
- Seleciono os 10 valores mais altos
- Imprimo na tela

### 7.1. Criação de calculos - Lista

O primeiro calculo que pensei para o exercício 7 foi para retornar um resultado em forma de lista com a média das avaliações de cada categoria levando em consideração as importantes utilizadas
anteriormente.

O Resultado: 

![71](/Sprint3/Evidências/Desafio/re71.png)

Como foi feito o codigo:
- Defini as categorias importantes
- Inclui a coluna "Outros" para as não importantes
- Agrupo e calculo a média
- Imprimo na tela o resultado

### 7.2. Criação de calculos - Valor

O segundo calculo que pensei para o exercício 7 foi para retornar um resultado em forma de valor com App com o menor número de instalações.

O resultado: 

![71](/Sprint3/Evidências/Desafio/re72.png)

Como foi feito o codigo:
- Transformo a colun "Installs" em string
- Removo caracteres especiais ("+", ",")
- Encontro o App com o menor valor
- Imprimo na tela o resultado

### 8.1 Formas gráficas de exibição - Gráfico de linhas

Fiz uma forma de visualização alternativa para a etapa 6 do desafio, com gráfico de linhas:

![81](/Sprint3/Evidências/Desafio/re81.png)

Sobre o código:
- Apenas alterei a exibição do resultado

### 8.2 Formas gráficas de exibição - Gráfico de área

Também fiz outra forma de visualização para a etapa 6 do desafio, com gráfico de área:

![81](/Sprint3/Evidências/Desafio/re82.png)

Sobre o código:
- Apenas alterei a exibição do resultado