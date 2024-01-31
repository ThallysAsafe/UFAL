lista = [1,2,3]

def insertwhile(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j]<lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
    return lista
def insertfor(lista):
    count = 0
    for i in range(1, len(lista)):
        for j in range(i,0,-1):
            count += 1
            if lista[j]>lista[j-1]:
                break
            lista[j], lista[j-1] = lista[j-1], lista[j]
    return lista, count
print(insertfor(lista))