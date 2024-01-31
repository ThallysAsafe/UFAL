notas = [9,8,7,6,5,4,3,2,1]
for i in range(len(notas)-1):
    # seleciona o menor elemento
    menor = i
    for j in range(i+1,len(notas)):
        if notas[menor] > notas[j]:
            menor = j
    # insere na i-ésima
    notas[i], notas[menor] = notas[menor],notas[i]
print(notas)
