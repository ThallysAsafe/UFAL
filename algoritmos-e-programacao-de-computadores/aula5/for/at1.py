# Verificar se uma lista é subconjunto de outra lista
a = []
b = []
cont = 0
qtd1 = int(input('Digite a quantidade de elementos da lista A:'))
qtd2 = int(input('Digite a quantidade de elementos da lista B:'))
for i in range(qtd1):
    a.append(int(input('Digite um numero para Lista A: ')))
for i in range(qtd2):
    b.append(int(input('Digite um numero para Lista B: ')))
if a in b and b in a:
    print('Lista A é igual a Lista B')
elif a in b:
    print('A lista A é um subconjuto da lista B')
else:
    print('A lista A não é subconjunto da lista B')
        

