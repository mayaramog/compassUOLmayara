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

qtd = []
filmes = []

# Processa cada linha do CSV
for i, registro in enumerate(dados.splitlines()):
    if i == 0:
        # Pula a primeira linha (cabeçalho)
        continue

    divide = verifica_sprdr(registro)
    filme = divide[4]

    if filme in filmes:
        # Se o filme já está na lista, incrementa a qtd
        indice = filmes.index(filme)
        qtd[indice] += 1
    else:
        # Se o filme não está na lista, adiciona o filme e inicializa a quantidade com 1
        filmes.append(filme)
        qtd.append(1)

# Imprime o resultado
with open("etapa-4.txt", "w", encoding="utf-8") as dest:
    seq = 1;
    for i in range(len(filmes)):
        dest.write(f"{seq} - O filme {filmes[i]} aparece {qtd[i]} vez(es) no dataset.\n")
        print(f"{seq} - O filme {filmes[i]} aparece {qtd[i]} veze(s) no dataset.\n")
        seq += 1
