# 1. Implemente e teste os algoritmos de ordenação QuickSort e MergeSort para ordenar um vetor de
# registros que representa uma tabela de campeonato de futebol. O registro é Time, com os campos nome
# e pontuação. A ordenação deve feita pelo campo pontuação.

Campeonato1 = [{"Time": 'Cruzeiro',"Pontuacao": 23},{"Time": 'Palmeiras',"Pontuacao": 54},{"Time": 'Flamengo',"Pontuacao": 56},{"Time": 'Bota-fogo',"Pontuacao": 45},{"Time": 'Fluminense',"Pontuacao": 38}]

Campeonato2 = [{"Time": 'Cruzeiro',"Pontuacao": 23},{"Time": 'Palmeiras',"Pontuacao": 54},{"Time": 'Flamengo',"Pontuacao": 56},{"Time": 'Bota-fogo',"Pontuacao": 45},{"Time": 'Fluminense',"Pontuacao": 38}]
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    middle = len(lista) // 2
    lista1 = merge_sort(lista[:middle])
    lista2 = merge_sort(lista[middle:])

    i, j = 0, 0
    lista3 = []

    while j < len(lista2) and i < len(lista1):
        if lista1[i]["Pontuacao"] < lista2[j]["Pontuacao"]:
            lista3.append(lista2[j])
            j += 1
        else:
            lista3.append(lista1[i])
            i += 1

    if i < len(lista1):
        lista3 += lista1[i:]
    elif j < len(lista2):
        lista3 += lista2[j:]

    return lista3

print(f"Merge_sort: {merge_sort(Campeonato1)}")


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista)//2]
    i, j = 0, len(lista)-1

    while i <= j:
        while lista[i]["Pontuacao"] > pivot["Pontuacao"]:
            i += 1
        while lista[j]["Pontuacao"] < pivot["Pontuacao"]:
            j -= 1

        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    return quick_sort(lista[:i]) + quick_sort(lista[i:])

print(f"Quick_sort: {quick_sort(Campeonato2)}")