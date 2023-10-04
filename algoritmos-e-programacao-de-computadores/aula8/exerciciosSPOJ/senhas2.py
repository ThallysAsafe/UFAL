qnt = 1
lista = []
resposta = []
cont = 0
result = []
while qnt != 0:
    qnt = int(input())
    if qnt != 0 and qnt >= 2 and qnt <= 10:
        sequencia= []
        cont += 1
        entrada = [{'A': {} ,'B': {},'C':{} ,'D': {},'E': {}} for _ in range(qnt)]
        for i in range(qnt):
            num = input().split(' ')
            cod = []
            for chave in entrada[i].keys():
                for j in range(len(num[0])):
                    if num[j] in ['0','1','2','3','4','5','6','7','8','9']:
                        entrada[i][chave] = {num[j],num[j+1]}
                        num.pop(1)
                        num.pop(0)
            for j in range(len(num)):
                if num[j] in ['A','B','C','D','E']:
                    cod.append(num[j])
            sequencia.append(cod)
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


