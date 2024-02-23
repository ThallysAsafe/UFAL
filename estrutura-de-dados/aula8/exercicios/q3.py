# 3 . Uma expressão aritmética com parênteses, colchetes
# e chaves é dita bem formada se estes símbolos são
# fechados na ordem inversa que são abertos.
# ● Ex: expressão bem formada
# – 3-[15+2*(4-3)*[2+(5-1)]]/4
# ● Ex: expressão mal formada
# – 5-[4+(0-3]
# ● Faça um algoritmo para resolver o problema usando
# pilhas

class Celula:
    valor = None
    proximo = None
    def __init__(self,valor):
        self.valor = valor


class Pilha:
    topo = None
    mapa = {')': '(', '}':'{', ']': '['}
    expressaoRuim = True
    def __init__(self):
        self.topo = None
    
    def inserir(self,valor):
        for caracter in valor:
            if caracter in ')]}{[(':
                if caracter in '{[(':
                    c = Celula(caracter)
                    c.proximo = self.topo
                    self.topo = c
                else: 
                    inverso = self.mapa[caracter]
                    if inverso == self.topo.valor:
                        self.topo = c.proximo
                    else:
                        return self.expressaoRuim
        if self.topo == None:
            return False
    def imprimir(self):
        aux = self.topo
        while aux != None:
            print(aux.valor)
            aux = aux.proximo
        print("------")
lista = []
expressao = input()

verificador = Pilha()
verificador.inserir(expressao)
if verificador.inserir(expressao):
    print("expressão ruim")
else:
    print("Essa é da boa")  
