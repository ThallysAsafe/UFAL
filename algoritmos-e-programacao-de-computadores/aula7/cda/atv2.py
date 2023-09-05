m = 4
n = 4
A= [0]*m
for i in range(m):
    A[i] = [0]*n
for i in range(m):
    A[i][i] = 1
    print(A[i], end=" ")
    print()