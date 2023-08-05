'''5. Faça um programa que recebe um conjunto de inteiros e calcula a amplitude do conjunto.'''
qnt = int(input('Digite quantos elementos deseja adicionar: '))
j = 0
num = []
mai = men = 0
while qnt != j:
    j += 1
    num.append(int(input('Digite um numero inteiro: ')))
print(num)
for pos, c in enumerate(num):
    if pos == 0:
        mai = c
        men = c
    elif c >= mai:
        mai = c
    elif c <= men:
        men = c
amplitude = mai - men
print(f'A Amplitude dos Conjuntos é: {amplitude}')