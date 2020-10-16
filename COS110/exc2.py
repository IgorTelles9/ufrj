""" 
    Dado um número n, este programa mostra todos os primos até n.
    Exercício 2 dos laboratórios de Algoritmos e Programação - ECI. 
    Rio, setembro de 2020.

"""

n = int(input()) #7
primos = []
numero_atual = 1
while (numero_atual <= n): 
    if (numero_atual < 3):
        primos.append(numero_atual)
    else:
        for primo in primos:
            if (primo != 1):
                resto = numero_atual % primo
                if (resto == 0):
                    break;
            if ( (numero_atual // primo ) < primo ):
                primos.append(numero_atual)
                break;
    numero_atual+=1

    
primos = str(primos)    
print(primos)

