'''12. Algoritmo que recebe uma palavra e conta quantas vogais há na palavra'''
palavra = str(input('Digite uma palavra: '))
vogais = 'aeiou'
i = 0
cont = 0
while i < len(palavra):
    if palavra[i] in vogais:
        cont += 1
        condicao = True
    i += 1    
if condicao == True:
    print(f'Existe {cont} vogais na palavra {palavra}')
else:
    print(f'Não Existe palavras, sem vogais')