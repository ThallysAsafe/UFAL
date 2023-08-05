'''8. Faça um programa que recebe um conjunto de inteiros e um valor n e verifica se existe algum número com valor maior que n no conjunto'''
conjunto = []
valorN = 0
while True:
    conjunto.append(int(input('Digite um numero inteiro: ')))
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
valorN = float(input('Digite o valor N: '))
for n in conjunto:
    if n > valorN:
        condicao = True
        break
    else:
        condicao = False
if condicao == True:
    print(f'Existe um valor maior que o valor {valorN}')
else:
    print(f'Existe não um valor maior que o valor {valorN}')
