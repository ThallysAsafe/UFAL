# 1. Faça um programa que lê um arquivo csv contendo dados de temperatura e umidade em vários dias em uma cidade e diga qual foi o dia mais quente o mais frio da cidade.
import pandas as pd
arquivo = 'temperatura.csv'
def lercsv(arquivo):    
    arq = pd.read_csv(arquivo)
    maior = arq['temperatura'][1]
    menor = arq['temperatura'][1]
    for i in range(len(arq['temperatura'])):
        if arq['temperatura'][i] < menor:
            menor = arq['temperatura'][i]
            dia = i
        elif arq['temperatura'][i] > maior:
            dia2 = i
            maior = arq['temperatura'][i]
    dia += 1
    dia2 += 1

    print(f'Dia {dia2} foi o mais quente com {maior} Cº')
    print(f'Dia {dia} foi o mais frio com {menor} Cº')

lercsv(arquivo)
