""" 
    Exercício 7 dos laboratórios de Alg. Prog
    Esse programa recebe dois vetores e verifica se há um indice i tal que
    A[i] = B[i]
    Laboratório Alg. Prog. ECI / Set. 2020 
"""  

def verifica_igual(vetor_um, vetor_dois, i=0):
    if vetor_um[i] == vetor_dois[i]:
        return True
    else:
        tam_menor = min( len(vetor_um), len(vetor_dois) ) - 1
        if i >= tam_menor:
            return False

        else:
            return verifica_igual(vetor_um, vetor_dois, i+1)


v1 = eval(input())
v2 = eval(input())
resp = verifica_igual(v1, v2)
print(resp)