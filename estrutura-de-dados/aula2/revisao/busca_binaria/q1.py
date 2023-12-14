# Busca Binária Recursiva em uma Lista Ordenada:
# Implemente uma função recursiva para realizar a busca binária em uma lista ordenada, retornando o índice do elemento se presente, ou -1 se ausente.

def busca_bin(lista, n):
    meio = len(lista)//2
    if len(lista) == 1 and lista[meio] != n:
        return False
    elif lista[meio] == n:
        return True
    elif lista[meio] < n:
        return busca_bin(lista[meio+1:], n)
    elif lista[meio] > n:
        return busca_bin(lista[:meio], n)
lista = [1,2,3,4,5,6]
n = -2
print(busca_bin(lista, n))