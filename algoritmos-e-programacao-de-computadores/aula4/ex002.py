'''2. Faça um programa que leia a idade de uma pessoa e imprima sua categoria:
'''
idade = int(input('Digite Sua Idade: '))
if idade >= 60:
    print('Você é um Idoso!')
elif idade >= 18 and idade <= 59:
    print('Você é um Adulto!')
elif idade >= 14 and idade <= 17:
    print('Você é um Adolescente!')
elif idade != 0 and idade <= 13:
    print('Você é uma Criança!')
else:
    print('idade inválida!')
print('Fim do Programa')