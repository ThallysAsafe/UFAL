# 3. Calcular o fatorial de um número
numero = int(input('Digite um numero: '))
fatorial = 1
for i in range(1,numero+1): # O(N)
    fatorial *= i 
print(fatorial)
# O(N) --> O(N)