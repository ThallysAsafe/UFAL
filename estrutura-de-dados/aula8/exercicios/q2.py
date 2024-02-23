class Pilha:
    dados = None
    fim = 0
    tam = 5

    def __init__(self):
        self.dados = [None]*self.tam

    def inserir(self,valor):
        if self.fim < self.tam:
            self.dados[self.fim] = valor
            self.fim += 1
        else:
            return "Pilha Cheia"

    def remover(self,containers):
        if self.fim > 0:
            for j in range(len(self.dados)):
                if containers == pilha[j] and self.fim != j:
                    self.fim -= 1
                    self.swap = self.dados[self.fim]
                    self.dados[self.fim] = None
                elif containers == pilha[j]:
                    self.fim -= 1
                    self.dados[self.fim] = None

        else:
            return "Pilha Vazia"
def comparacao():
    for containers in entrada:
        if pilha1.fim > pilha4.fim and pilha2.fim > pilha4.fim and pilha3.fim > pilha4.fim:
            pilha4.inserir(containers)
        elif pilha1.fim > pilha3.fim and pilha2.fim > pilha3.fim:
            pilha3.inserir(containers)
        elif pilha1.fim > pilha2.fim:
            pilha2.inserir(containers)
        else:
            pilha1.inserir(containers)        

pilha1 = Pilha()
pilha2 = Pilha()
pilha3 = Pilha()
pilha4 = Pilha()
swap =  Pilha()

entrada = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"]
pilhas = [pilha1,pilha2,pilha3,pilha4,swap]
menor = pilha1.fim

for pilha in pilhas:
    print(pilha)