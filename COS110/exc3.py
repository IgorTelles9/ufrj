"""
    Exercício 3 dos laboratórios de Alg. Prog
"""

vetor_1 = eval(input())
vetor_2 = eval(input())

tamanho = len(vetor_1)
resultado = 0

for i in range(tamanho):
    resultado_atual = vetor_1[i] * vetor_2[i]
    resultado += resultado_atual

print(resultado)