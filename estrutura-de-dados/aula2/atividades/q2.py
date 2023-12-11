# 2. Implemente uma função recursiva que, dados dois números inteiros x e n, calcule o elevado de x^n
def elevado(x, n):
    if x > 0 and n > 0:
        return x * elevado(x, n-1) 
    elif x > 0 and n < 0: 
        return ((1 / x) * (elevado(x, n+1)))
    elif x < 0 and n > 0:
        return x * elevado(x, n-1)
    elif x < 0 and n < 0: 
        return ((1 / x) * (elevado(x, n+1)))
    else: return 1
x = 5
n = -3
print(elevado(x, n))