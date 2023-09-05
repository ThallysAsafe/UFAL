m = 2
n = 2
def inicializarMatriz(m,n):
    matrizA = [0]*m
    for i in range(m):
        matrizA[i] = [0]*n
    return matrizA
def soma(m,n,matrizA,matrizB):
    matrizC = inicializarMatriz(m,n)
    for i in range(m):
        for j in range(n):
            matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
    return matrizC


def imprimir(m,n,matrizA):
    matrizA = soma(m,n,matrizA,matrizB)
    for i in range(m):
        print(matrizA[i])
        print()
matrizA = inicializarMatriz(m,n)
matrizB = inicializarMatriz(m,n)
for i in range(m):
    for j in range(n):
        matrizA[i][j] = int(input(f'Digite um valor para posição [{i},{j}]: ')) 
        matrizB[i][j] = int(input(f'Digite um valor para posição [{i},{j}]: '))
soma(m,n,matrizA,matrizB)
print(imprimir(m,n,matrizA))