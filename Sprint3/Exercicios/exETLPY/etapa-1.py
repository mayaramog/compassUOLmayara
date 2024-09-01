"""
Etapa 1.

Apresente o ator/atriz com o maior número de filmes e a 
respectiva quantidade. A quantidade de filmes encontra-se
na coluna Number of movies do arquivo.

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

qtd_max_filme = 0
ator_max_filmes = ""
for i, registro in enumerate(dados.splitlines()):
    if i == 0:
        # Pula a primeira linha sem valores
        continue

    divide = verifica_sprdr(registro)

    ator = divide[0]
    qtd_filme_str = divide[2].strip()

    # Conversão da string
    try:
        # Transforma string em inteiro
        qtd_filme = int(qtd_filme_str)
    except ValueError:
        print(f"Erro ao converter quantidade de filmes.")
        continue

    if qtd_filme > qtd_max_filme:
        qtd_max_filme = qtd_filme
        ator_max_filmes = ator

resultado = f"Ator/Atriz com o maior quantidade de filmes: {ator_max_filmes} -> Quantidade de filmes: {qtd_max_filme}"

with open("etapa-1.txt", "w", encoding="utf-8") as dest:
    dest.write(resultado)

print(f"\n{resultado}")
print("\nInformação salva em arquivo etapa-1.txt!\n")
