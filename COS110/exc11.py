"""
    Esse programa verifica se uma matriz é um quadrado mágico
    Exercício 11 dos laboratórios de Alg. Prog
    Outubro de 2020
"""
def is_magic_sqr(matrix):
    soma_diag = 0
    soma_diag_sec = 0
    for i in range(len(matrix)):
        # loop calcula a soma da diagonal principal
        soma_diag += matrix[i][i]
        soma_diag_sec += matrix[i][len(matrix)-i-1]
    if (soma_diag != soma_diag_sec):
        return False

    lista_somas = []
    for i in range(len(matrix)):
        soma_colunas = 0
        soma_linhas = 0
        for j in range(len(matrix)):
            # loop pra somar todas as linhas e colunas
            soma_linhas += matrix[i][j] #soma linhas
            soma_colunas += matrix[j][i] #soma colunas
        if (soma_linhas != soma_colunas or soma_linhas != soma_diag):
            # se a soma da linha é diferente da soma da coluna
            # ou se as somas sao iguais, mas sao diferentes da soma_diag
            return False
        lista_somas.append(soma_linhas)
        lista_somas.append(soma_colunas)

    for soma in lista_somas:
        # verifica se todas as somas são iguais
        if soma != lista_somas[0]:
            return False

    return True

    
matriz = eval(input())
print (is_magic_sqr(matriz))
