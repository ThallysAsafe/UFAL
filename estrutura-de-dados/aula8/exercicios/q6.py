# 6. Implemente uma pilha para armazenar
# números e escreva uma função para ordenar os
# valores da pilha em ordem crescente. Você pode
# utilizar uma pilha auxiliar para resolver o
# problema, mas não pode utilizar outro tipo de
# estrutura de dados.

class Celula:
    valor = None
    proximo = None

    def __init__(self,valor):
        self.valor = valor

class Pilha:
    topo = None

    def __init__(self):
        self.topo = None

    def inserir(self,valor):
        c = Celula(valor)
        c.proximo = self.topo
        self.topo = c

    def remover(self):
        if self.topo != None:
            aux = self.topo.valor
            self.topo = self.topo.proximo
            return aux
    def imprimir(self):
        aux = self.topo
        lista = []
        while aux != None:

            lista.append(aux.valor)
            aux = aux.proximo
        
        for i in range(len(lista)-1,-1,-1):
            print(lista[i], end=' ')
    def empty(self):
        return self.topo == None
torres = {
    'Pilha Desordenada': Pilha(),
    'Pilha Temporaria': Pilha(),
    'Pilha Resultado': Pilha()
}
lista = [1,4,53,352,63,2,3]
for valores in lista:
    torres['Pilha Desordenada'].inserir(valores)
while torres['Pilha Desordenada'].empty() == False or torres['Pilha Temporaria'].empty() == False:
    menor = float('inf')
    aux = torres['Pilha Desordenada'].topo.valor
    while torres['Pilha Desordenada'].empty() == False and aux != None:
        aux = torres['Pilha Desordenada'].remover()

        if aux < menor:
            menor = aux

        torres['Pilha Temporaria'].inserir(aux)
        
    torres['Pilha Resultado'].inserir(menor)
    while  torres['Pilha Temporaria'].empty() == False :
        aux = torres['Pilha Temporaria'].remover()

        if aux != menor:
            torres['Pilha Desordenada'].inserir(aux)
torres['Pilha Resultado'].imprimir()