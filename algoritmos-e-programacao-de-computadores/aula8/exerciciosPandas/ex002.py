# 2. Faça um programa que recebe do usuário duas notas de vários alunos e escreve um arquivo csv contendo as duas notas e a média do aluno.
import pandas as pd
arq = 'notas.csv'
def calculadoraMedia(arq):
    nota1 = []
    nota2 = []
    medias = []
    alunos = []
    arq = pd.read_csv(arq)
    for i in range(len(arq['nota1'])):
        media=(arq['nota1'][i]+arq['nota2'][i])/2
        medias.append(media)
        nota1.append(arq['nota1'][i])
        nota2.append(arq['nota2'][i])
        alunos.append(arq['alunos'][i])
    
    nvarq = pd.DataFrame({'Alunos': alunos,'1º nota': nota1, '2º nota': nota2,'Media': medias})
    nvarq.to_csv('alunosMedia.csv',index=False)
calculadoraMedia(arq)