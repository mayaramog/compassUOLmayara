"""

Media e sort de dicionario.

Realizar a media dos valores de um dicionario
identificar os valores maiores que a media e 
retornar uma lista com a chave e o valor.

"""


def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo)
    
    maior_media = [(item, valor) for item, valor in conteudo.items() if valor > media]
    
    # Ordena a lista pelo valor
    return sorted(maior_media, key=lambda x: x[1])


conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))
