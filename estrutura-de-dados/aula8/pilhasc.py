class Pilha:
    dados = None
    fim = 0
    tam = None

    def __init__(self,tam):
        self.dados = [None]*tam
        self.tam = tam

    def inserir(self,valor):
        if self.fim < self.tam:
            self.dados[self.fim] = valor
            self.fim += 1
        else:
            return "Pilha Cheia"

    def remover(self):
        if self.fim > 0:
            self.fim -= 1
            self.dados[self.fim] = None
        else:
            return "Pilha Vazia"
p = Pilha(10)
p.inserir(-1)
p.inserir(-2)
p.inserir(-2)
p.remover()
print(p.dados)