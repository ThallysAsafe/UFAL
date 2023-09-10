# Identificar Matriz Diagonal
# Crie uma função que verifica se uma matriz é diagonal.
A = [[1,0,0],
     [0,1,0],
     [0,0,1]]
def matdiagonal(A):
    m = len(A)
    n = len(A[0])
    i = 0
    condição = False
    while i < m:
        j = 0
        while j < n:
            if (A[i][j] == 0) and i != j:
                print(i)
                print(j)
                print('--')
                condição = True
            elif (A[i][j] != 0) and i != j:
                print('AAAA')
                condição = False
                return condição
            j += 1
        i += 1
            
    return condição
print(matdiagonal(A))