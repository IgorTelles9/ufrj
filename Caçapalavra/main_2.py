def ehValido(coordenadas):
    if coordenadas[0] >= 0 and coordenadas[0] <= 3 and coordenadas[1] >= 0 and coordenadas[1] <= 3:
            return True
    else:
        return False

def checa_preenchido(coordenadas):
    """ Verifica se a célula está preenchida por uma letra """
    if matriz[coordenadas[0]][coordenadas[1]]:
        return True
    return False

def checa_repeticao(letra):
    """ Verifica se a letra já está na matriz """
    for i in range(4):
        for j in range (4):
            if letra == matriz[i][j]:
                return [i,j]
    return False

def gera_adjacencias (coordenadas):
    """ Retorna os limites de adjacências da coordenada"""
    if coordenadas[0] > 0:
        i = coordenadas[0] - 1 
        if coordenadas[0] == 1: 
            limite_i = 3
        else:
            limite_i = 4
    else:
        i = 0
        limite_i = 2

    # define as adjacências das colunas
    if coordenadas[1] > 0: 
        j = coordenadas[1]  - 1 
        if coordenadas[1] == 1:
                limite_j = 3
        else:
            limite_j = 4
    else:
        j = 0
        limite_j = 2
    
    return i,j,limite_i,limite_j

def checa_adjacencias(i, j, limite_i, limite_j, item, coordenadas_palavra_atual):
    """ 
    Verifica se a coordenada dada tem ao menos uma adjacência com o item. 
    Retorna a coordenada, se houver. Senão, retorna False.
    """
    const_j = j
    coordenadaAtual = False
    while (i < limite_i): 
        j=const_j
        while (j < limite_j): 
            if matriz[i][j] == item and not ([i,j] in coordenadas_palavra_atual):
                coordenadaAtual = [i,j]
                return coordenadaAtual
            j+=1
        i+=1
    return coordenadaAtual

def adiciona_aleatoriamente(matriz, i, j, limite_i, limite_j,coordenadas_palavra_atual):
    while True:
        coordenadaAtual = [randint(i, limite_i-1), randint(j, limite_j-1)]
        m,n,limite_m,limite_n = gera_adjacencias(coordenadaAtual)
        adjacencia_livre = checa_adjacencias(m,n,limite_m,limite_n,0,coordenadas_palavra_atual)
        if not(checa_preenchido(coordenadaAtual)) and adjacencia_livre: #se a coordenada estiver vazia e a adjacencia estiver vazia
            break
    matriz[coordenadaAtual[0]][coordenadaAtual[1]] = letra
    coordenadas_palavra_atual.append(coordenadaAtual)  

""" main """
from time import time
start = time()
from random import randint
palavras = ['sala', 'casa', 'sofa', 'teto']
#palavras = ['vitoria','igor']
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
coordenadas_palavra_atual = [] # essa lista guarda as coordenadas das letras inseridas em cada palavra

for palavra in palavras: # percorre cada palavra na lista de palavras
    coordenadas_palavra_atual = [] # reseta a lista pra uma nova palavra
    for letra in palavra: # percorre cada letra por palavra

        if coordenadas_palavra_atual == []: # primeira letra: verifica toda matriz
            i,j = (0,0)
            limite_i, limite_j = (4,4)
        else: # outras letras: verifica as adjacencias
            i, j, limite_i, limite_j = gera_adjacencias(coordenadas_palavra_atual[-1]) # gera as adjs da ultima letra inserida
        
        coordenadaAtual = checa_adjacencias(i,j,limite_i,limite_j, letra, coordenadas_palavra_atual) # procura a letra nas adjs da ultima letra da palavra
    
        if coordenadaAtual: # ja existe a letra na matriz
            # checa se a letra tem ao menos uma célula adjacente vazia
            i,j,limite_i,limite_j = gera_adjacencias(coordenadaAtual)
            adjacencia_vazia = checa_adjacencias(i,j,limite_i,limite_j, 0, coordenadas_palavra_atual)
            if adjacencia_vazia: # adjacencia vazia identificada
                coordenadas_palavra_atual.append(coordenadaAtual)
            else: #sem adjacencia vazia; adiciona a letra em uma adjacencia da letra anterior
                adiciona_aleatoriamente(matriz,i,j,limite_i,limite_j, coordenadas_palavra_atual)
        else: # letra não existe na matriz; adiciona a letra em uma adjacencia da letra anterior
            adiciona_aleatoriamente(matriz,i,j,limite_i,limite_j, coordenadas_palavra_atual)


        print(matriz[0])    
        print(matriz[1])
        print(matriz[2])
        print(matriz[3])
        print()

        
print(matriz[0])    
print(matriz[1])
print(matriz[2])
print(matriz[3])
print()
end=time()
print(end-start) #0.04400038719177246
        

