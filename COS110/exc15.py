"""
    Esse programa checa se duas entradas são anagramas
    Exercício 15 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def eh_anagrama(palavra_1, palavra_2):
    checkeds = [0]*len(palavra_1)

    if len(palavra_1) != len(palavra_2):
        return False
    equals = 0
    for i in range(len(palavra_1)):
        for j in range(len(palavra_2)):
            if checkeds[j]!=1 and palavra_1[i] == palavra_2[j]:
                equals +=1
                checkeds[j] = 1 
                break
    if equals == len(palavra_1):
        return True
    else:
        return False

palavra_um = input()
palavra_dois = input()

print(eh_anagrama(palavra_um, palavra_dois))