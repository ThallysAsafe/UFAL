'''13. Algoritmo que recebe um conjunto de inteiros e dois números e verifica se estes dois numeros ocorrem em sequência no conjunto
Ex: lista = [1, 3, 5, 8, 6, 7, 4], n1 = 5 e n2 = 8'''
lista = []
i = 0
qnt = int(input('Quantos elementos quer adicionar ao conjunto?'))
while i < qnt:
    lista.append(int(input('Digite um numero: ')))
    i += 1
n1 = int(input('Digite um Valor pra N1: '))
n2 = int(input('Digite um Valor para N2: '))
cont = 0
for pos, i in enumerate(lista):
    if cont == 2:
        break
    elif i == n1:
        cont += 1
    elif i == n2:
        cont += 1
    elif pos > 1:
        cont = 0
if cont == 2:
    print(f'Sim, os numeros {n1} e {n2} são sequencia na lista')
else:
    print(f'Não, os numeros {n1} e {n2} não são sequencia na lista')
    