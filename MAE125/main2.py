# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def plu (matriz, vetor_w):
    size = len(matriz)
    for n in range(size):
        # n é a linha e a coluna do pivo
        pivo = matriz[n][n]
        lower = np.identity(size)
        
        if pivo == 0:
            linha_permuta = 0
            for linha in range(n+1, size, 1):
                # procura uma linha para um novo pivo 
                if matriz[linha][n] != 0:
                    linha_permuta = linha
                    break
            matriz[[n,linha_permuta]] = matriz=[[linha_permuta,n]]
            pivo = matriz[n][n]
        
        for linha in range(n+1, size, 1):
            lower[linha][n] = (matriz[linha][n]/pivo) * -1
        matriz = np.dot(lower, matriz)
        vetor_w = np.dot(lower, vetor_w)
    return matriz, vetor_w

def backsubstitution (matriz_a, vetor_y):
    size = len(matriz_a)
    parametros = size * [0]
    i = size - 1 # size - 1 = indice do ultimo elemento da lista
    while i >= 0:
        if i == size - 1: 
            parametros[i] = vetor_y[i]/matriz_a[i][i]
        else:
            j = size - 1
            x=0
            x = vetor_y[i]
            while j > i:
                x -= ( matriz_a[i][j] * parametros[j])
                j-=1
                parametros[i] = x / matriz_a[i][i]
        i-=1
    return parametros

def classificador (entradas, dict_parametros):
    saida_calculada = 999
    saida = entradas[3] * - 1
    entradas = entradas[0:3]
    modulo = 0 
    for key, value in dict_parametros.items():
        
        if len(value) == 4:
            x = np.dot(entradas.transpose(), value[0:3])
            x += value[3]       
        else:
            x = np.dot(entradas.transpose(), value)
        
        modulo = abs(x - saida) 
        
        if saida_calculada > modulo:
            res = key 
            saida_calculada = modulo
    return res

def classificador_2 (entradas, parametros):
    # um classificador pra testes (ambos tao dando a mesma saida)
    saida = entradas[3] * - 1
    entradas = entradas[0:3]
    saidas_calculadas = []
    flores_calculadas = []
    for key, value in parametros.items():
        x = 0
        for i in range(3):
            x += value[i] * entradas [i]
        if len(value) == 4: # se houver termo ind 
            x+= value[3] # soma o termo ind 
        saidas_calculadas.append(abs(x-saida))
        flores_calculadas.append(key)
        
    flor_calculada = flores_calculadas[saidas_calculadas.index(min(saidas_calculadas))]
    return flor_calculada
            

raw_data = pd.read_csv("dados_01.csv")

# FORMATAÇÃO DOS DADOS
raw_data = raw_data.to_numpy()
data = np.delete(raw_data, np.s_[0:2], axis=1)
classe = data[:,4]
data = np.delete(data, np.s_[4], axis=1)
coluna_ti = np.array([1]*15)

# MÍNIMOS QUADRADOS 

"""ÍRIS SETOSA """
iris_setosa = data[0:15] # selecionando os dados
iris_setosa_y = iris_setosa[:,3]         # escolhendo um parametro para ser
iris_setosa_y= np.dot(-1,iris_setosa_y)  # funcao dos outros
iris_setosa_a = np.delete(iris_setosa, np.s_[3], axis=1) # matriz A

# SEM TERMO INDEPENDENTE

iris_setosa_a_transp = iris_setosa_a.transpose() # matriz A transposta
iris_setosa_r= np.dot(iris_setosa_a_transp,iris_setosa_a) # multiplicacao de A transposta por A 
iris_setosa_r = np.round(iris_setosa_r.astype(np.double),2) # arredondando o resultado para duas casas 

iris_setosa_w = np.dot(iris_setosa_a_transp, iris_setosa_y) # multiplicacao A transposta por y
iris_setosa_w = np.round(iris_setosa_w.astype(np.double),2) # arrededondando de novo

iris_setosa_triang, iris_setosa_w = plu(iris_setosa_r, iris_setosa_w) # plu aplicada 
iris_setosa_triang = np.round(iris_setosa_triang.astype(np.double),2)

iris_setosa_parametros = backsubstitution(iris_setosa_triang, iris_setosa_w) # backsubs aplicada 

# COM TERMO INDEPENDENTE
iris_setosa_a_ti = np.hstack((iris_setosa_a, np.atleast_2d(coluna_ti).T))# adicionando a coluna de uns à matriz A
 
iris_setosa_a_ti_transp = iris_setosa_a_ti.transpose() 

iris_setosa_ti_r = np.dot(iris_setosa_a_ti_transp, iris_setosa_a_ti)
iris_setosa_ti_r = np.round(iris_setosa_ti_r.astype(np.double),2)

iris_setosa_ti_w = np.dot(iris_setosa_a_ti_transp, iris_setosa_y)
iris_setosa_ti_w = np.round(iris_setosa_ti_w.astype(np.double),2)

iris_setosa_ti_triang, iris_setosa_ti_w = plu(iris_setosa_ti_r,iris_setosa_ti_w) # plu aplicada 
iris_setosa_ti_triang = np.round(iris_setosa_ti_triang.astype(np.double),2)

iris_setosa_ti_parametros = backsubstitution(iris_setosa_ti_triang, iris_setosa_ti_w)

