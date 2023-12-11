# 1. Implemente uma função recursiva que, dados dois números inteiros x e n, calcule o multiplicacao de x.n
def multiplicacao(x,n):
    if x > 0 and n > 0:
        return x + multiplicacao(x,n-1)
    elif x < 0 and n < 0:
        return -x + multiplicacao(x,n+1)   
    elif x > 0 and n < 0:
        return -x + multiplicacao(x,n+1)  
    elif x < 0 and n > 0:
        return -x + multiplicacao(x,n-1)
    else:
        return 0
x = 0
n = 0
print(multiplicacao(x,n))