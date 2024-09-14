# Desafio

O desafio da Sprint 4 consiste na cosntrução de imagens e containers a partir de um código phyton, reutilizar ou reiniciar um container e construir um código python que gera uma hash a partir de ums string recebida no input e a impressão dessa hash co o método hexdigest.

## Etapa 1 -> Criação de imagem para rodar um programa

A etapa 1 do desafio consiste em baixar o arquivo com extensão python [carguru.py](/Sprint4/Desafio/carguru/carguru.py), criar um arquivo Dockerfile e utilizar os comandos build e run para criar a imagem e o container.

Primeiro fui encontrar a imagem de Python no site do Docker
O primeiro passo foi navegar até o site do Docker que foi mostrado nas videoaulas da Udemy.

No site da [imagem Python](https://hub.docker.com/_/python) tem um guia de como realizar Dockerfiles e rodar imagens novas a partir dessa imagem python:
![img1](/Sprint4/Evidências/Preparação/siteDockerPython.png)

A partir dessa leitura, iniciei a criação do [Dockerfile](/Sprint4/Desafio/carguru/Dockerfile) e utilizei o comando com build:
![img2](/Sprint4/Evidências/Desafio%20carguru/buildImagem.png)

Após isso, utilizei o comando run interativo com o terminal, para não precisar abrir o DockerDesktop para averiguar e após isso, verifiquei o ID do container criado com o comando de listagem de dockers:
![img2](/Sprint4/Evidências/Desafio%20carguru/runImagem.png)

## Etapa 2 - Reiniciar e reutilizar containers

É possivel reutilizar e reiniciar containers? A resposta é sim! Basta conferir se o container está sendo utilizado, caso sim é utilizado o comando restart, caso não, o comando start, segue a resolução que fiz com o container criado para o carguru.py:

Após obter o ID do container criado, reiniciei o container:
![img3](/Sprint4/Evidências/Desafio%20carguru/reiniciarContainer.png)

Como ficam os logs no DockerDesktop:

![img4](/Sprint4/Evidências/Desafio%20carguru/dockerDesktop.png)

## Etapa 3 -> Criar arquivo python e gerar hash de String

A etapa atual consiste na criação de um arquivo Python que receba uma String e gere uma hash por meio do algoritmo SHA-1 (Secure Hash Algorithm 1) que criptografa a String recebida em uma sequência de bytes, após isso utilizar a função hexdigest para representar o hashing em formato hexadecimal.

Iniciei fazendo o arquivo python [etapa3.py](/Sprint4/Desafio/mascarar-dados%20e%20hash/etapa3.py), depois criei a imagem [mascarar-dados.Dockerfile](/Sprint4/Desafio/mascarar-dados%20e%20hash/mascarar-dados.Dockerfile) seguindo o mesmo padrão da etapa 1, somente alterei o caminho e o arquivo python.

Utilizei os comandos com build e run:

![img3.1](/Sprint4/Evidências/Desafio%20mascarar-dados%20e%20hash/buildImagem.png)

![img3.2](/Sprint4/Evidências/Desafio%20mascarar-dados%20e%20hash/runImagem.png)

Por mais que a etapa exija que o arquivo python permita a inserção de mais de uma string, até um comando de parada, eu reiniciei o container após o seu encerramento apenas como uma forma de demonstração de reinicialização com um container diferente:

![img3.3](/Sprint4/Evidências/Desafio%20mascarar-dados%20e%20hash/reiniciarContainer.png)

Como ficou os logs no DockerDesktop:
![img3.4](/Sprint4/Evidências/Desafio%20mascarar-dados%20e%20hash/dockerDesktop.png)

## Evidências extra

Meu DockerDesktop:

![evi1](/Sprint4/Evidências/Preparação/dockerDesktop.png)

Utilizei uma pasta da minha máquina e fiz a criação dos arquivos no Visual Studio Code:

![evi2](/Sprint4/Evidências/Preparação/ArquivosNoVSC.png)
