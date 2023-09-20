arq = open(r'C:\Users\Thallys\Documents\Estudos\UFAL\algoritmos-e-programacao-de-computadores\aula8\pasta\dados.txt')
texto = arq.read()
arq.close()
texto = texto.split("\n")
usuarios = []
for linha in texto:
    atributos = linha.split(', ')
    usuario = {'nome':atributos[0],'email':atributos[1],'senha':atributos[2]}
    usuarios.append(usuario)
print(usuarios)