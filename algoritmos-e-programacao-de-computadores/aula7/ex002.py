# 2. Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome.
nome = None
dicionario = {}
while nome != '':
    lista = []
    nome = input('Nome do aluno: ')
    if nome == '': 
        break
    lista.append(float(input('1º Nota: ')))
    lista.append(float(input('2º Nota: ')))
    dicionario[nome] = lista
def medias(dicionario):
    j = 0
    while j < len(dicionario.keys()):  
        for key in dicionario.keys():
            soma = 0 
            for i in range(2):
                soma += dicionario[key][i] 
            media = soma / 2
            print(f"{key}: {media}")
            j += 1
medias(dicionario)
