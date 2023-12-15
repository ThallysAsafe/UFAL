# Maior Elemento Menor que um Valor na Lista Ordenada:
# Implemente uma função que encontre o maior elemento na lista ordenada que é menor que um valor dado, utilizando busca binária.

def maior_valor(lista, n):
    if len(lista) == 1:
        return lista[0]
    meio = len(lista)//2
    if lista[meio] > n:
        return maior_valor(lista[:meio], n)
    elif lista[meio] < n:
        return maior_valor(lista[meio:], n)
n = 11
lista = [1,2,3,4,5,6,7,9,10]
print(maior_valor(lista, n))