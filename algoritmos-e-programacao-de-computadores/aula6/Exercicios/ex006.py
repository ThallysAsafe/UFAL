'''6. Um a palavra A é dita uma permutação de uma palavra B se os caracteres de A formam uma permutação dos caracteres de B
Ex: amor é uma permutação de roma
Ex: metro é uma permutação de morte
Faça uma função permutação que recebe duas palavras e verifica se uma é permutação da outra'''

def permutacao(palavra_a,palavra_b):
    resultado = 0
    for letra_a in palavra_a:
        for letra_b in palavra_b:
            if letra_a == letra_b:
                resultado += 1
    if resultado == len(palavra_a):
        print('É uma permutação')
    else:
        print('Não é uma permutação')
palavra_a = input('Digite uma palvra: ')
palavra_b = input('Digite a outra palvra: ')
permutacao(palavra_a,palavra_b)