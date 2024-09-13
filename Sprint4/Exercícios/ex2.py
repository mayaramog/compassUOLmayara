"""

len, filter e lambda.

Função que conta quantidade de vogais
presentes no texto passado por parâmetro.

"""


def conta_vogais(texto:str)-> int:
    vogais = ["a", "e", "i", "o", "u"]
    
    # Verifica se é vogal
    verif_vogal = lambda t: t.lower() in vogais
    
    contagem = list(filter(verif_vogal, texto))
    
    return len(contagem)


qtd = conta_vogais("Oi, meu nome é Mayara.")

print(qtd)
