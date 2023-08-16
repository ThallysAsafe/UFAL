'''1-Escreva um programa que possui uma função “maior”, que recebe uma lista e devolve o maior elemento na lista'''
lista = [2,6,3,9,1,9]
def maior(lista):
    maior_numero = lista[0]
    for numero in lista:
        if maior_numero < numero:
            maior_numero = numero
    return maior_numero
print(maior(lista))