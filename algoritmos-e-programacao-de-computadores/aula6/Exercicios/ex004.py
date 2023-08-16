'''4. Faça um algoritmo que copie o conteúdo de uma lista para outra, eliminando valores repetidos. Implemente funções para isso'''
lista1 = [2,2,1]
lista2 = []
def copiador(lista1):
    for numero in lista1:
        if numero not in lista2:
            lista2.append(numero)
    return lista2
print(copiador(lista1))