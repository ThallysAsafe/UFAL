'''8. Faça um programa que recebe duas palavras A e B e verifica se B é uma substring de A.'''
def substring(palavra_a,palavra_b):
    resultado = 'não'
    if len(palavra_a) < len(palavra_b):
        if palavra_a in palavra_b:
            resultado = 'sim'
            return resultado
    else:
        if palavra_b in palavra_a:
            resultado = 'sim'
            return resultado
    return resultado
palavra_a = (input('Digite uma palavra-A: '))
palavra_b = (input('Digite uma palavra-B: '))
print(substring(palavra_a,palavra_b))