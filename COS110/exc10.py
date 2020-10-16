"""
    Inverte um inteiro >= 0 e conta quantos dígitos ele tem.
    Programa do exercício 10 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def size (integer):
    size=0
    if (integer != 0):
        while (integer >= 1):
            integer = integer/10
            size +=1
    else:
        size = 1
    return size

def invert (integer, size):
    int_list = [int(x) for x in str(integer)]
    int_list.reverse()
    str_integer = ''
    for i in range(size):
        str_integer += str(int_list[i])
    inverted = int(str_integer)
    return inverted

numero = int(input())
tamanho = size(numero)
invertido = invert(numero, tamanho)
saida = (tamanho, invertido)
print(saida)