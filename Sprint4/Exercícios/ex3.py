"""
reduce(módulo functools) e map.

Função recebe uma lista de tuplas e calcula
o saldo a partir dos valores, "C" para crédito
"D" para débito.

"""
from functools import reduce


def calcula_saldo(lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    return reduce(lambda ant, valor: ant + valor, valores)


lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

print(calcula_saldo(lancamentos))
