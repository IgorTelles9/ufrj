"""
    Exercício 5 dos laboratórios de Alg. Prog
    Esse programa calcula a determinante de uma matriz quadradade
    com tamanho máximo = 3
"""

def det_um (matriz):
    """ calcula o determinante de uma matriz n=1 """
    det = matriz[0]
    return det

def det_dois (matriz):
    """ calcula o determinante de uma matriz n=2 """
    det = matriz[0][0] * matriz[1][1]
    det -= matriz[0][1] * matriz [1][0]
    return det  

def det_tres (matriz):
    """ calcula o determinante de uma matriz n=3 """ 
    soma = matriz[0][0] * matriz[1][1] * matriz[2][2]
    soma += matriz[0][1] * matriz[1][2] * matriz[2][0]
    soma += matriz[0][2] * matriz[1][0] * matriz[2][1]
    soma_negativa =  matriz[0][0] * matriz[1][2] * matriz[2][1]
    soma_negativa +=  matriz[0][1] * matriz[1][0] * matriz[2][2]
    soma_negativa +=  matriz[0][2] * matriz[1][1] * matriz[2][0]
    det = soma - soma_negativa
    return det

def calcula_det (matriz):
    if len(matriz) == 1: 
        return det_um(matriz)
    elif len(matriz) == 2:
        return det_dois(matriz)
    elif len(matriz) == 3: 
        return det_tres(matriz)

matriz = eval(input ())
determinante = calcula_det(matriz)
print(determinante)



