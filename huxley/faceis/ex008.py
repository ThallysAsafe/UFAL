num = 0
soma = 0
i = 0
qnt = 0
falta = 0
while (num % 2 == 0):
    num = int(input())
    qnt += 1
    if i == 0:
        n1 = num
        i += 1
    soma += num
div = soma // 12
if div < 1:
    div = 1
div2 = div
falta = 12*div2 - (soma-num)
if falta < 0:
    falta *= -1 
preço = div * 7.89
print(preço)
print(falta)