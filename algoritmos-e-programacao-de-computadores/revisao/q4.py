a1 = float(input('Digite o valor do 1º angulo do triangulo: '))
a2 = float(input('Digite o valor do 2º angulo do triangulo: '))
if 0 < a1 != 90 or 0 < a2 != 90:    
    a3 = 180 - a2 - a1
    print(f'O valor do 3º angulo do triangulo é: {a3}')
else:
    print('Valor Inválido')