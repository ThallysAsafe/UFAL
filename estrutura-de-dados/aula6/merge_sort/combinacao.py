

def combinacao(lista1, lista2):
    j = 0
    i = 0
    lista3 = []
    while j < len(lista2) and i < len(lista1):
        if lista1[i] > lista2[j]:
            lista3.append(lista2[j])
            j += 1
        else:   
            lista3.append(lista1[i])
            i += 1
    if i < len(lista1):
        lista3 = lista3 + lista1[i:]
    elif j < len(lista2):
        lista3 = lista3 + lista2[j:]
    return lista3


def combinacao_for(lista1, lista2):
    m = len(lista1)
    n = len(lista2)
    i = 0
    j = 0
    lista = []
    for c in range(m+n):
        if lista1[i] < lista2[j]:
            lista.append(lista1[i])
            i += 1
        elif lista1[i] < lista2[j]:
            lista.append(lista2[j])
            j += 1
