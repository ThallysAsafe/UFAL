"""1. Faça um programa que recebe um número e calcula o fatorial desse número"""
num = int(input('Digite um numero: '))
qnt = num
fatorial2 = 1
fatorial = 1
if num < 0:
    print('Não existe esse fatorial!')
while True:
    if num == 0:
        break
    fatorial = fatorial * num
    num -= 1
print(f'O fatorial de {qnt} é: {fatorial}')
for f in range(1, qnt+1):
    fatorial2 = fatorial2 * f
print(f'O fatorial de {qnt} utilizando for é: {fatorial2}')
