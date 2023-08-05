'''14. Algoritmo que recebe um conjunto de inteiros e calcula a amplitude do conjunto. A amplitude é dada por 
A = max – min'''
conjunto = []
r = 's'
while r not in 'Nn':
    conjunto.append(int(input('Digite um Numero: ')))
    r = str(input('Quer Continuar? '))
print(conjunto)
maior = menor = 0
for pos, i in enumerate(conjunto):
    if pos == 0:
        maior = i
        menor = i
    elif i > maior:
        maior = i
    elif i < menor:
        menor = i
amplitude = maior - menor
print(f'A amplitude do conjunto é: {amplitude} ')
