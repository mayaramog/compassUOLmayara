"""

Etapa 2.

Considerando todos o atores, faça a média de bilheteria
bruta de todos os filmes (coluna Gross).

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

media = 0
for i, registro in enumerate(dados.splitlines()):
    if i == 0:
        # Pula a primeira linha sem valores
        continue

    divide = verifica_sprdr(registro)

    media = media + float(divide[5].strip())

media = media / (i-1)

with open("etapa-2.txt", "w", encoding="utf-8") as dest:
    dest.write(f"A média de bilheteria bruta de acordo com a tabela Gross é: {media}")


print(f"\nA média de bilheteria bruta de acordo com a tabela Gross é: {media}\n")