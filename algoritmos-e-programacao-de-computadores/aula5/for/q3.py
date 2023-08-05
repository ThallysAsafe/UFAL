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
for c in b:
    if c in a:
        cont = cont + 1
    else:  
        cont += 0
if a in b and len(a) == cont:
    print('Lista A é igual a Lista B')
elif len(a) == cont:
    print('A lista A é um subconjuto da lista B')
elif len(b) == cont:
    print('A lista B é um subconjuto da lista A')
else:
    print('A lista A não é subconjunto da lista B')
        
