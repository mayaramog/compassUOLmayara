# Sprint 5 ⋆
## Sumário
- ### [Curso AWS Cloud Quest: Cloud Practitioner](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint5/README.md#curso-aws-cloud-quest-cloud-practitioner-1)
- ### [Curso AWS Certified Cloud Practitioner](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint5/README.md#curso-aws-certified-cloud-practitioner-1)
- ### [Exercícios propostos na Sprint 5]()
- ### [Desafios propostos na Sprint 5](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint5/README.md#desafios-propostos-na-sprint-5-1)
- ### [Dificuldades encontradas](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint5/README.md#dificuldades-encontradas-1)
- ### [Pontos a melhorar para a próxima Sprint](https://github.com/mayaramog/compassUOLmayara/blob/main/Sprint5/README.md#pontor-a-melhorar-para-a-pr%C3%B3xima-sprint)

## Curso AWS Cloud Quest: Cloud Practitioner
- Link da certificação: https://www.credly.com/badges/11c486c2-e633-4484-b9f2-7b58ace1d735/public_url

![Certificação cloud quest](/Sprint5/Evidências/aws-cloud-quest-cloud-practitioner-mayara-goncalves.png)

- [Evidências](/Sprint5/Evidências/GameAWS/) do processo de finalização do jogo da AWS Cloud Quest

## Curso AWS Certified Cloud Practitioner

Curso de preparação para a prova da AWS

- [Certificado](/Sprint5/Certificados/18719_5_6046265_1727467355_AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)

## Exerícios propostos na Sprint 5

- ### LAB AWS S3
A orientação foi que deveriamos criar uma instância no EC2 da AWS antes de iniciar o uso da conta AWS para os exercícios e desafios, segue o link para as imagens de criação dessa instância: [Processo de criação da instância com as especificações necessárias](/Sprint5/Evidências/Instância/)

Após a criação da instância já era possível realizar o exercício proposto, segue as etapas:

- Etapa 1: Criar um bucket
![etapa1](/Sprint5/Evidências/Exercícios/etapa1.png)

- Etapa 2: Habilitar hospedagem de site estático
![etapa2](/Sprint5/Evidências/Exercícios/etapa2.png)

- Etapa 3: Editar as configurações do Bloqueio de acesso público
![etapa3](/Sprint5/Evidências/Exercícios/etapa3.png)

- Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível
![etapa4](/Sprint5/Evidências/Exercícios/etapa4.png)

- Etapa 5: Configurar um documento de índice
![etapa5](/Sprint5/Evidências/Exercícios/etapa5.png)

- Etapa 6: Configurar documento de erros
Arquivo criado -> [error.html](/Sprint5/Evidências/Exercícios/error.html)
![etapa6](/Sprint5/Evidências/Exercícios/etapa6.png)

- Etapa 7: Testar o endpoint do site
![etapa7](/Sprint5/Evidências/Exercícios/etapa7.png)

- Esvaziando e excluindo bucket para evitar gastos extras
![esvaziar](/Sprint5/Evidências/Exercícios/esvaziar.png)
![excluir](/Sprint5/Evidências/Exercícios/excluir.png)

## Desafios propostos na Sprint 5
- Realizar consultas (6 consultas com algumas especificações em python) em um banco de dados escolhido pelo aluno:

```
- Clausula que filtra os dados usando menos de 2 operadores lógicos
- Duas fUnções de agregação
- Uma função condicional
- Uma função de conversão
- Uma função de data
- Uma função de String
```

- O arquivo com o código das consultas -> [consultas.py](/Sprint5/Desafio/consultas.py)

O banco de dados escolhido foi um arquivo CSV que contém a bilheteria diaria das obras por exibidora do dia 06/08/2024. Para filtrar a consulta e seguir as etapas do desafio, optei por fazer um filtro por estado e trabalhar com a média e soma do público baseado nesse estado.

- Resultado das consultas:
![result1](/Sprint5/Evidências/Desafio/consulta1.png)
![result1](/Sprint5/Evidências/Desafio/consulta2.png)

- Criação do bucket:
![bucket](/Sprint5/Evidências/Desafio/bucketCriado.png)

- Carregar arquivo para o bucket:
![arquivo bucket](/Sprint5/Evidências/Desafio/arquivoCSVcarregado.png)

- Aparição de um erro de chaves de acesso, não tinha conhecimento que elas atualizavam após um tempo:
![cahve de acesso](/Sprint5/Evidências/Desafio/erroDeAttChavesAcesso.png)

## Dificuldades encontradas
- Realizar as consultas em python, não é uma linguagem que domino e me confundi ao fazer 6 consultas em uma.

## Pontor a melhorar para a próxima Sprint
- Organização de atividades e tempo
