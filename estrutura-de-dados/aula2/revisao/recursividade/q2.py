# Soma Recursiva de Elementos em uma Lista:
# Crie uma função recursiva para calcular a soma de todos os elementos em uma lista.

def soma_lista(lista, i):
    if i > len(lista)-1:
        return 0
    else:
        return lista[i] + soma_lista(lista, i+1)
    
lista = [1,2,3,4,5]
i = 0
print(soma_lista(lista, i))