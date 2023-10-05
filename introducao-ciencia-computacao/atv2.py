#  Objetivo: Dado um número, o sistema deve receber efetuar o cálculo do seu fatorial de
# duas formas:
# ◦ Utilizando um algoritmo iterativo: função fatorial_iterativo(numero)
# ◦ Utilizando um algoritmo recursivo: função fatorial_recursivo(numero)

#  Comportamento desejado:
# ◦ O sistema deve ler inicialmente um número: numero.
# ◦ Em seguida, deve executar a função fatorial_iterativo(numero) e apresentar seu
# retorno.
# ◦ Finalmente, deve executar a função fatorial_recursivo(numero) e apresentar seu
# retorno.
# ◦ Os retornos das duas funções deve ser o mesmo, equivalente a “numero fatorial”.
#  Diretrizes Adicionais:
# ◦ A função “fatorial_iterativo(numero)” deve utilizar estruturas de repetição
# (enquanto ou para).
# ◦ A função “fatorial_recursivo(numero)” NÃO deve utilizar estruturas de repetição
# # (enquanto ou para), mas chamadas recursivas para a função.
def fatorial_interativo(numero):
    fatorial = 1
    for i in range(1,numero+1):
        fatorial *= i
    return fatorial

def fatorial_recursivo(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial_recursivo(numero-1)
def inicio():
    numero = int(input('Digite um numero para saber o seu fatorial: '))
    print('Fatorial interativo: ', end='')
    print(fatorial_interativo(numero))
    print('Fatorial recursivo: ', end='')
    print(fatorial_recursivo(numero))

inicio()
