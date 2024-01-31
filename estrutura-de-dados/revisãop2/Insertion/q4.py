# 04)Implemente o Insertion Sort de forma recursiva.
lista = [9,8,7,6,5,4,3,2,1]
def Insertion_Recursivo(lista,i = 0, j = 0):
    if i > len(lista):
        return
    

def selection_recursivo(lista, i = 0, j = 1, menor = 0):
    print(f"j={j}")
    print(f"i={i}")
    if j == (i + 1):
        print(0)
        menor = i
    elif i == len(lista)-1:
        print(5)
        return lista
    if j == len(lista)-1 and lista[menor]>lista[j]:
        print(1)
        
        j = 0
        lista[i], lista[menor] = lista[menor], lista[i]
        i += 1
        print(lista)
        return selection_recursivo(lista, i, j, menor)
    if lista[menor] > lista[j]:
        print(2)
        menor = j
        
        j += 1
        return selection_recursivo(lista, i, j, menor)
    if lista[menor] < lista[j]:
        i += 1
        print(3)
        return selection_recursivo(lista, i, j, menor)

print(selection_recursivo(lista))