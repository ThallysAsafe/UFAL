m = 4
n = 3

A = [0]*m
print(A)

for i in range(m):
    A[i] = [0]*n

print(A)

A[-1][0] = 1
A[2][2] = 3
A[3][2] = 4
A[1][2] = 2
for i in range(m):
    for j in range(n):
        A[i][j] = j + i
        print(A[i][j], end=" ")
    print()