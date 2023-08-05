print('Calculadora de Atraso de Pagamento')
print('='*30)
valor = float(input('Digite o Valor do Boleto: '))
dias = int(input('Digite quantos dias está atrasada a conta: '))
juros = 0.05
multa = 0.02 * valor
total = valor + multa + (valor*juros*dias)
print(f'O valor total para o pagamento do boleto em atraso é de {total}R$')
