import calculadora
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
opcao = int(input('''
    (1) - Adição
    (2) - Subtração
    (3) - Multiplicação
    (4) - Divisão
    Digite a opção desejada: '''))
if opcao >= 1 and opcao <= 4:
    if opcao == 1:
        resultado = calculadora.soma(num1, num2)
    elif opcao == 2:
        resultado = calculadora.subtracao(num1, num2)
    elif opcao == 3:
        resultado = calculadora.multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = calculadora.divisao(num1, num2)
    print(resultado)
else:
    print('OPÇÃO INVÁLIDA!')
