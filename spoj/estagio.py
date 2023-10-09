
def entrada(qnt,resultado=[]):
    for i in range(qnt):
        num = input().split(' ')
        cod, med = num[0], num[1]
        if i == 0:
            codmaior = f'{cod} '
            maior = med
        else:
            if med > maior:
                codmaior = ''
                maior = med
                codmaior = f'{cod} '
            elif med == maior:
                codmaior += f'{cod} '
    resultado.append(codmaior)
    return resultado

def imprimirResultados(resultado):
    for melhorAluno in resultado:
        print(melhorAluno)

resultado = []
qnt = int(input())
while qnt != 0:
    entrada(qnt)
    qnt = int(input())
    if qnt == 0:
        imprimirResultados(resultado)