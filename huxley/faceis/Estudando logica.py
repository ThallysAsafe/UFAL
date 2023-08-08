lista = []
n = 0
cont = 0
qnt = 0
n1 = 0
a = 0
x = 1
p = 0
while(n != -1): 
    while (n != -1 and qnt != 1001):
        qnt += 1
        x += 1
        if (qnt == 1001 or n != -1):
            lista.append(n)
            n = int(input())
            n1 = n
    k = 0
    for i in range(0 ,x-1):
        if lista[i] == n1:
            k += 1
            x -= 1
        x -= 1
    p += 1
    qnt = 0
    lista.clear()
    if n1 >= 0:
        print(f'{n1} appeared {k} times')  