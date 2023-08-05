from math import pi
print('Calculadora de Área de um Cilindro')
print('='*30)
r = float(input('Digite valor do raio: '))
altura = float(input('Digite o valor da Altura: '))
area = 2*r*pi*(r + altura)
print(f'O valor da Área do Cilindro é {area:.2f}')
