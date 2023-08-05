produto = float(input('Digite o valor do produto: '))
if produto > 0:
    avista = produto * 0.9
    parc = produto / 3
    comv = avista * 0.05
    comp = produto * 0.05
    print(f'''Valor a vista com desconto de 10%: R${avista:.2f}
    Valor da Parcela em 3x sem juros: R${parc:.2f}
    Comissão do Vendendor a vista: R${comv:.2f}
    Comissão do Vendendor a prazo: R${comp:.2f}''')
else:
    print('Valor inválido!')
