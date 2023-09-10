# Transposição de Matriz
# Escreva um programa que calcula a matriz transposta de uma matriz dada.

m = 2
n = 3

A= [0]*m
for i in range(m):
    A[i] = [i]*n

for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
print("_________")
B = [0]*n
for i in range(n):
    B[i] = [0]*m
for i in range(m):
    for j in range(n):
        B[j][i] = A[i][j]
for i in range(n):
    for j in range(m):
        print(B[i][j], end=" ")
    print()