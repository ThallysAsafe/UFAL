# 5. Implemente uma função que simula a
# navegação de páginas em um navegador web
# onde o usuário possa retornar a páginas
# anteriores mantendo a ordem inversa de visita.
# Utilize uma pilha encadeada para resolver o
# problema.

class Cell:
    url = None
    proximo = None

    def __init__(self,url):
        self.url = url

class Pilha:
    topo = None

    def __init__(self):
        self.topo = None

    def inserir(self,url):
        c = Cell(url)
        c.proximo = self.topo
        self.topo = c
    
    def voltarpagina(self):
        print("voltando pagina")
        if self.topo != None:
            self.topo = self.topo.proximo
    
    def imprimir(self):
        aux = self.topo
        lista = []
        while aux != None:
            lista.append(aux.url)
            aux = aux.proximo
        for i in range(len(lista)-1,-1,-1):
            print(lista[i], end= '')
        print()
        
url = Pilha()
url.inserir('localhost:3000/')
url.inserir('produtos/')
url.inserir('4567456/')
url.inserir("color='blue'/")
url.imprimir()
url.voltarpagina()
url.imprimir()
url.voltarpagina()
url.imprimir()
