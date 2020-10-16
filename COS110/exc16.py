"""
    Dado um inteiro n, esse programa imprime os primos circulares até n
    Exercício 16 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def size (integer):
    """ Retorna o tamanho de um inteiro """
    size=0
    if (integer != 0):
        while (integer >= 1):
            integer = integer/10
            size +=1
    else:
        size = 1
    return size

def sao_primos (n):
    """ Retorna todos os primos até n*10 """
    primos = []
    nao_primos = [0]*(n+1)
    for i in range(2, n+1):
        if nao_primos[i] != 1:
            primos.append(i) 
            for j in range (i, n+1, i):
                nao_primos[j] = 1
    return primos

def rotaciona (integer, size):
    """ Retorna todas as rotações de um inteiro """
    int_list = [int(x) for x in str(integer)] # transforma o int em list
    rotacionados = []
    for i in range(size):
        int_list.append(int_list.pop(0)) # rotaciona
        str_int = ''
        for integ in int_list: # transforma a lista em string
            str_int+= str(integ)
        rotacionado = int(str_int) # transforma a string em int
        rotacionados.append(rotacionado) # adiciona o int a list de rotacionados
    return rotacionados

def sao_primos_circulares (n):
    """ Retorna todos os primos circulares até n """
    primos_10 = sao_primos(10**size(n)) # primos ate 10^digitos de n pra garantir q vms conferir todas as rotacoes
    primos = sao_primos(n) 
    primos_circulares = []
    for primo in primos:
        primos_rotacionados = rotaciona(primo, size(primo)) # cria uma lista com o primo rotacionado
        verificador = 0
        for primo_rotacionado in primos_rotacionados:
            # esse loop verifica se todas as rotações são números primos
            if primo_rotacionado in primos_10:
                verificador+=1
        if verificador == len(primos_rotacionados):
            # se sim, todas as rotações são números primos, então é um primo circular
            primos_circulares.append(primo)
    return primos_circulares

n=int(input())
print (sao_primos_circulares(n))

        
