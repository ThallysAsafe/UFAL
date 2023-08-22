'''4. Faça um algoritmo que copie o conteúdo de uma lista para outra, eliminando valores repetidos. Implemente funções para isso'''
lista1 = [2,2,1,3,16,3,14,11,78,12,11,78,0,0]
lista2 = []
def copiador(lista1):
    lista2.append(lista1[1])
    for numero in lista1:
        resultado = 0
        for num1 in lista2:
            if numero != num1:
                resultado += 1
                if resultado == len(lista2) or len(lista2) == 0:
                    lista2.append(numero)
    return lista2
print(copiador(lista1))