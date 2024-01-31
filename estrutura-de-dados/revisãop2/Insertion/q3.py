# 03)Crie uma função que recebe uma lista e utiliza o algoritmo de Insertion Sort para encontrar o segundo menor elemento.
lista = [9,8,7,6,5,4,3,2,1,0]
def Insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j]<lista[j-1]:
            lista[j],lista[j-1]=lista[j-1],lista[j]
            j -= 1
    return lista[1]
print(Insertion_sort(lista))