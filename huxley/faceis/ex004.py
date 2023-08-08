num = 0
x = 0
lista = []
k = 0
p = 0
qnt = 0
n1 = int(input()) 
while (num != -1 and qnt != 20):
    qnt += 1
    if (num != -1):
        num = int(input())
        lista.append(num)
        x += 1     
for i in range(p, x-1):
    if lista[i] == n1:
        k += 1
        x -= 1
print(f'{n1} aparece {k} vezes')