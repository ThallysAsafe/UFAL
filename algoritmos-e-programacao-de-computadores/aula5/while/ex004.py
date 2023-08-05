'''4. Faça um programa programa que recebe um conjunto de inteiros e conta quantos elementos maiores que n existem no conjunto'''
num = []
j = 0
acimacorte = []
qnt = int(input('Digite quantos numeros do conjunto:'))
while qnt != j:
    j += 1
    num.append(int(input('Digite um numero inteiro: ')))
print('-='*30)
n = int(input('Qual é o valor de corte do conjunto numérico: '))
for i in num:
    if i > n:
        acimacorte.append(i)
print(f'Os elementos presentes no conjunto que estão acima de {n} é: {acimacorte}')