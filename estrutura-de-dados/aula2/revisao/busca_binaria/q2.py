# Inserção em Lista Ordenada com Busca Binária:
# Crie uma função que insira um elemento em uma lista ordenada mantendo a ordem, usando a busca binária para encontrar a posição correta.

def busca_binaria2(elemento, lista, i=0, fim= None):
    if fim is None:
        fim = len(lista)-1
    meio = (fim+i)//2
    print(i,meio,fim)
    if i > fim:
        lista.insert(i, elemento)  
        return lista 
    elif lista[meio] > elemento:
        return busca_binaria2(elemento, lista, i, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria2(elemento, lista, meio+1, fim)
    else:
        lista.insert(meio, elemento)
        return lista

elemento = 2
lista = [0,1,3,4]
print(busca_binaria2(elemento, lista))