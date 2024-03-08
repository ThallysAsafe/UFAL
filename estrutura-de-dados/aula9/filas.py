class Fila:
    inicial = 0
    tam = 0
    fim = 0
    estrutura = None

    def __init__(self,tam):
        self.tam = tam
        self.estrutura = [None]*tam

    def inserir(self,valor):
        
        if not self.estaCheia():
            self.estrutura[self.fim] = valor
            self.fim =  (self.fim + 1)% self.tam
        else:
            print("Fila cheia")

    def estaVazia(self):
        return self.inicial == self.fim
    def estaCheia(self):
        return self.inicial == (self.fim+1)%self.tam

    def remover(self):
        if not self.estaVazia():
            self.estrutura[self.inicial] = None
            self.inicial = (self.inicial+1)%self.tam
        else:
            print("Fila vazia")

fila = Fila(10)
print(fila.estrutura)
fila.inserir(10)
print(fila.estrutura)
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)
fila.remover()
fila.inserir(9)

fila.remover()
fila.inserir(10)
fila.remover()
fila.inserir(10)
fila.remover()
fila.inserir(10)
fila.remover()
fila.inserir(10)
fila.remover()
fila.inserir(10)
fila.remover()
fila.inserir(10)
fila.remover()
fila.inserir(10)
fila.inserir(10)
fila.inserir(10)

print(fila.estrutura)



print(fila.estrutura)
print(fila.inicial,fila.fim)