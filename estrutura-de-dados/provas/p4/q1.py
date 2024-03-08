class Celula:
    valor = None
    proximo = None
    def __init__(self, valor):
        self.valor = valor

class Pilha:
    topo = None
    mapa = {')':'(','}':'{',']':'['}
    def __init__(self):
        self.topo = None


    def inserir(self,valor):
        c = Celula(valor)
        c.proximo = self.topo
        self.topo = c
    def remover(self):
        if self.topo != None:
            self.topo = self.topo.proximo
    
        
def verificador(expressao):
    pilha = Pilha()
    for caracter in expressao:
        if caracter in '[({})]':
            if caracter in '[{(':
                pilha.inserir(caracter)
            else:
                if  pilha.topo != None and pilha.topo.valor == pilha.mapa[caracter]:
                    pilha.remover()
                else:
                    return 'Não'

    if pilha.topo == None:
        return "Sim"
    return 'Não'
        

print('Expressão | é correta?')
lista = ['(1 + 2) + (3 + 4)','(','{(())}','{[(()])}','[[[[][][][)()()()))]]]]']
for i in range(len(lista)):
    print(lista[i], verificador(lista[i]))