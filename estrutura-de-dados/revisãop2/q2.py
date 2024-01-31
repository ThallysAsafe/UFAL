# 02) Implemente uma função que recebe uma lista de números e retorna o menor
# número presente na lista.

lista = [9,8,7,6,5,4,3,2,1,0]
def menoritem(lista):
    menor = lista[0]
    for i in range(1,len(lista)):
        if lista[i] < lista[menor]:
            menor = i
    return lista[menor]

print(menoritem(lista))
