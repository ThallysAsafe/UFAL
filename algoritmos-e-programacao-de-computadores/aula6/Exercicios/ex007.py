'''7. Faça um programa que tenha duas funções, uma para calcular a média e outra para calcular a variância de um conjunto de números.'''
def calculandomedia(lista):
    soma = 0
    for numeros in lista:
        soma += numeros
    media = soma / len(lista)   
    return media 

def desvios_padrao(lista, media):
    desvio = 0
    for numeros in lista:
        desvio += (numeros - media)**2
    variancia = desvio / len(lista)
    return variancia

lista = [0,1,2,3,4,5,6,7,8,9,10]
media = calculandomedia(lista)
print(media)
print(desvios_padrao(lista, media))

 