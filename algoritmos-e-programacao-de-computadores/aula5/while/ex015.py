'''15. Algoritmo que recebe dois conjuntos de inteiros A e B de tamanho n e calcula a distância euclidiana entre esses conjuntos. A distância euclidiana é dada por
D(A,B) = √(A[1] – B[1])² + (A[2] - B[2])² + … + (A[n] - B[n])²'''
r = 's'
conjA = []
conjB = []
somatot = []
soma = 0
qnt = int(input('Quantidade de elementos? '))
i=0
while i != qnt:
    conjA.append(int(input('Digite um valor para Conjunto A: ')))
    conjB.append(int(input('Digite um valor para Conjunto B: ')))
    i+=1
for c in range(len(conjA)):
    soma = (soma) + (conjA[c] - conjB[c])**2
somatot.append(soma)
for i in somatot:
    distancia = i ** (1/2)
print(f'A distancia Euclidiana dos conjuntos A e B é: {distancia:.2f}')
