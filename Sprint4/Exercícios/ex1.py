"""
lambda e high order functions.

A partir de number.txt, apresentar os 5 maiores
valores pares e a soma utilizando as funções:
map, filter, sorted e sum.

"""


with open("number.txt") as arquivo:
    # Conversão para inteiro
    numeros = list(map(int, arquivo))
    
# Função pares para identificar os pares, filter para filtrar e sorted para decrescente
pares = sorted(filter(lambda num: num % 2 == 0, numeros), reverse=True)

maioresp = pares[:5]
soma = sum(maioresp)

print(maioresp)
print(soma)
