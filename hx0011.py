import timeit

def fatorial(num):
    fat = 1
    while 1 < num:
        fat *= num 
        num -= 1
    return fat
# Medir o tempo de execução do cálculo do fatorial para num = 5
tempo_execucao = timeit.timeit(lambda: fatorial(5), number=10000)  # Executar 10000 vezes para obter uma média
print(f"Tempo de execução médio: {tempo_execucao:.5f} segundos")
