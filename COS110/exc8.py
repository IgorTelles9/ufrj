"""
    Exercício 8 dos laboratórios de Alg. Prog
"""

def eh_sub_seq(vetor_seq, vetor, i=0,j=0):
    if vetor_seq[i] == vetor[j]:
        """
        o elemento i em vetor_seq é igual ao elemento
        j em vetor 
        """
        if i == len(vetor_seq) - 1:
            # não há mais elementos em vetor_seq 
            # e o ultimo elemento estava em vetor
            return True 

        elif i+1 < len(vetor_seq) and j+1 < len(vetor):
            # ainda há elementos e vetor_seq e vetor
            i+=1
            j+=1
            return eh_sub_seq(vetor_seq, vetor, i=i, j=j)
            # pula pra próxima posicao de vetor_seq e vetor

        
    else:
        """
        o elemento i em vetor_seq é diferente 
        do elemento j em vetor
        """
        if i < len(vetor_seq) and j+1 < len(vetor):
            # se i ainda está dentro do vetor_seq
            # e j+1 está dentro de j
            j+=1
            return eh_sub_seq(vetor_seq, vetor, i=i, j=j)
            #pula pra próxima posicao de vetor
        
        else:
            print("FALSE: ", i, j)
            return False

v1 = eval(input())
v2 = eval(input())
print(eh_sub_seq(v1, v2))




