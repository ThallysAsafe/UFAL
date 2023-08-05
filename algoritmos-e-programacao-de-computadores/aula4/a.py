'''Exercício 1:
Você está analisando os dados de um poço de petróleo e precisa calcular a produção diária média
em barris de óleo. Escreva um programa em Python que solicite ao usuário o volume total de
óleo produzido em metros cúbicos e a quantidade de dias de produção, e em seguida, imprima
a produção diária média em barris de óleo, considerando que 1 barril de óleo equivale a 0,159
metros cúbicos.
''' # NÃO PRECISA COLOCAR O QUE ESTÁ ACIMA!
volume = float(input('Digite o volume total de oleo produzido em metros cubicos: '))
dias = int(input('Digite a Quantidade de Dias de Produção: '))
barris = volume / 0.159
media = barris / dias
print(f'A produção diaria média é de {media} Barris de Oléo.')
print('A produção diaria média é de {} Barris de Oléo.'.format(media))
print('A produção diaria média é de Barris de Oléo:',media)

