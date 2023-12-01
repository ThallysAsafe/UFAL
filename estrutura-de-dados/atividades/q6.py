# 6. Algoritmo que recebe duas listas e imprime a intersecção das duas listas
lista1 = [1,3,2,2,7]
lista2 = [2,1,3]
lista3 = []

for numero in lista1: # O(N)
    cont = 0
    cond = True
    for i in range(0,len(lista2)): # O(M)
        if numero == lista2[i]:
            cont = 1
            for j in range(0,len(lista3)): # O(P)
                if lista3[j] == numero:
                    cond = False
                    break
            break
    if (cont != 0) and cond == True:
        lista3.append(numero)
print(lista3)

# O(N) x O(M) x O(P) ----> O(N x M x P)