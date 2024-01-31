# 04) Implemente um algoritmo de ordenação seguindo a lógica do Insertion Sort, sua
# implementação deve retornar, além da lista ordenada, uma variável contadora que
# acompanha quantas trocas de posição o algoritmo fez na lista durante o processo
# de ordenação.

lista = [9,8,7,6,5,4,3,2,1,0]
def insertion_sort(lista):
    count = 0
    for i in range(1,len(lista)):
        j = i
        if lista[j]>lista[j-1]:
            count += 1
        while j > 0 and lista[j]<lista[j-1]:
            count += 1
            lista[j], lista[j-1] = lista[j-1],lista[j]
            j -= 1

    return lista, count
print(insertion_sort(lista))