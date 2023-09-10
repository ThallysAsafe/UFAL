# Média dos Elementos de uma Matriz
# Calcule a média dos elementos de uma matriz.
A = [[2,2,2],
     [2,2,2],
     [2,2,2]]

def mediaMatriz(A):
    m = len(A)
    n = len(A[0])
    soma = 0
    for i in range(m):
        for j in range(n):
            soma += A[i][j]
    media = soma / (m*n)
    return media

print(mediaMatriz(A))