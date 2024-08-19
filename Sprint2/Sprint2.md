# Sprint 2 ⋆
## Sumário
- ### [Conteúdos da Udemy](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Sprint2.md#conte%C3%BAdos-da-udemy-1)
- ### [Curso AWS Sales Accreditation (Business)](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Sprint2.md#curso-aws-sales-accreditation-business-1)
- ### [Exercícios propostos na Sprint 2](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Sprint2.md#exerc%C3%ADcios-propostos-na-sprint-2-1)
- ### [Desafios propostos na Sprint 2](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Sprint2.md#desafios-propostos-na-sprint-2-1)
- ### [Dificuldades encontradas](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Sprint2.md#dificuldades-encontradas-1)
- ### [Pontos a melhorar para a próxima Sprint](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint2/Sprint2.md#pontos-aprimorados-e-a-melhorar-para-a-pr%C3%B3xima-sprint)


## Conteúdos da Udemy
- ### SQL para Análise de Dados: Do básico ao avançado
```
Assuntos abordados:
- Instalação e uso do PgAdmin;
- Comandos básicos (SELECT, DISTINCT, WHERE ORDER BY, LIMIT);
- Operadores aritméticos, de comparação e lógicos;
- Funções agregadas, GROUP BY, HAVING;
- JOINS, UNIONS e Subquerys;
- Tratamento de dados (unidades, textos e datas);
- Manipulação de tabelas (CREATE, INSERT, ALTER, DROP, DELETE)
```
- ### Conceitos de Data e Analytics
Documentos disponibilizados:
- [Conceitos de Data e Analytics I](/Sprint2/Evidencias/Data%20e%20Analytics/DA-Conceitos+de+Data+&+Analytics+I.pdf)
- [Conceitos de Data eAnalytics II](/Sprint2/Evidencias/Data%20e%20Analytics/DA-Conceitos+de+Data+&+Analytics+II.pdf)
- ### ETL e ELT / Data Lake 
```
ETL e ELT     /    /    /    /    
- Extract-Transform-Load / Extract-Load-Transform;
- Processamento de blocos de BD na etapa de extração;
- Construção de DataWarehouse e Business Intelligence;
- Pode ser utilizado em conjunto com o Data Lake;
- Escolha de acordo com a necessidade.

Data Lake    /    /    /    /
- Local central de armazenamento de dados;
- Independe de origem ou formato;
- Não necessita de adaptação de estrutura;
- Flexibilidade.

Características do Data Lake
- Único repositório compartilhado;
- Dados estruturados, semi-estruturados e não-estruturados;
- Baixo custo de armazenamento;
- Orquestração e agendamento;
- Consumir, processar ou agir de acordo com os dados.
```
- ### Modelagem Relacional
```
- Varias coisas;
- Dados relacionados entre si;
- Características próprias;
- Entidades, Atributos, Relacionamentos;
- Modelo conceitual, lógico, físico;
- Integridade (check, nulidade, unicidade, unique, default)
- Normalização (1FN, 2FN, 3FN).
```
- ### Modelagem Dimensional
```
- Granularidade;
- OLTP vs OLAP;
- Fatos: Armazenam eventos e as chaves primárias das dimensões, praticamente ocorre como um resumo de todos os participantes do evento, é um fato;
- Dimensões: Participantes do evento, especificam as chaves presentes no fato;
- Star Schema e SnowFlake.

Ex: Evento/Fato Venda, possui como chaves: idPessoa, idProduto, quantidadeProduto. As dimensões podem ser: Pessoa, que possui o id, nome, pais, cidade..., e Produto com id, nome, fabricante, fornecedor...
```

## Curso AWS Sales Accreditation (Business)
- Conceitos de nuvem (O que é? Como usar? Por que usar?)
- Serviços da AWS
- AWS Cloud Value Framework (equipe, resiliência operacional, agilidade empresarial)
- Como lidar com objeções à nuvem (segurança e privacidade, défict de habilidades, sustentabilidade)
- Venda conjunta com a AWS (AWS Partner)
- Certificado do curso da AWS -> [Certificado Mayara](/Sprint2/Certificados/AWSSalesAccreditationMayara.png)

## Exercícios propostos na Sprint 2
- Arquivo explicativo sobre os exercícios -> [Exercicios.md](/Sprint2/Exercicios/Exercicios.md)

Os exercícios se baseiam nas queries propsotas de acordo com dois Banco de Dados disponibilizados, são esses (segue também a pasta com a resolução das consultas):
- Bilbioteca -> [Exercícios da Biblioteca](/Sprint2/Exercicios/Biblioteca/)
- Loja -> [Exercícios da Loja](/Sprint2/Exercicios/Loja/)

Além das queries, também há outro exercício que é a exportação do resultado de duas queries para .CSV, um com divisor ; e outro com divisor |, seguem os arquivos:
- [5 editoras com livros mais caros](/Sprint2/Exercicios/Biblioteca/Exportação%20CSV-Dados%20da%20Query/5EditorasComMaisLivros.csv)
- [10 livros mais caros](/Sprint2/Exercicios/Biblioteca/Exportação%20CSV-Dados%20da%20Query/10LivrosMaisCaros.csv)

## Desafios propostos na Sprint 2

Segue os links para alguns tópicos sobre o desafio da Sprint 2:

- #### [Pasta Desafio](/Sprint2/Desafio/)
- #### [Desafio.md](/Sprint2/Desafio/Desafio.md)
- #### [Arquivos SQL Desafio](/Sprint2/Desafio/Arquivos%20SQL/)

## Dificuldades encontradas
- #### Organização de tarefas no inicio da Sprint

Como eu já tive uma matéria teórica de Banco de Dados na faculdade, decidi intercalar entre as video aulas de SQL e os exercíios, o que me atrapalhou. Para mim, compensaria mais se eu tivesse dado total atenção para o curso de SQL no ínicio, por ser curto, e depois focado somente nos exercícios e desafios.

- #### Compreender o Modelo Dimensional e seus propósitos

Tive uma dificuldade para entender o Modelo Relacional, eu procurei por fora em artigos e vídeos do YouTube, além das dúvidas tiradas pelos colegas nas reuniões técnicas, mas mesmo assim sinto que ficaram lacunas no entendimento, sinto que fiocu vago. 

## Pontos aprimorados e a melhorar para a próxima Sprint

- #### Evolução da agilidade

Por mair que houveram as dificuldades acima acerca da organização de tarefas da Sprint, senti que evolui na questão de agilidade, me senti menos presa e com "medo" de fazer os desafios e estudar, fui mais positiva nessa Sprint.

- #### Aprimorar a organização

Melhorar os começos das Sprint, começar já com o pé direito e delimitando bem as tarefas do dia.

- #### Extra

Achei interessante e legal a Sprint2, gostei de aprimorar meus conhecimentos em SQL.
