from random import randint
lista = [1,2,3,4,5,6,7,8,9,10]
x = 11
def busca_binaria(x, lista):
    if len(lista) == 0:
        return False
    media = len(lista)//2
    if lista[media] == x:
        return True
    elif lista[media] > x:
        return busca_binaria(x,lista[:media])
    elif lista[media] < x:
        return busca_binaria(x,lista[media+1:])
print(busca_binaria(x,lista))
