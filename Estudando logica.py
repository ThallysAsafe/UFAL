n = int(input())
lista = [n*1, n*10,n*100,n*1000]
qnt = 1000
cont = 0
i = 3
while qnt != -1:
    if qnt == lista[i]:
        cont += 1
    qnt -= 1
    i -= 1
print(cont)