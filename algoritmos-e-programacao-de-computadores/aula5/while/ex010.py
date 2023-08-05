'''10. Algoritmo que recebe uma palavra e imprime o reverso dessa palavra'''
palavras = (input('Digite uma palvra: '))
reverso = []
i = len(palavras)
while i != 0:
    i -= 1
    reverso.append(palavras[i])
for i in reverso:
    print(i, end='')
    
'''separador = ''
palavra = separador.join(reverso)
print(palavra)
'''