'''9. Faça um programa que recebe um conjunto de inteiros e um valor n e indica qual o valor mais próximo de n no conjunto'''
conjunto = []
diferença = []
valorN = 0
menor = 0
cont = 0
while True:
    conjunto.append(int(input('Digite um numero inteiro: ')))
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
valorN = float(input('Digite o valor N: '))
for n in conjunto:
    diferença.append(valorN-n)
    if (valorN-n) == 0:
        menor = n
        cont += 1
for pos, proximo in enumerate(diferença):
    if cont >= 1:
        break
    elif pos == 0:
        menor = conjunto[pos]
    elif proximo >= 0 and proximo <= menor:
        menor = conjunto[pos]
print(conjunto)
print(f'O numero mais proximo de {valorN} é: {menor}')