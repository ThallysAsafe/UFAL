"""lista = [49]
soma = 50
i = 0
soma_temp = 0
while i < len(lista) and soma_temp <= soma:
    soma_temp += lista[i]
    i += 1
if i == len(lista):
    print(f'A soma do conjunto não é maior que {soma}')
else:
    print(f'A soma do conjunto é maior que {soma}')"""
palavra = 'algoritmo'
i = 0
letra = 't'
while i < len(palavra) and palavra[i] != letra:
    i += 1
if i == len(palavra):
    print('Não tem essa letra')
else:
    print(f'Tem essa letra, está na posição {i}')