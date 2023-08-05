'''7.   Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.'''
quantidade = int(input('Digite a quantidade de Carros que vendeu: '))
valor = float(input('Digite o valor total de suas vendas: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
comissao = float(input('Digite o valor que você recebe por carro vendido: R$'))
if (salario > 0 and quantidade >= 0 and valor >= 0 and comissao >= 0):
    saltot = salario + (comissao*quantidade) + valor*0.05
    print(f'O salário final é de: R${saltot:.2f}')
else:
    print(f'Você digitou algum Valor inválido!')
