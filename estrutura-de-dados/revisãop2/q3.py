# 03) Implemente um algoritmo de ordenação seguindo a lógica do Selection Sort, sua
# implementação deve retornar, além da lista ordenada, uma variável contadora que
# acompanha o número de comparações feitas durante o processo de ordenação.

lista = [9,8,7,6,5,4,3,2,1,0]
def selection_sort(lista):
    count = 0
    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1, len(lista)):
            count += 1
            if lista[menor] > lista[j]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista, count
print(selection_sort(lista))