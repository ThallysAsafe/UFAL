'''6. Faça um algoritmo que recebe dois conjuntos de inteiros A e B e calcula a distância euclidiana entre estes dois conjuntos'''
conjuntoA = []
conjuntoB = []
dis = []
soma = 0
while True:
    conjuntoA.append(int(input('Digite um numero inteiro pro conjunto A: ')))
    conjuntoB.append(int(input('Digite um numero inteiro pro conjunto B: ')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
    elif r not in 'Ss':
        print('Erro na entrada, Utilize N ou S')
        while r not in 'SsNn':
            r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break    
for c in range(len(conjuntoA)):
    junc = (conjuntoB[c] - conjuntoA[c])**2
    dis.append(junc)
print(dis)
for c in dis:
    soma = (soma) + (c)      
distancia = (soma) ** 1/2
print(f'A distancia Euclidiana dos conjuntos A e B é:{distancia}')

 