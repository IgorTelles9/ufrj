"""
    Esse programa verifica se o número dado é um número de Lychrel ou não
    Exercício 13 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def fatorLychrel (inteiro, j=0):
    inteiro_list = [int(x) for x in str(inteiro)]
    inteiro_list.reverse()
    inteiro_str = ''
    for i in range(len(inteiro_list)):
        inteiro_str += str(inteiro_list[i])
    inteiro_invertido = int (inteiro_str)
    if inteiro == inteiro_invertido:
        return j 
    else:
        if j < 50:
            inteiro += inteiro_invertido
            j+=1
            return fatorLychrel(inteiro, j)
        else:
            return -1

integer = int(input())
print(fatorLychrel(integer))