"""Iris-versicolor"""
iris_versicolor = data[15:30] 
iris_versicolor_y = iris_versicolor[:,3]         
iris_versicolor_y= np.dot(-1,iris_versicolor_y)  
iris_versicolor_a = np.delete(iris_versicolor, np.s_[3], axis=1) 

# SEM TERMO INDEPENDENTE

iris_versicolor_a_transp = iris_versicolor_a.transpose()
iris_versicolor_r= np.dot(iris_versicolor_a_transp,iris_versicolor_a) 
iris_versicolor_r = np.round(iris_versicolor_r.astype(np.double),2) 

iris_versicolor_w = np.dot(iris_versicolor_a_transp, iris_versicolor_y) 
iris_versicolor_w = np.round(iris_versicolor_w.astype(np.double),2) 


iris_versicolor_triang, iris_versicolor_w = plu(iris_versicolor_r,iris_versicolor_w) # plu aplicada 
iris_versicolor_triang = np.round(iris_versicolor_triang.astype(np.double),2)

iris_versicolor_parametros = backsubstitution(iris_versicolor_triang, iris_versicolor_w)


# COM TERMO INDEPENDENTE
iris_versicolor_a_ti = np.hstack((iris_versicolor_a, np.atleast_2d(coluna_ti).T))
 
iris_versicolor_a_ti_transp = iris_versicolor_a_ti.transpose() 

iris_versicolor_ti_r = np.dot(iris_versicolor_a_ti_transp, iris_versicolor_a_ti)
iris_versicolor_ti_r = np.round(iris_versicolor_ti_r.astype(np.double),2)

iris_versicolor_ti_w = np.dot(iris_versicolor_a_ti_transp, iris_versicolor_y)
iris_versicolor_ti_w = np.round(iris_versicolor_ti_w.astype(np.double),2)

iris_versicolor_ti_triang, iris_versicolor_ti_w = plu(iris_versicolor_ti_r,iris_versicolor_ti_w)
iris_versicolor_ti_triang = np.round(iris_versicolor_ti_triang.astype(np.double),2)

iris_versicolor_ti_parametros = backsubstitution(iris_versicolor_ti_triang, iris_versicolor_ti_w)

"""Iris-virginica"""
iris_virginica = data[30:45]
iris_virginica_y = iris_virginica[:,3]         
iris_virginica_y= np.dot(-1,iris_virginica_y) 
iris_virginica_a = np.delete(iris_virginica, np.s_[3], axis=1) 

# SEM TERMO INDEPENDENTE
iris_virginica_a_transp = iris_virginica_a.transpose() 
iris_virginica_r= np.dot(iris_virginica_a_transp,iris_virginica_a)
iris_virginica_r = np.round(iris_virginica_r.astype(np.double),2)

iris_virginica_w = np.dot(iris_virginica_a_transp, iris_virginica_y) 
iris_virginica_w = np.round(iris_virginica_w.astype(np.double),2) 

iris_virginica_triang, iris_virginica_w = plu(iris_virginica_r,iris_virginica_w) 
iris_virginica_triang = np.round(iris_virginica_triang.astype(np.double),2)

iris_virginica_parametros = backsubstitution(iris_virginica_triang, iris_virginica_w) 


# COM TERMO INDEPENDENTE
iris_virginica_a_ti = np.hstack((iris_virginica_a, np.atleast_2d(coluna_ti).T))
 
iris_virginica_a_ti_transp = iris_virginica_a_ti.transpose() 

iris_virginica_ti_r = np.dot(iris_virginica_a_ti_transp, iris_virginica_a_ti)
iris_virginica_ti_r = np.round(iris_virginica_ti_r.astype(np.double),2)

iris_virginica_ti_w = np.dot(iris_virginica_a_ti_transp, iris_setosa_y)
iris_virginica_ti_w = np.round(iris_virginica_ti_w.astype(np.double),2)

iris_virginica_ti_triang, iris_virginica_ti_w = plu(iris_virginica_ti_r,iris_virginica_ti_w) 
iris_virginica_ti_triang = np.round(iris_virginica_ti_triang.astype(np.double),2)

iris_virginica_ti_parametros = backsubstitution(iris_virginica_ti_triang, iris_virginica_ti_w)

# QUESTÃO 5 

dict_parametros = {
    "Iris-setosa": iris_setosa_parametros,
    "Iris-setosa-ti": iris_setosa_ti_parametros,
    "Iris-versicolor": iris_versicolor_parametros,
    "Iris-versicolor-ti": iris_versicolor_ti_parametros,
    "Iris-virginica": iris_virginica_parametros,
    "Iris-viriginica-ti": iris_virginica_ti_parametros
    }





# calculando a acurácia do classificador
k=0
acertos = 0
for d in data:
    saida_calculada = classificador(d, dict_parametros)
    
    # as proximas linhas sao pra remover o '-ti' das saidas com ti
    saida_calculada_list = list(saida_calculada)
    count = 0
    for char in saida_calculada_list:
        if char == '-':
            count += 1
    if count == 2:
        for i in range(3):
            saida_calculada_list.pop()
    saida_calculada = ''.join(saida_calculada_list)
    if saida_calculada == classe[k]:
        acertos += 1
    k += 1
print( 'Acurácia de ' + str((acertos/45) * 100) + '%')



