'''Ex: Cálculo de imposto de renda
Todo mês uma empresa precisa calcular quanto de imposto de renda de seus funcionários irá repassar para a receita federal
Regras
Se o funcionário ganha até R$ 1500,00 ele está isento de pagar imposto
Se ganha acima disso, precisa pagar 27% de imposto sobre o salário
'''
def calculadoraimposto(salario):
    if salario <= 1700:
        return 0
    else:
        return round(salario * 0.27, 2)
lista_salarios = [
    1450.30,
    1840.50,
    2450,
    3641.90,
    5000
]
for salario in lista_salarios:
    imposto = calculadoraimposto(salario)
    print(f'Salário: {salario}', f'\nImposto: {imposto}' '\n...')