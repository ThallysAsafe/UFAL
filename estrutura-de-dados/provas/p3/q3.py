# O método de ordenação por seleção funciona colocando o menor elemento do vetor na primeira
# posição, o segundo menor na segunda posição e assim por diante. Altere o algoritmo para que, a cada
# passo, ele coloque o maior elemento na última posição, o segundo maior na penúltima posição, e assim
# por diante.
lista = [5,4,3,2,1,1,2,7,3,4,5]
def selection_sort(lista):
    
    j = len(lista)-1
    while j > 0:
        i = 0
        maior = i
        while i <= j:
            if lista[maior] < lista[i]:
                maior = i
            i += 1
        lista[j], lista[maior] = lista[maior], lista[j]
        j-=1
    return lista

print(selection_sort(lista))

        
