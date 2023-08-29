# 1. Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
def buscvogais(texto,vogal):
    dicionario = {'a':  0,'e':  0,'i': 0 ,'o':  0,'u': 0}
    for i in texto:
        for j in vogal:
            if i == j:
                dicionario[j] += 1         
    return dicionario
texto = input('Digite uma texto: ').lower()
vogal = 'aeiou'
print(buscvogais(texto,vogal))