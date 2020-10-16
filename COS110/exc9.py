""" 
    Exercício 7 dos laboratórios de Alg. Prog
    Esse programa recebe realiza divisão inteira por recursão
    Laboratório Alg. Prog. ECI / Set. 2020 
"""  

def divisao_inteira(dividendo, divisor):
    if dividendo < divisor:
        return 0
    return divisao_inteira(dividendo-divisor, divisor) + 1

n1 = int(input())
n2 = int(input())
print(divisao_inteira(n1,n2))