class Lista:
    tam = 0 
    itens = None
    fim = 0
    def __init__(self,tam):
        self.tam = tam
        self.itens = [None]*tam
        
    def inserirPos(self,pos,item):
        if self.fim < self.tam and abs(pos) <= self.fim:
            if pos == self.fim:
                self.fim += 1
            self.itens[pos] = item
        else:
            print("Posição inválida")
    
    def append(self,itens):
        if self.fim < self.tam:
            self.itens[self.fim] = itens
            self.fim += 1
        else:
            print("Fila cheia")
            
    def inserirDesloc(self,pos,item):
        if self.fim < self.tam and pos < self.fim:
            if self.itens[pos] != None:
                aux = self.fim
                while pos < aux:
                    self.itens[aux] = self.itens[aux-1]
                    aux -= 1
                self.fim += 1
                self.inserirPos(pos,item)
        else:
            print("Posição invalida")
        
    def pop(self,pos):
        if self.fim > 0 and abs(pos) < self.fim:
            self.itens[pos] = None
            item = self.itens[pos] 
            for i in range(pos,self.fim):
                self.itens[i]=self.itens[i+1]
            self.fim -=1 
            return item
        else:
            print('Posicao invalida')
lista = Lista(10)
lista.inserirPos(0,2)
lista.inserirPos(4,3)
lista.inserirPos(2,4)
print(lista.itens)
lista.append(4)
lista.append(8)
lista.append(1)
print(lista.itens)
lista.inserirDesloc(2,10)
lista.pop(3)
print(lista.itens)
print(lista.fim)