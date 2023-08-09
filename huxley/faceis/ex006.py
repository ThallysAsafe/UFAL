num = int(input())
div = 0
temp = 0
if num > 6:
    for i in range(1,num):
        soma = 0
        for r in range(1,i):
            if i % r == 0:
                soma += r
        if soma == i:
            temp = soma
            print(temp)
else:
    print('SEM RESPOSTA')