arq = open(r'C:\Users\Thallys\Documents\Estudos\UFAL\algoritmos-e-programacao-de-computadores\aula8\exercicios\arquivos\identidade.txt')
texto = arq.read()
arq.close()
texto = texto.split('\n')
lista = []
identidade = {}
for linha in texto:
    rg, nome = linha.replace('\n','').split(' ')
    identidade[rg] = nome
print(identidade)