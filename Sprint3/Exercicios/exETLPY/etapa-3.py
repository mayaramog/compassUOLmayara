"""

Etapa 3.

Apresente o ator/atriz com a maior média
de receita de bilheteria bruta por filme
na coluna Average per Movie.
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

maior = 0
ator = ""
for i, registro in enumerate(dados.splitlines()):
    if i == 0:
        # Pula a primeira linha sem valores
        continue

    divide = verifica_sprdr(registro)

    atual = float(divide[3])

    if atual > maior:
        maior = atual
        ator = divide[0]

with open("etapa-3.txt", "w", encoding="utf-8") as dest:
    dest.write(f"O ator/atriz com a maior média de receita de bilheteria bruta por filme é o/a {ator} com {maior} de bilheteria")


print(f"\nO ator/atriz com a maior média de receita de bilheteria bruta por filme é o/a {ator} com {maior} de bilheteria\n")
