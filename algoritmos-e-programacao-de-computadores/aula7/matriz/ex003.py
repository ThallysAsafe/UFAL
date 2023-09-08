# 3. Implemente uma função que recebe uma matriz e um inteiro e verifica se o inteiro existe na matriz

def busca(A,valor):
    m = len(A)
    n = len(A[0])
    i = 0
    j = 0
    while i < m:
        while j < n and A[i][j]!=valor:
            j += 1
        if j < n:
            return True
        i += 1
        j = 0
    return False

A = [[0,-1,2],
     [3,2,1],
     [5,3,2],
     [9,2,4]]
valor = 1
print(busca(A,valor))