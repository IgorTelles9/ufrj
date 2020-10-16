"""
    Exercício 14 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def arctg(x,n): 
    resultado = 0
    sinal_checker = 0

    for i in range(1,2*n):
        if (i % 2 != 0 or i == 1):
            if (sinal_checker % 2 == 0):
                resultado += (x**(i))/(i)
            else:
                resultado -= (x**(i))/(i)
            sinal_checker +=1
    return resultado

x = float(input())
n = int(input())

print(arctg(x,n))

