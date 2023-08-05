valor = int(input('Digite o valor: R$'))
total = valor 
totced100 = 0
totced50 = 0
totced20 = 0
totced10 = 0
totced5 = 0
totced2 = 0
totced1 = 0
if total >= 100:
    totced100 = total // 100
    total = total - 100 * totced100
if total >= 50:
    totced50 = total // 50
    total = total - 50 * totced50
if total >= 20:
    totced20 = total // 20
    total = total - 20 * totced20
if total >= 10:
    totced10 = total // 10
    total = total - 10 * totced10
if total >= 5:
    totced5 = total // 5
    total = total - 5 * totced5
if total >= 2:
    totced2 = total // 2
    total = total - 2 * totced2
if total >= 1:
    totced1 = total // 1
    total = total - 1 * totced1
if total == 0:
    print(f'{totced100} notas de 100,00 R$')
    print(f'{totced50} notas de 50,00 R$')
    print(f'{totced20} notas de 20,00 R$')
    print(f'{totced10} notas de 10,00 R$')
    print(f'{totced5} notas de 5,00 R$')
    print(f'{totced2} notas de 2,00 R$')
    print(f'{totced1} notas de 1,00 R$')
else:
    print('Valor inválido')




        

