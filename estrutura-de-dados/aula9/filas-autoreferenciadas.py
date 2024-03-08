class Celula:
    item = None
    proximo = None
    def __init__(self,valor):
        self.item = valor

class Fila:
    inicio = None
    fim = None

    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        aux = self.inicio
        while aux != None:
            if aux.proximo == None:
                print(aux.item, end= ' ')
            else:
                print(aux.item, end= ', ')
            aux = aux.proximo
        print()

    def inserir(self,valor):
        c = Celula(valor)
        if self.estaVazia():
            self.inicio = c
        else:
            self.fim.proximo = c
        self.fim = c 

    def estaVazia(self):
        return self.inicio == None
    
    def remover(self):
        if not self.estaVazia():
            aux = self.inicio
            valor = self.inicio.item
            del aux
            self.inicio = self.inicio.proximo
            return valor 
        else:
            print("Fila está vazia")
            return None
fila = Fila()
fila.inserir(5)
fila.imprimir()
fila.inserir(4)
fila.imprimir()
fila.inserir(3)
fila.imprimir()
fila.inserir(2)
fila.imprimir()
fila.inserir(1)
fila.imprimir()
fila.inserir(0)
fila.imprimir()
fila.remover()
fila.remover()
fila.inserir(5)
fila.imprimir()