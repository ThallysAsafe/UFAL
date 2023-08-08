'''10. Algoritmo que recebe uma palavra e imprime o reverso dessa palavra'''
palavras = (input('Digite uma palvra: '))
reverso = ''
i = len(palavras) - 1
while i >= 0:
    reverso += palavras[i]
    i -= 1
print(reverso)
    
'''separador = ''
palavra = separador.join(reverso)
print(palavra)
'''