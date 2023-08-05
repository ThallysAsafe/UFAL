'''5.  Escreva um algoritmo que recebe três valores para os lados de um triângulo (a,b e c) e decide se a forma geométrica é um triângulo ou não e em caso positivo, classifique em isósceles, escaleno ou equilátero.'''
print('Verificador de Triangulos')
lado1 = float(input('Digite o valor do lado A: '))
lado2 = float(input('Digite o valor do lado B: '))
lado3 = float(input('Digite o valor do lado C: '))
if lado1 + lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 >= lado2:
    if lado1 == lado2 == lado3:
        print('Esse é um triangulo Equilátero')
    elif lado1 != lado2 != lado3:
        print('Esse é um triangulo Escaleno')
    else:
        print('Esse é um triangulo Isoceles')
else:
    print('Os valores não estão corretos pra formar um triangulo!')        
print('Fim do Programa!')
