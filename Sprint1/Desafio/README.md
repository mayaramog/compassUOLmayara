# Desafios propostos na Sprint 1
Nesta seção será apresentado um guia de resolução dos desafios propostos na Sprint, contendo a explicação com textos e imagens, além de comentários sobre as dificuldades encontradas ao longo da Sprint, pontos que pretendo melhorar na próxima Sprint e explicação dos conteúdos vistos fora da Udemy propostos.
- ### [Repositório e apresentação no GitHub]() 
- ### [Prática e comandos Linux e Markdown]()

## ✩ Repositório e apresentação no GitHub
Segue abaixo um link para a minha apresentação README na formataçãod de Markdown como foi proposto:


✧ [Repósitorio Mayara -> README.md](https://github.com/mayaramog/compassUOLmayara/tree/main?tab=readme-ov-file#readme)

> [!NOTE]
> Utilizei um pouco de HTML para uma formatação mais espefícica dos gifs e imagem.

## ✩ Prática de comandos Linux e Markdown
### Etapas
- [1.Entregáveis]()
- [2.Preparação]()
- [3.Desafio]()
- [3.1.Criar arquivo executável]()
- [3.2.Agendar a execução do processamento]()
- [3.3.Criar novo relatório]()

### 1. Entregáveis

Caminho para a pasta da entrega com **todos** arquivos exigidos para a entrega do desafio: [Link](/Sprint1/Desafio).

- Arquivo executável [processamento_de_vendas](/Sprint1/Desafio/Entregáveis/ecommerce/processamento_de_vendas.sh)
- Arquivo executável [consolidador_de_processamento_de_vendas](/Sprint1/Desafio/Entregáveis/ecommerce/consolidador_de_processamento_de_vendas.sh)
- Original [dados_de_vendas](/Sprint1/Desafio/Entregáveis/ecommerce/Relatorios%20e%20dados%20de%20vendas/dados_de_vendas.csv)
- 1º modificação [dados_de_vendas](/Sprint1/Desafio/Entregáveis/ecommerce/Relatorios%20e%20dados%20de%20vendas/dados_de_vendas_1º_modificacao.csv)
- 2º modificação [dados_de_vendas](/Sprint1/Desafio/Entregáveis/ecommerce/Relatorios%20e%20dados%20de%20vendas/dados_de_vendas_2º_modificacao.csv)
- Pasta de [Evidências](/Sprint1/Evidências)
- As pastas Certificados e Exercícios não exisite pois não há certificados fora da Udemy gerados e exercícios propostos na Sprint


### 2. Preparação

- Download do arquivo dados_de_vendas.csv
- Criação do diretório ecommerce e passagem do dados_de_vendas.csv para o novo diretório, utilizei os comandos no terminal Linux:
```
cd Documents
mkdir ecommerce
mv dados_de_vendas.csv ecommerce
```
- Pasta ecommerce (tirei print apenas após a execução do arquivo processamento_de_vendas.sh, por tanto já contem os outros diretórios):

![Pasta ecommerce](/Sprint1/Evidências/pastaComProcessadorEConsolidador.png)

### 3. Desafio
Gerar relatórios de vendas

### 3.1. Criar arquivo executável

- Para criar o arquivo utilizei o comando no terminal linux:
```
vim processador_de_vendas.sh
```
Adicionei os comandos no executável, utilziando Script Shell, seguindo os passos do desafio. Ficou assim:


![processamento_de_vendas.sh](/Sprint1/Evidências/codigoProcessamento.png)

> [!NOTE]
> Não é o segundo registro, mas sim o primeiro, a correção já foi efetuada no arquivo!!
![processamento_de_vendas.sh](/Sprint1/Evidências/codigoProcessamento2.png)

![processamento_de_vendas.sh](/Sprint1/Evidências/codigoProcessamento3.png)

Adicionando permissões de execução para o arquivo:

![permissões processamento_de_vendas](/Sprint1/Evidências/permissaoxProcessamento.png)

Como fica a execução no terminal:

![processamento_de_vendas.sh no terminal](/Sprint1/Evidências/execucaoComentProcessamentoVenda.png)


Modificação feita no executável para imprimir as 10 primeiras linhas do arquivo no terminal Linux:


![processamento_de_vendas.sh imprime dados no terminal](/Sprint1/Evidências/codigoImprimeTerminalProcessador.png)

Excecução no terminal:

![processamento_de_vendas.sh impressão no terminal](/Sprint1/Evidências/processamentoImprimeTerminal.png)


- Mostrando como ficam as pastas criadas:

Primeiro fiz alguns testes para checar o funcionamento do relatório, como mostrado no código acima, o relatório vai sendo incrementado a cada execução do processamento_de_vendas.sh e o arquivo zip é atualizado, dessa forma fica mais organizado.
A incrementação começa por relatorio0.txt (caso ainda não exista nenhum relatorio)

![Checagem de relatorio](/Sprint1/Evidências/verificandoRelatorio.png)


### 3.2. Agendar a execução do processamento

- Primeiro, verifiquei se o crontab existia na minha máquina Linux, como não existia, verifiquei a atualização do Linux e fiz a instalação com os seguintes comandos:
```
sudo apt update
sudo apt install cron
sudo systemctl enable cron
```
Após a instalação e configuração do editor de texto (utilizei o nano) do crontab, comecei a testar os comandos:

![verificando crontab 2](/Sprint1/Evidências/testandoContrab2.png)
 
Após mais alguns testes, configurei para o agendamento requerido, as 15:27, mas como houveram alguns contratempos e precisei mudar algumas coisas no código, deixei para executar todos os dias e não de segunda a quinta.

![configurando agendamento](/Sprint1/Evidências/testandoContrab.png)

Mas caso eu fizesse a execução de segunda a quinta, utilizaria o seguinte comando no editor de texto nano:
```
27 15 * * 1-4 cd home/mayara/Documents/ecommerce/ && ./processamento_de_vendas.sh
```
### 3.3. Criar novo relatório
- Modificação do arquivo dados_de_vendas.csv
1. Arquivo original e relatório gerado com o agendamento:

 ![1 dados de vendas](/Sprint1/Evidências/dadosDeVendaOriginal.png)

 ![1 execucao agendada](/Sprint1/Evidências/1ExecucaoAgendada.png)

 2. 1º modificação do arquivo e relatório gerado com o agendamento:

![1 modificacao dados de vendas](/Sprint1/Evidências/2modificacaoDados.png)

![2 execucao agendada](/Sprint1/Evidências/2execucaoAgendada.png)

>[!NOTE]
> Acabei me esquecendo de ligar a máquina, por isso o agendamento não foi executado, isso causou o atraso do relatório em 1 dia.

3. 2º modificação do arquivo e relatório gerado com o agendamento:

![2 modificacao dados de vendas](/Sprint1/Evidências/3modificacaoDados.png)

![3 execucao agendada](/Sprint1/Evidências/3execucaoAgendada.png)

- Criação do Script consolidador_de_processamento_de_vendas.sh

Para a criação, utilizei os seguintes comandos:
```
cd Documents/ecommerce
vim consolidador_de_processamento_de_vendas.sh
```
O arquivo executável tem como função agrupar os relatórios gerados até então formando um relatório final.

Após salvar o arquivo, o script ficou da seguinte forma:

![consolidador](/Sprint1/Evidências/codigoConsolidador.png)

Também adicionei permissões de execução para esse executável, da mesma forma que fiz com o processamento_de_dados.sh, com o seguinte comando:
```
chmod 755 consolidador_de_processamento_de_vendas.sh
```
As permissões dos arquivos executáveis ficaram assim:

![permissões executaveis](/Sprint1/Evidências/permissoesExecutaveis.png)

Após as execuções agendadas do processador ocorrerem, executei manualmente o consolidador:

![consolidador execucao](/Sprint1/Evidências/execucaoConsolidador.png)

O relatório final, que concatena os gerados até entao, ficou assim:

![relatorio final 1](/Sprint1/Evidências/relatoriofi1.png)

![relatorio final 2](/Sprint1/Evidências/relatoriofi2.png)

---