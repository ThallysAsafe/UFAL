from combinacao import combinacao
def divisao(lista):
    if len(lista) == 1:
        return lista
    else:
        return combinacao(divisao(lista[0:len(lista)//2]), divisao(lista[len(lista)//2:]))
lista = [9,8,7,6,5,4,3,2,1]
print(divisao(lista))