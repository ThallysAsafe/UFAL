'''2. Escreva um programa que possui uma função que recebe uma lista e um valor e verifica se existe o valor na lista'''
lista = [2,5,67,8,1,21,63,15]
def buscador(lista, valor):
    for numeros in lista:
        if numeros == valor:
            resultado = 'Sim, existe esse número na lista.'
            return resultado
        else:
            resultado = 'Não, não existe esse número na lista.'    
    return resultado
valor = float(input('Digite um número, para ver se tem na lista: '))
print(buscador(lista,valor))

        