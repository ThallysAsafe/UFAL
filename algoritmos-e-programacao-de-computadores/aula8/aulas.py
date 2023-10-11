import pandas as pd
df = pd.read_csv('vendas.csv') # comando para ler o arq, dependendo q tipo for o arqv a função muda
print(df) # mostra a tabela inteira
print(df.head(10)) # mostra as x primeiras
print(df.tail(3)) # mostra as x ultimas
print(df.columns) # mostra as colunas
print(df.keys()) # mostras as colunas
print(df.email) # se vc colocar o nome da coluna ele ira mostrar todos os valores pertencentes aquela coluna, exemplo é email
print(df['name']) # pode achar assim tbm
print(df.sort_values(by='created_at')) # imprimi os dados organizados
print(df[df.email == 'jaida.schaden@example.com']) # imprimir as linhas que apresentam esse email
print(df[df.quantity > 3]) # apresenta quem teve quantity maior q 3

alunos = ['ana', 'carlos', 'gilberto', 'marta']
trabalhos = [9,8,7,6]
provas = [9,8,7,6]
seminarios = [9,8,7,6]
artigos = [9,8,7,6]

pdf = pd.DataFrame({'aluno': alunos,'trabalho': trabalhos, 'prova': provas, 'seminário': seminarios, 'artigo': artigos})
print(pdf)
pdf.to_csv('alunos.csv',index=False)