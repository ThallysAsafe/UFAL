'''6. Uma das tarefas de um caixa eletrônico é decidir qual a combinação de cédulas deve fornecer ao usuário quando este solicita um saque, de modo a minimizar o número de cédulas fornecidas. Sabendo que um caixa eletrônico possui notas de 100, 50, 10, 5 e 1, faça um programa que recebe um valor a ser sacado e decida qual a combinação de cédulas irá fornecer. 
'''
valor = int(input('Digite o valor que deseja saquar: R$'))
total = valor

totced100 = None
totced50 = None
totced10 = None
totced5 = None
totced1 = None
if valor >= 0:
    totced100 = total // 100
    totced50 = (total-100*totced100) // 50
    totced10 = (total-100*totced100-50*totced50) // 10
    totced5 = (total-100*totced100-50*totced50-10*totced10) // 5
    totced1 = (total-100*totced100-50*totced50-10*totced10-5*totced5) // 1
    print(f'{totced100} Notas de 100,00R$\n{totced50} Notas de 50,00R$\n{totced10} Notas de 10,00R$\n{totced5} Notas de 5,00R$\n{totced1} Notas de 1,00R$\n')
else:
    print('Valor Inválido!')