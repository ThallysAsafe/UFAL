'''Exercício 2:
Você está projetando um duto de transporte de petróleo e precisa calcular a vazão volumétrica
média em metros cúbicos por segundo. Escreva um programa em Python que solicite ao usuário
o volume total de petróleo transportado em barris e a quantidade de dias de transporte, e em
seguida, imprima a vazão volumétrica média em metros cúbicos por segundo, considerando que
1 barril de óleo equivale a 0,159 metros cúbicos e que um dia possui 24 horas.
'''
barris = float(input('Digite o volume total de petroleo transportado por barris:  '))
dias = int(input('Digite a quantidade de dias de transporte: '))
volume = barris * 0.159   #Convertendo barris em volume total!
segundos = dias*24*60*60  #Convertendo dias em segundos
vazao = volume / segundos #Vazao media
print(f'A vazão volumétrica média é de {vazao} metros cúbicos por segundo.')
