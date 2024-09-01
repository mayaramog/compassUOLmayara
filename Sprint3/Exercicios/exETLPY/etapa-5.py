"""

Etapa 4.

Identificar os filmes #1 e contar a quantidade
de vezes em que eles aparecem no arquivo csv.

"""


def verifica_sprdr(linha):
    campos = []
    campo = ""
    conteudo = False

    for sep in linha:
        if sep == '"':
            conteudo = not conteudo
        elif sep == ',' and not conteudo:
            campos.append(campo)
            campo = ""
        else:
            campo += sep

    if campo:
        campos.append(campo)
    
    return campos


# Abertura do arquivo CSV
with open("actors.csv", "r", encoding="utf-8") as arquivo:
    dados = arquivo.read()

result = []

# Processa cada linha do CSV
for i, registro in enumerate(dados.splitlines()):
    if i == 0:
        # Pula a primeira linha (cabeçalho)
        continue

    divide = verifica_sprdr(registro)

    result.append(f"{divide[0]} - {divide[1]}")

result.sort(key=lambda x: x.split(" - ")[1], reverse=True)

# Imprime no terminal pra checar se o codigo está funcionando
for linha in result:
    print(linha)

with open("etapa-5.txt", "w", encoding="utf-8") as dest:
    # Grava cada linha da lista result no arquivo
    for linha in result:
        dest.write(f"{linha}\n")