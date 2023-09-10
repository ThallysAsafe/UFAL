# 1. Implemente uma função que recebe uma matriz e verifica se ela é simétrica
m = 3
n = 3

A = [[2,2,2],
     [2,1,3],
     [2,3,1]]
def matriz(m,n,A):
    resultado = 0 
    i = 0
    while i < m:
        j = 0
        while j < n:
            if A[i][j] != A[j][i]:
                resultado += 1
            j += 1
        i += 1
    if resultado <= 1:
        return True
    return False
print(matriz(m,n,A))