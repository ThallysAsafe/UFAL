# 4. Identificar a soma máxima entre dois elementos de um
# conjunto
lista = [9,1,2,4,5,6]
maior = lista[1]
soma = 0
for  i in range(2): # O(2)
    maior = lista[1]
    for num in lista: # O(N)
        if num > maior:
            maior = num
    soma += maior
    lista.remove(maior)
print(soma)
# O(2) x O(N) --> O(2N)