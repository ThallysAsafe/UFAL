# Rotação em Lista Ordenada com Busca Binária:
# Desenvolva uma função que rotaciona uma lista ordenada em torno de um ponto desconhecido e, em seguida, utilize a busca binária para encontrar um elemento na lista rotacionada.

def busca_binaria_rotacionada(lista, valor, ini=0, fim=None):

    if fim is None:
        fim = len(lista) -1
    
    meio = (fim + ini) // 2

    if lista[meio] == valor:
        return valor
    if lista[ini] <= lista[meio]:
        if lista[ini] <= valor <= lista[meio]: