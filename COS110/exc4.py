""" 
    Este programa multiplica matrizes por matrizes, matrizes por vetores e vetores por vetores.
    Exercício 4 dos laboratórios de Algoritmos e Programação - ECI. 
    Rio, setembro de 2020.

"""

matriz_1 = eval(input())
matriz_2 = eval(input())

#matriz_1 = [ [1],[2] ] 
#matriz_2 = [1,2] 

#print(type(matriz_1[0]))
#print(type(matriz_2[0]))

soma = 0
resultado = []

if type(matriz_1[0])==list and type(matriz_2[0])==list:
  # multiplicação de matriz por matriz
  linhas_1 = len(matriz_1)
  linhas_2 = len(matriz_2) 
  colunas_2 = len(matriz_2[0])
  resultado.append([])
  resultado.append([])

  for i in range(linhas_1):
    for j in range(colunas_2):
      for k in range(linhas_2):
          soma += matriz_1[i][k] *  matriz_2[k][j]
      resultado[i].append(soma)
      soma = 0 

elif type(matriz_1[0])==int and type(matriz_2[0])==list: 
  # multiplicação de vetor por matriz
  linhas_2 = len(matriz_2) 
  colunas_2 = len(matriz_2[0])
  
  for j in range(colunas_2):
    for k in range(linhas_2):
      soma += matriz_1[k] *  matriz_2[k][j]  
    resultado.append(soma)
    soma = 0 
    
elif type(matriz_1[0])==list and type(matriz_2[0])==int:
  # multiplicação de matriz por vetor
  
  linhas_1 = len(matriz_1) # [1],[2]
  colunas_1 = len(matriz_1[0]) #[1,2]
  colunas_2 = len(matriz_2)
  resultado.append([])
  resultado.append([])

  for i in range(linhas_1):
    for j in range(colunas_1):
      for k in range(colunas_2):
        soma += matriz_1[i][j] *  matriz_2[k]   
        resultado[i].append(soma)
        soma = 0 

else:
  # multiplicação de vetor por vetor
  tamanho = len(matriz_1)

  for i in range(tamanho):
    soma = matriz_1[i] * matriz_2[i]
    resultado.append(soma)
      
print(resultado)

    