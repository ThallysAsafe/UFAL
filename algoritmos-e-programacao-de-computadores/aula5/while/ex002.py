'''2. Faça um programa que conta o número de valores negativos em um conjunto
'''
num = [2,3,-4,5,1,-6,9]
cont = 0
'''outra forma
j = 0
while j != len(num):
    if num[j] < 0:
        cont += 1
    j += 1'''
for i in num:
    if i < 0: cont += 1
print(f'Existem {cont} valores negativos presentes dentro do conjunto')