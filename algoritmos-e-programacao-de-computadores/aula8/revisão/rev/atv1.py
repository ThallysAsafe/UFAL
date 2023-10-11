# Contagem de Linhas:
# Escreva um programa que lê um arquivo de texto e conta quantas linhas ele possui.
caminho = 'atv1.txt'
def arquivo(caminho):
    arq = open(caminho)
    texto = arq.read()
    arq.close()
    return texto

def contadorLinhas():
    texto = arquivo(caminho)
    texto = texto.split('\n')
    print(f'O arquivo {caminho} possui {len(texto)} linhas')
contadorLinhas()