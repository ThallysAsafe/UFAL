qnt = 2
cont = 0
resultado = []
resposta = []
while qnt != 0 and qnt >= 2 and qnt <= 10:
    qnt = int(input())
    if qnt != 0 and qnt >= 2 and qnt <= 10:
        sequencia = []
        entrada = []
        cont += 1
        for i in range(qnt):
            num = input().split(' ')
            cod = ''
            entrada.append({'A': set(num[0:2]) ,'B': set(num[2:4]),'C': set(num[4:6]) ,'D': set(num[6:8]),'E': set(num[8:10])})
            sequencia.append(num[10:16])
            print(sequencia)
        separador_sequencias = []
        for i in range(qnt):
            a = []
            for j in range(6):
                a.append(entrada[i][sequencia[i][j]])
            separador_sequencias.append(a)
        resultado = []
        for i in range(len(separador_sequencias[0])):
            intersec = separador_sequencias[0][i]
            for conjunto in separador_sequencias[1:]:
                intersec = intersec & conjunto[i]
            resultado.append(intersec)
        a = ''
        for i in resultado:
            for res in i:
             a += f'{res} '
        resposta.append(f'Teste {cont}\n{a}\n')
for respofinal in resposta:
    print(respofinal)
