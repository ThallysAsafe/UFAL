# Buscar um elemento em uma lista de inteiros
lista = [1,2,3,4,5,6,7,8,9]
num = int(input('Digite o numero pra ver se tem na lista: '))
cont = 0
for c in lista:
    if num == c:
        cont += 1
        break
if cont >= 1:
    print(f'Existe o numero {num} na lista')
else:
    print(f'Não Existe o numero {num} na lista')       
        