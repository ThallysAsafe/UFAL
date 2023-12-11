# 2. Identificar os valores de um conjunto que estão abaixo da
# média do conjunto
conjunto = [2,5,1,7,5,7,9,3]
soma = 0
for num in conjunto: # O(N)
    soma += num

media = soma / len(conjunto)
for num in conjunto: # O(N)
    if num < media:
        print(num)

#2*(O(n))