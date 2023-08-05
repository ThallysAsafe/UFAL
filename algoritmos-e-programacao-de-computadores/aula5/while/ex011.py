'''11. Algoritmo que recebe uma palavra e um caractere e conta as ocorrências do caractere na palavra'''
palavra = str(input('Digite uma palavra: ')).lower()
letra = str(input('Digite a letra que deseja procurar: ')).lower()
i = 0
cont = 0
while i < len(palavra):
    if palavra[i] == letra:
        condicao = True
        cont = cont + 1
    i += 1
if condicao == True:
    print(f'Tem a letra {letra} na palavra {palavra}, {cont} vezes!')
else:
    print(f'Não tem essa letra {letra} na palavra {palavra}')