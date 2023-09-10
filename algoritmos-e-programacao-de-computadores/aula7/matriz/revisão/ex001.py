# Soma de Matrizes
# Escreva um programa que recebe duas matrizes como entrada e calcula a soma delas.

A = [[1,1,1],
     [1,1,1],
     [1,1,1]]
B = [[2,2,2],
     [2,2,2],
     [2,2,2]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

for i in range(3):
    for j in range(3):
        print(C[i][j], end=' ')
    print()
