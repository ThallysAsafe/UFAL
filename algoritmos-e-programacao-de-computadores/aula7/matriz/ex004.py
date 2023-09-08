# 4. Um quadrado mágico é aquele dividido em linhas e colunas no qual a soma das linhas, das colunas e diagonais é a mesma. Ex:
# 8  3  4
# 1  5  9
# 6  7  2
# Implemente uma função que recebe uma matriz e verifica se é um quadrado mágico

matriz =  [[4 , 9 , 2],
            [3 , 5 , 7],
            [8,  1,  6]]
def verificador(matriz):
    m = len(matriz)
    n = len(matriz[0])
    i = 0
    soma = 0
    while i < m:
        j = 0
        while j < n:
            soma += matriz[i][j]
            j += 1
        i += 1
    i = 0
    while i < n:
        j = 0
        while j < m:
            soma += matriz[i][j]
            j += 1
        i += 1
    verificação = soma / (m + n)
    soma = 0
    for i in range(m):
        soma += matriz[0][i]
    if soma == verificação:
        return True
    return False

print(verificador(matriz))



