"""

generator.

funcao pares_ate retorna um generator, ou seja
um yield para os valores pares no intervalo [2,n].

"""


def pares_ate(n:int):
    for num in range(2, n + 1):
        if num % 2 == 0:
            yield num


generator = pares_ate(20)

for par in generator:
    print(par)
