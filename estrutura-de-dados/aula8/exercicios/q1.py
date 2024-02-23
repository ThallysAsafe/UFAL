# 1. Uma palavra ou frase é um palíndromo quando
# pode ser lida de trás pra frente mantendo o
# mesmo sentido. Exemplos de palavras são “ovo”,
# “radar”, “reviver”. Exemplos de frases são “A base
# do teto desaba”, “A dama admirou o rim da
# amada”.
# Faça um programa que recebe uma palavra ou
# frase e responda se ela é um palíndromo ou não.

class Celula:
    palavras = None
    proximo = None

    def __init__(self,palavras):
        self.palavras = palavras 

class Pilha:
    topo = None
    def __init__(self):
        self.topo = None

    def inserir(self,palavras):
        c = Celula(palavras)
        c.proximo = self.topo
        self.topo = c
    l
    def palindromo(self):
        aux = self.topo
        
        while aux != None:
            palindromos = aux.palavras.replace(" ", "").lower() # utilizamos o replace para auxilixar na verificação, ele retira os espaços presentes dentro da string
            i, j = 0 , (len(palindromos)-1)
            cond = True
            while i < len(palindromos):
                if palindromos[i] != palindromos[j]:
                    cond = False
                j -= 1
                i += 1
            if cond:
                print(f"{aux.palavras} é um Palíndromo")
            else:
                print(f"{aux.palavras} não é Palíndromo")
            aux = aux.proximo

    def remover(self):
        self.topo = self.topo.proximo

p1 = Pilha()
p1.inserir("A Torre da derrota")
p1.inserir("reviver")
p1.inserir("ovo")
p1.inserir("radar")
p1.inserir("A dama admirou o rim da amada")
p1.palindromo()