# Calcular a média de uma lista de inteiros
soma = 0
num = []
qtd = int(input('Digite a quantidade de elementos da lista:'))
for i in range(qtd):
    num.append(int(input('Digite um valor inteiro para ser adicionado a lista: ')))
for c in num:
    soma = soma + c
media = soma / (len(num))
print(f'A media da soma é dos valores presentes na lista é: {media}')
