class Celula:
    letra = None
    proximo = None

    def __init__(self, letra):
        self.letra = letra

class Pilha:
    palavra = None
    topo = None

    def __init__(self):
        self.topo = None

    def inserir(self, palavra):
        self.palavra = palavra
        self.topo = self.soletrar(self.palavra.replace(" ", "").lower())
        self.palindromo(self.palavra)

    def soletrar(self, palavra):
        for letra in palavra:
            c = Celula(letra)
            c.proximo = self.topo
            self.topo = c
        return self.topo

    def palindromo(self, palavra):
        j = 0

        palavras = palavra.replace(" ", "").lower()
        while self.topo != None and j <= len(palavras) - 1:
            if self.topo.letra == palavras[j]:
                self.topo = self.topo.proximo
            j += 1
        if self.topo == None:
            print(f"{palavra} é um Palíndromo")
        else:
            print(f"{palavra} não é um Palíndromo")


p1 = Pilha()
p1.inserir("A torre da derrota")
p1.inserir("reviver")
p1.inserir("Arroz")
