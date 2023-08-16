'''3. Escreva um programa que possui uma função que recebe uma lista e diz qual a soma máxima entre dois elementos da lista'''
lista = [2,76,8,0,1,35,9]
def calculandoSomaMaximo(lista, qnt):
    soma = 0
    for r in range(qnt):
            maior = lista[0]
            for numero in lista:
                if maior < numero:
                    maior = numero
            soma += maior
            lista.remove(maior)
    return soma
qnt = int(input('Quantos maiores elementos da lista vc quer somar: '))
print(calculandoSomaMaximo(lista,qnt))
    