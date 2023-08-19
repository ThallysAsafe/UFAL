'''8. Faça um programa que recebe duas palavras A e B e verifica se B é uma substring de A.'''
def substring(palavra_a,palavra_b):
    resultado = 'não'
    contador = 0
    i = 0
    while i < len(palavra_a) and len(palavra_a) > len(palavra_b):
        if contador < len(palavra_b):
            if palavra_a[i] != palavra_b[contador]:
                contador = 0
                if palavra_a[i] == palavra_b[contador]:
                    contador += 1
            else:
                contador += 1
            i += 1
        else:
            break
    if contador == len(palavra_b):
        resultado = 'sim'
        return resultado
    else:
        return resultado
palavra_a = (input('Digite uma palavra-A: '))
palavra_b = (input('Digite uma palavra-B: '))
print(substring(palavra_a,palavra_b))