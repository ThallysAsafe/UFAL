'''4. Uma empresa de vendas tem vários corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. Escreva um programa que recebe o nome e o valor vendido por um corretor e indique qual será sua comissão.'''
venda = float(input('Digite o valor da venda: '))
if venda > 50000:
    comissao = venda * 0.12
    print(f'O valor da venda: {venda}, e o valor da comissão é {comissao:2f} R$')
elif venda >= 30000:
    comissao = venda * 0.095
    print(f'O valor da venda: {venda}, e o valor da comissão é {comissao:2f} R$')
else:
    comissao = venda * 0.07
    print(f'O valor da venda foi {venda}, e o valor da comissão é {comissao:2f} R$')