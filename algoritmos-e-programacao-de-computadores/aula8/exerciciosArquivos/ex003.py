arq = open(r'C:\Users\Thallys\Documents\Estudos\UFAL\algoritmos-e-programacao-de-computadores\aula8\exercicios\arquivos\notas.txt')
dados = arq.read()
arq.close()
dados = dados.split('\n')
notas = []
for linha in dados:
    nota = float(linha)
    notas.append(nota)
def soma_notas(notas):
    soma = 0
    for i in notas:
        soma += i 
    return soma
def quantidademedia(soma):
    media = soma / len(notas)
    quant = 0
    for nota in notas:
        if nota > media:
            quant += 1
    return quant
soma = soma_notas(notas)
print(f'Quantidade de notas é igual a {len(notas)}')
print('Notas na ordem em que foram informadas')
for nota in notas:
    print(nota) 
print(f'A soma das notas é igual a {soma_notas(notas)}')
print(f'A media das notas: {soma_notas(notas)/len(notas)}')
print(f'Existe {quantidademedia(soma)} acima da media calculada')