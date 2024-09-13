"""

max, zip e map.

duas listas, uma com operadores e outra com
tuplas de numeros, realizar cada operacao de operadores
com os números.

"""


def calcular_valor_maximo(operadores,operandos) -> float:
    
    def operacao(op, x, y) -> float:
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y
        if op == "%":
            return x % y


    aplicar_op = lambda op: operacao(op[0], op[1][0], op[1][1])
    
    eltos = zip(operadores, operandos)
    
    results = map(aplicar_op, eltos)
    
    return max(results)


operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores,operandos))
