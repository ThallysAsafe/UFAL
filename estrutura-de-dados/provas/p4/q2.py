class Celula:
    valor = None
    proximo = None
    def __init__(self, valor):
        self.valor = valor

class Pilha:
    topo = None
    topo2 = None
    def __init__(self):
        self.topo = None
        self.topo2 = None
    def inversao(self):
        aux = self.topo
        while aux != None:
            inverso = Celula(aux.valor)
            inverso.proximo = self.topo2
            self.topo2 = inverso
            aux = aux.proximo  
        return self.topo2

    def inserir(self,valor):
        c = Celula(valor)
        c.proximo = self.topo
        self.topo = c
        return self.topo
        
    def remover(self):
        if self.topo != None:
            self.topo = self.topo.proximo

    def imprimir(pilha):
        aux2 = pilha
        while aux2 != None:
            print(aux2.valor)
            aux2 = aux2.proximo    
        print('-------')

def palindromo(palavras):
    pilha1 = Pilha()
    palavras = palavras.lower().replace(' ','')
    for j in range(len(palavras)):
        pilha1.inserir(palavras[j])
    topo2 = pilha1.inversao()
    for i in range(len(palavras)):
        if topo2.valor == pilha1.topo.valor:
            topo2 = topo2.proximo
            pilha1.remover()
        else:
            return 'Não'
    if pilha.topo == None:
        return "Sim"
pilha = Pilha()
lista = ['ovo','a torre da derrota','rodolfo','ame o poema',"qualquerpalavras",'renner']
print('Palavras | Palindromo?')
for i in range(len(lista)):
    print(f"{lista[i]}, {palindromo(lista[i])}")