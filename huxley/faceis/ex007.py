num = int(input())
maior = int(input())
proxi = 0
if num < 0:
    num = num * -1
i = 0
while (maior != num):
    i += 1
    if num * i <= maior:
        proxi = num * i
    elif proxi <= maior and proxi != 0:
        print(proxi)
        break
    elif num * i > maior:
        print(f'sem multiplos menores que {maior}')
        break
    else: 
        break
        

