num = int(input())
div = 0
temp = 0
if num > 6 and num < 20000:
    for i in range(1,num):
        soma = 0
        if num <= 5:
            print('EMPTY')
        for r in range(1,i):
            if i % r == 0:
                soma += r
            if soma == i:
                temp = soma
        if temp == soma and soma > 0:
            print(temp)
else:
    print('SEM RESPOSTA')