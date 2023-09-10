# Multiplicação de Matriz por Escalar
# Escreva uma função que multiplica uma matriz por um número escalar.
B = [[2,2,2],
     [2,2,2],
     [2,2,2]]
numero = 2
def matrizmultiplic(A,numero):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            A[i][j] = A[i][j]*numero
    for i in range(m):
        for j in range(n):
            print(A[i][j], end=' ')
        print()
matrizmultiplic(B,numero)