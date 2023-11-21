# 5. Copiar uma lista de inteiros, retirando elementos repetidos
lista_original = [1,2,3,2,1]
lista_copia_sem_repeticoes = []
for numero in lista_original: # O(N)
    cont = 0
    for i in range(0,len(lista_original)): # O(M)
        if numero == lista_original[i]:
            cont += 1
    if cont < 2:
        lista_copia_sem_repeticoes.append(numero)
print(lista_copia_sem_repeticoes)
# O(N) x O(M) --> O(N x M)