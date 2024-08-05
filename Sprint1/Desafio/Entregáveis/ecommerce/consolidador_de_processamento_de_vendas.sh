#!/bin/bash

# Nome do arquivo final onde todos os relatórios serão unido
relat_fi="relatorio_fina.txt"

# Limpar o relatorio final caso já exista, como eu não irei apagar nenhum relatorio, não há problemas em sobrescrever tudo
echo "Criando ou limpando arquivo para a operação..."
> "$relat_fi"

# Juntar todos os relatorios em um relatorio final
echo "Agrupando relatórios..."
ls vendas/backup | grep "^relatorio" | while read -r arq; do
    cat "vendas/backup/$arq" >> "$relat_fi"
    printf "\n-------------------------------\n" >> "$relat_fi"
done
echo "Execuçao realizada com sucesso!"
