# Sequência de Fibonacci Recursiva:
# Implemente uma função recursiva para gerar o enésimo termo da sequência de Fibonacci.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = 6
print(fibonacci(n))