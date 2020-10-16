
"""
    Exercício 6 dos laboratórios de Alg. Prog
    Esse programa calcula a determinante de uma matriz quadradada
    com tamanho >= 4
    Laboratório Alg. Prog. ECI / Set. 2020 
"""

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



def remove_linha_coluna(matriz, coluna):
    """ remove a coluna e a linha indicada """
    matriz_cortada = []
    for i in range(len(matriz)):
        if(i != 0):
            linha = []
            for j in range(len(matriz[i])):
                if j != coluna:
                    linha.append(matriz[i][j])
            matriz_cortada.append(linha)

    return matriz_cortada


def calcula_det(matriz):
    """ calcula o determinante de qualquer matriz quadrada >= 4x4 """
    linhas_matriz = len(matriz)
    colunas_matriz = len(matriz[0])
    if linhas_matriz < 4:
        det = det_tres(matriz)
        return det 
    else:
        soma = 0
        for j in range(colunas_matriz):
            matriz_temp = remove_linha_coluna(matriz, j)
            soma += matriz[0][j] * (-1)**(j+2) * calcula_det(matriz_temp)

    return soma   

   

matriz = eval(input())
det = calcula_det(matriz)
print(det)
             