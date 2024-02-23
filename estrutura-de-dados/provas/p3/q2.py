# 2. Mostre as etapas de funcionamento do QuickSort e Mergesort (apresentando inclusive as chamadas
# recursivas) para ordenar a sequência de números:
# 6 2 9 12 5 1 3
lista = [6, 2, 9, 12, 5, 1, 3]
lista1 = [6, 2, 9, 12, 5, 1, 3]
def merge_sort(lista):
    if len(lista) <= 1:
        print(f"Lista de tamanho um, retornando lista: {lista}")
        return lista

    meio = len(lista) // 2
    
    lista1 = merge_sort(lista[:meio])
    lista2 = merge_sort(lista[meio:])
    print(f"Dividindo, em duas listas: {lista1,lista2}")
    i, j = 0, 0
    lista3 = []

    while j < len(lista2) and i < len(lista1):
        print(f"Comparação:{lista1[i], lista2[j]}")
        if lista1[i] > lista2[j]:
            print(f"Menor: {lista2[j]}")
            lista3.append(lista2[j])
            j += 1
        else:
            print(f"Menor: {lista1[i]}")
            lista3.append(lista1[i])
            i += 1

    while i < len(lista1):
        print(f"Restante de lista1: {lista1[i]}")
        lista3.append(lista1[i])
        i += 1

    while j < len(lista2):
        print(f"Restante de lista2: {lista2[j]}")
        lista3.append(lista2[j])
        j += 1

    return lista3

def quick_sort(lista):
    print(f"função quick_sort, para a lista: {lista}")
    if len(lista) <= 1:
        print(f"Lista de tamanho um, retornando lista: {lista}")
        return lista

    pivo = lista[len(lista)//2]
    i, j = 0, len(lista)-1

    while i <= j:
        
        while lista[i] < pivo:
            print(f"Comparando lado esquerdo: {lista[i]} com pivo: {pivo}")
            i += 1
        while lista[j] > pivo:
            print(f"Comparando lado direito: {lista[i]} com pivo: {pivo}")
            j -= 1

        if i <= j:
            print(f"Esses dois valores {lista[i], lista[j]} trocarão de lugar")
            print(f"Lista antes da troca de posição: {lista}")
            lista[i], lista[j] = lista[j], lista[i]
            print(f"Lista depois da troca de posição: {lista}")
            i += 1
            j -= 1
    print(f"Chamando a função quick_sort, para cada lista: {lista[:i],lista[i:]}")
    return quick_sort(lista[:i]) + quick_sort(lista[i:])

print(f"Merge_sort: {merge_sort(lista)}")
print(f"Quick_sort: {quick_sort(lista1)}")