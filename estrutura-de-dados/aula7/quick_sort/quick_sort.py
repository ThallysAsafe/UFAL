# 1- escolha um pivô
lista = [3,5,8,4,2,1,9,0] 
def quick(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista)//2]
    i, j = 0, len(lista)-1

    while i < j:
        while lista[i] < pivot:
            i += 1
        while lista[j] > pivot:
            j -= 1

        if i < j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    print(i,lista[:i],lista[i:])
    lista1 = quick(lista[:i])
    lista2 = quick(lista[i:])
    return lista1 + lista2

print(quick(lista))

    # while i != j:
    #     print(lista[i],lista[j],lista[pivo],lista)
    #     if lista[j]>lista[pivo]:
    #             j -= 1
    #     elif lista[i]<lista[pivo]:
    #             i += 1
    #     else:
    #         lista[i], lista[j] = lista[j], lista[i]  
    # return lista, 
