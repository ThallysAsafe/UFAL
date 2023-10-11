# Concatenação de Arquivos:
# Crie dois arquivos de texto e, em seguida, escreva um programa que os concatene em um terceiro arquivo.
import os
def arquivo(caminho):
    arq = open(caminho)
    texto = arq.read()
    arq.close()
    return texto

def juntaArquivos():
    caminho = 'atv2_dados/atv2.txt'
    if os.path.exists(caminho):
        texto = arquivo(caminho)
        texto = texto.split('\n')
    else:
        arq = open('atv2_dados/atv2.txt','w')
        arq.close()     
    caminho = 'atv2_dados/atv2_1.txt'
    if os.path.exists(caminho):
        texto2 = arquivo(caminho)
        texto2 = texto2.split('\n')
    else:
        arq = open('atv2_dados/atv2_1.txt','w')
        arq.close()     
    if len(texto2) > len(texto):    
        for i in range(len(texto)):
            texto.append(texto2[i])
    else:
        for i in range(len(texto2)):
            texto.append(texto2[i])
    arq = open('atv2_dados/atv2juncao.txt','w')
    for i in range(len(texto)):
        arq.write(texto[i] + '\n')
    arq.close()

juntaArquivos()