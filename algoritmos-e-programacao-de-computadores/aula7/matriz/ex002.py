# 2. Implemente uma função que recebe uma matriz e um inteiro e faz a multiplicação da matriz pelo inteiro

A = [[2,2,2],
     [2,1,3],
     [1,3,1]]
num = 2
def multiplicamatriz(A,num):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            A[i][j] = A[i][j]*num
    for i in range(m):
        for j in range(n):
            print(A[i][j], end=' ')
        print()

multiplicamatriz(A,num)
