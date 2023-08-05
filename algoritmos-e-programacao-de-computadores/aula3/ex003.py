print('Conversor de Moeda')
valor = float(input('Digite o valor que você quer converter: '))
taxa = float(input('Digite o valor do dolar para real para fazer a conversão: '))
conv = valor / taxa
print(f'Com {valor}R$ e com a taxa de {taxa}R$ é possivel comprar {conv:.2f}U$! ')
