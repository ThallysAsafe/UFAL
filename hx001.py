numeros = []
ordem = []
qnt = int(input('Quantos números você deseja inserir? '))
i=0
for n in range(qnt):
    numeros.append(int(input(f"Digite o número {n}: ")))
    resto = n % 2
for n in range(qnt):
    if n >= 1 and resto == 1:
        if numeros[n] >= numeros[n-1]:
            ordem.append(numeros[n-1])
            ordem.append(numeros[n])
        else:
            ordem.append(numeros[n])
            ordem.append(numeros[n-1])
        numero = ordem[:]
print(numero)














"""for n in range(0, qnt):
    if n == 0:
        a.append(n)
    else:
        if numeros[n] < numeros[n-1]:
            ordem.append(numeros[n])
            ordem.append(numeros[n-1])
        else:
            ordem.append(numeros[n-1])
            ordem.append(numeros[n])
print(ordem)
"""


