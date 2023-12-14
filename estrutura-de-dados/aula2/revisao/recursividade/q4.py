# Contagem Recursiva de Dígitos:
# Crie uma função recursiva para contar o número de dígitos em um número inteiro.

def contador_digitos(n):
    if n < 10:
        return 1
    else: 
        return 1 +  contador_digitos(n//10)
n = 1123
print(contador_digitos(n))