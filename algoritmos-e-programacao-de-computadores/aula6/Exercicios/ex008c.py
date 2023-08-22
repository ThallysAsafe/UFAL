'''8. Faça um programa que recebe duas palavras A e B e verifica se B é uma substring de A.'''
palavra_a = input('Digite uma palavra: ')
palavra_b = input('Digite outra palavra: ')

def substring(palavra_a,palavra_b):
    if palavra_a < palavra_b:
        return 'não'
    j = 0
    i = 0
    while j < len(palavra_b) and i < len(palavra_a):
        if palavra_a[i] == palavra_b[j]:
            i += 1
            j += 1
        else:
            j = 0
            if palavra_a[i] == palavra_b[j]:
                j += 1
            i += 1
    if j == len(palavra_b):
        return ('sim')
    else:
        return ('não')
print(substring(palavra_a,palavra_b))