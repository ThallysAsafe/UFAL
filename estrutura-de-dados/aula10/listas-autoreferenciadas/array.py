class Celula:
    proximo = None
    item = None
    def __init__(self,item):
        self.item = item
        
class Listas:
    inicio = None
    fim = None
    tamanho = 0
    def __init__(self):
        pass
    
    def inserir(self,item):
        c = Celula(item)
        if self.estaVazia():
            self.inicio = c
        else:   
            self.fim.proximo = c 
        self.fim = c
        self.tamanho += 1
            
    def estaVazia(self):
        return self.inicio == None
            
    def imprimir(self):
        aux = self.inicio
        while aux != None:
            if aux.proximo == None:
                print(aux.item, end= ' ')
            else:
                print(aux.item, end= ', ')
            aux = aux.proximo
        print()
    def inserirPos(self,pos,valor):
        if pos >= 0 and pos < self.tamanho:
            if pos == 0 and self.tamanho == 0:
                self.inserir(valor)
            else:
                c = Celula(valor)
                if pos == 0:
                    c.proximo = self.inicio
                    self.inicio = c
                else:
                    aux = self.inicio
                    count = 0
                    while count < pos-1:
                        aux = aux.proximo
                        count += 1
                    c.proximo = aux.proximo
                    aux.proximo = c
                self.tamanho += 1
        elif self.estaVazia() and pos == self.tamanho:
            self.inserir(valor)
        else:
            print("Posição inválida")
        
lista = Listas()
lista.inserir(10)
lista.inserir(3)
lista.inserir(4)
lista.inserir(1)
lista.imprimir()
lista.inserirPos(3,8)
lista.inserirPos(0,7)
lista.imprimir()
