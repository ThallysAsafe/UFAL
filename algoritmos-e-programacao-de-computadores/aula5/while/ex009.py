'''9. Faça um programa que recebe um conjunto de inteiros e um valor n e indica qual o valor mais próximo de n no conjunto'''
conjunto = []
diferença = []
valorN = 0
menor = 0
cont = 0
qnt = int(input('Digite quantos elementos deseja adicionar a um conjunto: '))
if qnt > 0:
    while qnt != 0:
        conjunto.append(int(input('Digite um numero inteiro: ')))
        qnt -= 1
    valorN = float(input('Digite o valor N: '))
    for n in conjunto:
        diferença.append(n-valorN)
        if (n-valorN) == 0:
            menor = n
            cont += 1
    for posição, diferença_numero in enumerate(diferença):
        if cont >= 1:
            break
        if diferença_numero < 0:
            diferença_numero = diferença_numero * -1
        if posição == 0:
            menor = diferença_numero
            mais_proximo = conjunto[posição]
        elif  diferença_numero >= 0 and diferença_numero < menor:
            mais_proximo = conjunto[posição]
            menor = diferença_numero
    print(f'O numero mais proximo de {valorN} é: {mais_proximo}')
else: 
    print('Quantidade Inválida!')