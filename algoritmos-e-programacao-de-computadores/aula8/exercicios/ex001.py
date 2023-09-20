arq = open(r'C:\Users\Thallys\Documents\Estudos\UFAL\algoritmos-e-programacao-de-computadores\aula8\exercicios\arquivos\identidade.txt')
texto = arq.read()
arq.close()
texto = texto.split('\n')
lista = []
identidade = {}
for linha in texto:
    atributos = linha.split(' ')
    identidade[atributos[0]] = atributos[1]
print(identidade)