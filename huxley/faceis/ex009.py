for i in range(2):
    num = input().split(' ')
    if i == 0:
        lista1 = (num)
    else:
        lista2 = (num)
lista3 = []
for cod in lista1:
    for cod2 in lista2:
        if cod == cod2:
            lista3.append(cod)
for cod in lista3:
    print(cod, end=' ')
    