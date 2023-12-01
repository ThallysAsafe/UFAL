def fat(n):
    # caso base
    if n == 0:
        return 1
    else:
        # passo recursivo
        return n * fat(n-1)
n = 100
print(fat(n))