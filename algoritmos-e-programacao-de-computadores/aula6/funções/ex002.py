'''Ex: Cálculo do salário de funcionários
Uma empresa precisa calcular o pagamento de seus funcionários
Todo mês são contadas as horas trabalhadas por cada funcionário
Cada funcionário tem um valor a ser pago por hora trabalhada
Se a quantidade de horas trabalhadas excede 40 horas então é preciso calcular hora extra
O valor da hora extra é 1.5 vezes a hora comum de trabalho
'''
horas_trabalhadas = int(input('Quantas horas trabalhadas: '))
valor_hora = float(input('Quanto ganha por hora:'))
def calculadorasalarial(horas_trabalhadas, valor_hora):
    if horas_trabalhadas > 40:
        horas_normais = 40
        horas_extras = horas_trabalhadas - 40
    else: 
        horas_normais = horas_trabalhadas
        horas_extras = 0
    salario = horas_normais*valor_hora + horas_extras*(1.5*valor_hora)
    return salario
print('Salario: ', calculadorasalarial(horas_trabalhadas,valor_hora))

