"""
    Exercício 18 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def mesma_soma_algarismos(lista):
    somas = []
    for i in range(len(lista)):
        int_list = [int(x) for x in str(lista[i])]
        iguais = []
        soma = sum(int_list)
        if soma not in somas:
            somas.append(soma) 
    if len(somas) != 1:
        return False
    else:
        return True
lista = eval(input())
print(mesma_soma_algarismos(lista))

    
