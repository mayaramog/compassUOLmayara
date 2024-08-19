# Desafios propostos na Sprint 2
Nesta seção será apresentado um guia de resolução dos desafios propostos na Sprint, contendo a explicação com textos e imagens.

## ✩ Modelagem de Dados Relacional e Dimensional com linguagem SQL

- [Arquivos SQL](/Sprint2/Desafio/Arquivos%20SQL/)
- [Evidências do Desafio](/Sprint2/Evidencias/Evidencias%20Desafio/)
- [Ilustração Modelo Relacional](/Sprint2/Evidencias/Evidencias%20Desafio/ConcessionariaER.jpg)
- [Ilustração Modelo Dimensional](/Sprint2/Evidencias/Evidencias%20Desafio/DimensionalConcessionaria.jpg)

O desafio é a **normalização** da base de dados tb_locacao, ou seja, aplicar as formas normais e depois converter o **modelo relacional** em **modelo dimensional**.

1. [Download do arquivo concessionaria.zip](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Desafio/Desafio.md#1-download-do-arquivo-concessionariazip)
2. [Normalizar a base de dados](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Desafio/Desafio.md#2-normalizar-a-base-de-dados)
3. [Modelo dimensional baseado no modelo relacional](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Desafio/Desafio.md#3-modelo-dimensional-baseado-no-modelo-relacional)

### 1. Download do arquivo concessionaria.zip
O arquivo possui uma tabela tb_locacao populada, então fiz a análise dos dados para encontrar as repetições e atributos que se relacionavam entre si para realizar a normalização.

A tabela e a base de dados antes da normalização estava assim:

![tb_locacao](/Sprint2/Evidencias/Evidencias%20Desafio/tb_locacao.png)

Os dados presentes no BD:

![tb_locacao dados 1](/Sprint2/Evidencias/Evidencias%20Desafio/tb_locacaoDados1.png)

![tb_locacao dados 2](/Sprint2/Evidencias/Evidencias%20Desafio/tb_locacaoDados2.png)

![tb_locacao dados 3](/Sprint2/Evidencias/Evidencias%20Desafio/tb_locacaoDados3.png)

### 2. Normalizar a base de dados

De inicio, para começar a normalização, já notei que haveria uma tabela para Locacao (que teria as seguintes chaves estrangeiras FK: idCliente, idVendedor e idCarro), Cliente, Carro, Vendedor e Combustível.

Então comecei separando as tabelas pelos atributos que se relacionavam entre si. Iniciei criando o **Esquema Relacional (Crows Foot)**, acho mais fácil para fazer a criação das tabelas com o desenho explicativo.

- Utilizei o site do [miro](https://miro.com/pt/) para fazer o Esquema Relacional a seguir:

![Esquema Relacional Miro](/Sprint2/Evidencias/Evidencias%20Desafio/ConcessionariaER.jpg)

- Utilizei o [Dbeaver](https://dbeaver.io/) para realizar os Scripts SQL


A partir do Esquema Relacional feito, fui realizar o Script para criar as tabelas.
- Script criação de tabelas normalizadas -> [Arquivo](/Sprint2/Desafio/Arquivos%20SQL/ScriptNormalizacao.sql)

Aqui uma imagem de como ficou o Script e sua execução:

![Criação de tabelas normalizadas](/Sprint2/Evidencias/Evidencias%20Desafio/normalizaçãoTabelas.png)

O ER fica da seguinte forma no DBeaver após a criação das tabelas normalizadas: 

![Esquema Relacional Dbeaver](/Sprint2/Evidencias/Evidencias%20Desafio/EsquemaRelacional.png)

Após a criação das tabelas no DBeaver era preciso povoar esse BD para checar se os tipos dos dados estavam coerentes e se a normalização estava correta. Pensei em como faria isso de forma ágil, então eu utilizei consultas SQL na tb_locacao adaptando o resultado para as tabelas que criei.

Segue algumas imagens que ilustram a ação:

![Consulta tb_locacao](/Sprint2/Evidencias/Evidencias%20Desafio/ObtendoDadostb_locacao.png)

![Consulta tb_locacao](/Sprint2/Evidencias/Evidencias%20Desafio/consultaPovoarBD.png)

![consulta tb_locacao](/Sprint2/Evidencias/Evidencias%20Desafio/dadostb_locacaoObtidos.png)

Após gerar esses resultados das consultas, eu gerava um Script de inserção para popular o BD normalizado:

- Script para popular tabelas normalizadas -> [Arquivo](/Sprint2/Desafio/Arquivos%20SQL/PopularTabelas.sql)


![insere 1](/Sprint2/Evidencias/Evidencias%20Desafio/scriptInsere1.png)

![insere 2](/Sprint2/Evidencias/Evidencias%20Desafio/scriptInsere2.png)

![insere 3](/Sprint2/Evidencias/Evidencias%20Desafio/scriptInsere3.png)

### 3. Modelo dimensional baseado no modelo relacional

Agora era preciso realizar o modelo dimensional desse BD da concessionaria. A partir do vídeo disponibilizado na Udemy e nos trechos do desafio, fiz as views de dimensões e fato das tabelas. Foi preciso fazer poucas alterações para seguir o modelo relacional, a normalização em si já ficou quase coerente com o modelo dimensional. Foi preciso mudar apenas o id do combustível, adicionar na tabela de locacao.

- Script das views para o modelo dimensional -> [Arquivo](/Sprint2/Desafio/Arquivos%20SQL/ViewsDimensional.sql)

Segue as imagens que evidênciam essa ação:

![views criação](/Sprint2/Evidencias/Evidencias%20Desafio/view.png)

![checandocriação de view](/Sprint2/Evidencias/Evidencias%20Desafio/ChecarCriacaoFatoLocacao.png)
