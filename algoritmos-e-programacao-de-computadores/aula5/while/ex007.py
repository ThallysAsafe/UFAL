'''7. Faça um programa que recebe um conjunto de inteiros e verifica se existe algum número negativo no conjunto'''
conjunto = []
while True:
    conjunto.append(int(input('Digite um numero inteiro: ')))
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
for c in conjunto:
    if c < 0:
        condicao = True
        break
    else:
        condicao= False 
if condicao == True:
    print('Existe um numero negativo dentro do conjunto!')
else:
    print('Não existe numero negativo dentro do conjunto!')

