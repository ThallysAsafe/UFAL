num = 0
x = 0
lista = []
k = 0
p = 0
while(num != -1):
    qnt = 1
    while (num != -1 and qnt != 10):
        qnt += 1
        if (num != -1 and qnt != 10):
            num = int(input())
            lista.append(num)
            x += 1 
            n1 = lista[0]    
    for i in range(p, x-1):
        if lista[i] == n1:
            k += 1
            x -= 1
    print(f'{n1} aparece {k} vezes')
    