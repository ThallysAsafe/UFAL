# Fatorial Recursivo:
# Implemente uma função recursiva para calcular o fatorial de um número.

def fatorial(i):
    if i == 0:
        return 1
    else:
        return i * fatorial(i-1)
i = 5
print(fatorial(i))
