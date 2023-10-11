# Leitura e Escrita Reversa:
# Leia o conteúdo de um arquivo de texto e escreva-o de volta no mesmo arquivo, mas na ordem reversa, de modo que a última linha seja a primeira e assim por diante.
import os

caminho = os.path.abspath(__file__).replace('atv3.py','atv3.txt')


def arquivo(caminho):
    arq = open(caminho)
    texto = arq.read()
    arq.close()
    return texto

def escreveArquivos():
    if os.path.exists(caminho):
        texto = arquivo(caminho)
        texto = texto.split('\n')
    else:
        arq = open(caminho,'w')
        texto = arq.read()
        arq.close()
    arq = open(caminho,'w')
    for i in range(1,len(texto)+1):
        if i == len(texto):
            arq.write(f'{texto[-i]}')
        else: 
            arq.write(f'{texto[-i]}\n')
    arq.close()
escreveArquivos()