# 4. Faça um programa que leia a temperatura média de cada mês do ano em um arquivo e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).
caminho = 'arquivos/temperatura.txt'
def buscArq(caminho):
    arq = open(caminho)
    temps = arq.read()
    arq.close()
    return armazen(temps)
def armazen(temps):
    list = []
    soma = 0
    temps = temps.split('\n')
    for i in temps:
        i = float(i)
        soma += i
        list.append(i)
    media = soma / len(list)
    print(f'O valor da media atual foi de {media:.2f}')
    mês = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    print('Os meses que estão acima da temperatura media anual são? ')
    for i in range(0, len(list)):
        if list[i] > media:
            print(f'{list[i]}, {mês[i]}')
buscArq(caminho)
         