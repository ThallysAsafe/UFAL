# Escreva o algoritmo e a função de custo de tempo deste para
# os seguintes problemas
# ● 1. Contar o número de elementos negativos em um conjunto
numeros = [1,-2,4,5,-6,-1,-9]
contador = 0
for numero in numeros: #   O(N)
    if numero < 0:
        contador += 1
print(contador) 

# O(N) --> O(N) linear