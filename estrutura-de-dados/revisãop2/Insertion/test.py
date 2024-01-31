lista = [9,8,7,6,5,4,3,2,1,0]
def selection_sort(lista, i=0, j=0, index=1):
    if i == len(lista)-1:
        print("1")
        return lista 
    elif index == len(lista):
        print("2")
        if lista[j] < lista[i]:
            lista[j], lista[i] = lista[i], lista[j]
        print(lista)
        return selection_sort(lista, i+1, i+1, i+2)
    elif(lista[j] > lista[index]):
        print("3")
        return selection_sort(lista, i, index, index+1)
    elif(lista[j] < lista[index]):
        print("4", index,i)
        return selection_sort(lista, i, j, index+1)
    
print(selection_sort(lista))