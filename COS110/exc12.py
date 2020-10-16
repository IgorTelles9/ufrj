"""
    Exercício 12 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def particiona (lista, indice):
    lista_resultado = [0]*len(lista)
    lista_menores = []
    lista_maiores = []
    j=0
    for i in lista:
        if (i<lista[indice]):
            lista_menores.append(i)
        elif i>=lista[indice] and j != indice:
            lista_maiores.append(i)
        j+=1 # serve pra checar quando a posicao iterada for igual a do indice
    #print (lista_menores)
    #print (lista_maiores)
    #print(len(lista_maiores)+len(lista_menores), len(lista))

    lista_resultado[len(lista_menores)] = lista[indice]

    for i in range(len(lista_menores)):
        lista_resultado[i] = lista_menores[i]

    for i in range(len(lista_maiores)):
        lista_resultado[len(lista_menores)+i+1] = lista_maiores[i]

    return str(len(lista_menores)) +' '+ str(lista_resultado)

lista = eval(input())
indice = int(input())
print(particiona(lista , indice))