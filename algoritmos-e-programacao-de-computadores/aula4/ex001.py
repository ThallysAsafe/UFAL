'''1. Faça um programa que leia dois números A e B e imprima o maior deles
'''
print('Qual é o Maior Numero!')
numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite mais um numero: '))
if numero1 > numero2:
    print(f'O numero maior é {numero1}')
elif numero2 > numero1:
    print(f'O numero maior é {numero2}')
else:
    print(f'Os numeros são iguais, logo o maior numero é o {numero1}')