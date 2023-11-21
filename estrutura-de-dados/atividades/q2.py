# 2. Identificar os valores de um conjunto que estão abaixo da
# média do conjunto
conjunto = [2,5,1,7,5,7,9,3]
soma = 0
for num in conjunto:
    soma += num
media = soma / len(conjunto)
for num in conjunto:
    if num > media:
        print(num)
