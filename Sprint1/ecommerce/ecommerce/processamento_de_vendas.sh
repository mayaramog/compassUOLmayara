#!/bin/bash

echo "Executando o arquivo processamento_de_vendas.sh..."

# Verificação e criação do diretório vendas, se não existir é criado, nas próximas vezes, como já existirá não será necessária a criação
if [ ! -d "vendas" ]; then
    echo "Diretório 'vendas' inexistente, criando diretório..."
    mkdir vendas
else
    echo "Diretório 'vendas' já existente, continuar execução..."
fi

# Copia o arquivo dados_de_vendas.csv para o diretório vendas
    echo "Copiando o arquivo 'dados_de_vendas.csv' para o diretório 'vendas'..."
    cp dados_de_vendas.csv vendas

# Mudando para o diretório vendas
cd vendas

# Verificação e criação do diretório backup, se não existir
if [ ! -d "backup" ]; then
    echo "Diretório 'backup' inexistente, criando diretório..."
    mkdir backup
else
    echo "Diretório 'backup' já existente, continuar execução..."
fi

# Copia o arquivo dados_de_vendas.csv para o diretório backup
echo "Copiando o arquivo 'dados_de_vendas.csv' para o diretório 'backup'..."
cp dados_de_vendas.csv backup

# Mudando para o diretório backup
cd backup

# Renomeando o arquivo dados_de_vendas.csv
echo "Renomeando o arquivo 'dados_de_vendas.csv' para adicionar a data de execução..."
novo_nome="dados-$(date +%Y%m%d).csv"
mv dados_de_vendas.csv "$novo_nome"
mv "$novo_nome" "backup-$novo_nome"

echo "Verificando a quantidade de relatorios já gerados para realizar a incrementação..."
qtd=$(ls | grep "^relatorio" | wc -l)
novo_relatorio="relatorio${qtd}.txt"

echo "Escrevendo a data do sistema no arquivo..."
printf "%s\n" "$(date +%Y/%m/%d\ %H:%M)" > "$novo_relatorio"

# Escrevendo o primeiro e ultimo registro
echo "Escrevendo a data do segundo registro do arquivo..."
tail -n +2 "backup-$novo_nome" | head -n 1 | awk -F',' '{print $5}' | awk -F/ '{print "Primeiro registro: " $3 "/" $2 "/" $1}' >> "$novo_relatorio"

# Escrever a data do último registro no arquivo relatorio.txt
echo "Escrevendo a data do último registro do arquivo..."
tail -n 1 "backup-$novo_nome" | awk -F',' '{print $5}' | awk -F/ '{print "Último registro: " $3 "/" $2 "/" $1}' >> "$novo_relatorio"

rm -f ordena_data.txt

echo "Escrevendo a quantidade de produtos diferentes..."
qtd_prod=$(wc -l < "backup-$novo_nome")
qtd_prod=$((qtd_prod - 1))
printf "%s\n" "Quantidade de produtos diferentes: $qtd_prod" >> "$novo_relatorio"

echo "Escrevendo as 10 primeiras linhas no arquivo..."
printf "%s\n" "$(head -n 10 "backup-$novo_nome")" >> "$novo_relatorio"

echo "Comprimindo arquivo "backup-$novo_nome"..."
zip backup-$novo_nome.zip backup-$novo_nome

echo "Excluindo arquivos..."
rm -f backup-$novo_nome
cd ../
rm -f dados_de_vendas.csv

echo "Encerrando a execução com sucesso!"
