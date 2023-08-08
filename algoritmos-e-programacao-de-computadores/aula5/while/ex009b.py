'''9. Faça um programa que recebe um conjunto de inteiros e um valor n e indica qual o valor mais próximo de n no conjunto'''
numeros = [2,7,3,9,-1]
i = 0
n = int(input('valor de n: '))
diferença = 0
while i < len(numeros):
    if numeros[i] > n:
        diferença = numeros[i] - n
    if numeros[i] < n:
        diferença = n - numeros[i]
    if i == 0:
        menor = diferença
        mais_proximo = numeros[i]
    if diferença == 0 or numeros[i] == n:
        menor = diferença
        mais_proximo = numeros[i]
        break
    if diferença < menor and diferença >= 0:
        menor = diferença
        mais_proximo = numeros[i]
    i += 1
print(f'O numero mais proximo de {n} é: {mais_proximo}')