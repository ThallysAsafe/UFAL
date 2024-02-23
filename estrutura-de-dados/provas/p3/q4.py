# 4. Modifique o programa do quick_sort de modo que, se um sub-vetor for pequeno, a ordenação por
# seleção seja usada.
lista = [9,8,7,6,5,4,3,2,1]
def quick_sort(lista):
    if len(lista) == 1:
        return lista
    elif len(lista) <= 3:
        lista = selection_sort(lista)
        return lista
    else:

        pivo = lista[len(lista)//2]
        i = 0
        j =  len(lista)-1
        while i <= j:
            
            while lista[i] < pivo:
                i += 1
            while lista[j] > pivo:
                j -= 1

            if i <= j:
                lista[i], lista[j] = lista[j], lista[i]

                i += 1
                j -= 1

        return quick_sort(lista[:i]) + quick_sort(lista[i:])


def selection_sort(lista):
    
    j = len(lista)-1
    while j > 0:
        i = 0
        maior = i
        while i <= j:
            if lista[maior] < lista[i]:
                maior = i
            i += 1
        lista[j], lista[maior] = lista[maior], lista[j]
        j-=1
    return lista

lista = [5,4,3,2,1,1,2,7,3,4,5]
print(quick_sort(lista))

