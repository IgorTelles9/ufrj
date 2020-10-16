"""
    Exercício 17 dos laboratórios de Alg. Prog
    Outubro de 2020
"""

def caminho_diagonal(matriz):
    """ Encontra a saída de um labirinto e retorna o caminho ou
        retorna False se não houver saída
    """

    i_saida = len(matriz) - 1
    j_saida = len(matriz[0]) - 1

 
    caminhos_disponiveis = 2
 
    while caminhos_disponiveis != 0:
        # esse loop serve pra resetar os caminhos do robo
        i =0
        j = 0
        caminhos_passados = []
        pos = ()

        if caminhos_disponiveis != 1:
            # como caminhos_.. = 2, esse if é priorizando na entrada

            while i <= i_saida and j <= j_saida:
                # esse loop começa o labirinto priorizando a direita
                pos = (i,j)
                caminhos_passados.append(pos)

                if j + 1 <= j_saida and matriz[i][j+1] == 0 :  
                    # vai pra direita se possível
                    j += 1
                elif i + 1 <= i_saida and  matriz[i + 1][j] == 0:
                    # vai pra baixo se possível 
                    i += 1
                else:
                    break
        else:
            while i <= i_saida and j <= j_saida:
                # esse loop começa o labirinto priorizando para baixo
                pos = (i, j)
                caminhos_passados.append(pos)

                if i + 1 <= i_saida and  matriz[i + 1][j] == 0:
                    # vai pra baixo se possível
                    i += 1
                elif j + 1 <= j_saida and matriz[i][j+1] == 0 :
                    # vai pra direita se possível  
                    j += 1
                else:
                    break

        caminhos_disponiveis -= 1 # sempre executa após sair dos whiles internos

        if caminhos_passados[-1][:] == (i_saida, j_saida):
            # retorna a lista de caminhos se está no final do labirinto
            return caminhos_passados
    return False
    # se sair do loop externo significa que não há caminho possível

m = eval(input())
print(caminho_diagonal(m))
