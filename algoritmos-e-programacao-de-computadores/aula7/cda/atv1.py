num = int(input('Digite um numero inteiro: '))
resultado = 0
for i in range(1,num+1):
    if num % i == 0:
        resultado += 1
if resultado == 2:
    print(f'{num} é um numero primo')
else:
    print(f'{num} não é um numero primo')