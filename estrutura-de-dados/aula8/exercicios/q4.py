# 4. Uma função muito utilizada de um editor de
# texto é a função de desfazer as ultimas ações de
# edição, voltando o texto ao estado anterior.
# Implemente a função de desfazer em de um editor
# de texto, onde a estrutura armazena cada estado
# atual do texto. Considere uma alteração como
# uma inserção de uma nova palavra no texto.

class Texto:
    palavras = None
    proximo = None
    def __init__(self,palavras):
        self.palavras = palavras

class Pilha:
    topo = None
    def __init__(self):
        self.topo = None

    def escrever(self,palavras):
        c = Texto(palavras)
        c.proximo = self.topo
        self.topo = c

    def desfazer(self):
        if self.topo != None:
            self.topo = self.topo.proximo
        else:
            print("Ainda não foi digitado nada")

    def imprimir(self):
        aux = self.topo
        lista = []
        while aux != None:
            lista.append(aux.palavras)
            aux = aux.proximo
        for i in range(len(lista)-1,-1,-1):
            print(lista[i], end=' ')
        print()
c = Pilha()
c.escrever("Hoje é um lindo dia")
c.escrever("para pescar")
c.escrever("super casca")
c.imprimir()
c.desfazer()
c.imprimir()
c.desfazer()
c.imprimir()