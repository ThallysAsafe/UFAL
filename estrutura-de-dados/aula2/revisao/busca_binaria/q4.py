# Rotação em Lista Ordenada com Busca Binária:
# Desenvolva uma função que rotaciona uma lista ordenada em torno de um ponto desconhecido e, em seguida, utilize a busca binária para encontrar um elemento na lista rotacionada.

def rotate_list(lista, rotation_point):
    n = len(lista)
    if rotation_point > n:
        rotation_point %= n
    
    # Divida a lista em duas partes e troque a ordem
    lista[:rotation_point], lista[rotation_point:] = lista[rotation_point:], lista[:rotation_point]

def busca_binaria_rotacionada(lista, valor, ini=0, fim=None):

    if fim is None:
        fim = len(lista) -1
    
    meio = (fim + ini) // 2

    if lista[meio] == valor:
        return valor
    if lista[ini] <= lista[meio]:
        if lista[ini] <= valor <= lista[meio]:
            return busca_binaria_rotacionada(lista, valor, ini, meio - 1)
        else:
            return busca_binaria_rotacionada(lista, valor, meio + 1, fim)
    else:
        if lista[meio] <= valor <= lista[fim]:
            return busca_binaria_rotacionada(lista, valor, meio + 1, fim)
        else:
            return busca_binaria_rotacionada(lista, valor, ini, meio - 1)

lista = [3, 4, 5, 6, 7, 8, 1, 2]
valor = 3
rotation_point = 6

# Rotação da lista
rotate_list(lista, rotation_point)

# Elemento a ser buscado
target_element = 5

# Busca binária na lista rotacionada
result = busca_binaria_rotacionada(lista, valor, 0, len(lista) - 1)

# Saída
print(f"A lista rotacionada é: {lista}")
print(f"O elemento {target_element} está na posição {result} na lista rotacionada.")
