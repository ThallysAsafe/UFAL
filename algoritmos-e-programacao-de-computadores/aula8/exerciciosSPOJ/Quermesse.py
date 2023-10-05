qnt = 1
cont = 0
result = []
while qnt != 0:
    qnt = int(input())
    if qnt != 0:
        num = input().split(' ')
        for i in range(qnt):
            ingressos = int(num[i])
            if ingressos == i+1:
                cont += 1
                result.append(ingressos)
                break
for i in range(cont):
    print(f'Teste {i+1}')
    print(result[i])
    print()