'''3. Faça um programa que recebe um conjunto de inteiros e imprime os valores que estão abaixo da média do conjunto'''
num = []
abaixomedia = []
qnt = int(input('Digite quantos numeros do conjunto:'))
j = 0
soma = 0
while qnt != j:
    nums = int(input('Digite um numero inteiro: '))
    num.append(nums)
    soma = soma + nums
    j += 1
media = soma / qnt
for i in num:
    if i < media:
        abaixomedia.append(i)
print(f'Os numeros a baixo da media dos valores do conjunto são: {abaixomedia}')
