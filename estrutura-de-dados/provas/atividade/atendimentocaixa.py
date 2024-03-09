class Celula:
    cliente = None
    proximo = None
    def __init__(self,valor):
        self.cliente = valor
        
class Fila:
    inicio = None
    fim = None
    cond = True
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        
    def inserir(self,valor):
        if self.cond:
            c = Celula(valor)
            if self.estaVazia():
                self.inicio = c
            else:
                self.fim.proximo = c
            self.fim = c
        
        
    def remover(self):
        if not self.estaVazia():
            aux = self.inicio
            valor = self.inicio.cliente
            del aux
            self.inicio = self.inicio.proximo
            return valor
        else:
            return None
            
    def estaVazia(self):
        return self.inicio == None

        
    def imprimirCaixa(self):
        aux = self.inicio
        if aux != None:
            return aux.cliente
        else:
            return "Vazia"
    
    def imprimirFila(self):
        print("++=====================================++") 
        aux = self.inicio
        if self.cond or aux != None:
            i = 1
            print("FILA:")
            if aux == None:
                print("Vazia")
            while aux != None:
                print(f"nº{i}: {aux.cliente}")
                aux = aux.proximo
                i += 1
        
    
    def inserirFila(self):
        if self.cond:
            nome = input("Nome do Cliente: ")
            self.inserir(nome)
            print("Cliente Adicionado a Fila de Espera")
        else:
            print("Horário de Atendimento fechado")
        
class Atendente:
    nome = None
    def __init__(self,nome):
        self.nome = nome
        self.caixa = Fila()
class Banco:
    fila = Fila()
    historicoDia = Fila()
    atendente = [None]*3
    def __init__(self):
        for i in range(3):
            nome = input(f"Nome do Atendente do Dia do Caixa-{i+1}: ")
            self.atendente[i] = Atendente(nome)
            
    def verSituacao(self):
        self.fila.imprimirFila()
        self.verSituacaoCaixas()
        
    def verSituacaoCaixas(self):
        print("++=====================================++") 
        print(f"Caixa-01: {self.atendente[0].nome}")
        print(f"Cliente: {self.atendente[0].caixa.imprimirCaixa()}")
        print(f"Caixa-02: {self.atendente[1].nome}")
        print(f"Cliente: {self.atendente[1].caixa.imprimirCaixa()}")
        print(f"Caixa-03: {self.atendente[2].nome}")
        print(f"Cliente: {self.atendente[2].caixa.imprimirCaixa()}")
        print("++=====================================++") 
        

    
     
def banco():
    print("++=====================================++")    
    print("     Sistema de Atendimento do Banco     ")
    print("++=====================================++")    
    banco = Banco()
    while True:
        banco.verSituacao()
        print("""1-Inserir um novo cliente para Fila de atendimento\n2-Inserir cliente no Caixa Vazio\n3-Finalizar Atendimento\n4-Fechar o horario de Atendimento\n5-Encerrar Programa e Mostrar o Histórico de Senhas""")
        op = int(input("Digite qual opção desejada?"))
        if op == 1:
            banco.fila.inserirFila()
            banco.historicoDia.inserir(banco.fila.fim.cliente)
        elif op == 2:
            if not banco.fila.estaVazia():
                if banco.atendente[0].caixa.estaVazia():
                    banco.atendente[0].caixa.inserir(banco.fila.inicio.cliente)
                    banco.fila.remover()
                elif banco.atendente[1].caixa.estaVazia():
                    banco.atendente[1].caixa.inserir(banco.fila.inicio.cliente)
                    banco.fila.remover()
                elif banco.atendente[2].caixa.estaVazia():
                    banco.atendente[2].caixa.inserir(banco.fila.inicio.cliente)
                    banco.fila.remover()
                else:
                    print("É necessario terminar o atendimento de 1 dos caixas para chamar o proximo")
            else:
                print("Não tem mais ninguem na fila de espera, para ser atendido")
        elif op == 3:
            banco.verSituacaoCaixas()      
            liberar = int(input("Digite qual atendimento foi finalizado: "))
            if liberar >= 1 and liberar <= 3:
                if liberar == 1 and not banco.atendente[0].caixa.estaVazia():
                    banco.atendente[0].caixa.remover()
                elif liberar == 2 and not banco.atendente[1].caixa.estaVazia():
                    banco.atendente[1].caixa.remover()
                elif liberar == 3 and not banco.atendente[2].caixa.estaVazia():
                    banco.atendente[2].caixa.remover()
                else:
                    print("Esta Caixa-de-Atendimento está Vazia, chame o proximo da fila")
        elif op == 4:
            banco.fila.cond = False
            print("Horário de Atendimento fechado")
        elif op == 5:
            if banco.fila.estaVazia() and banco.atendente[0].caixa.estaVazia() and banco.atendente[1].caixa.estaVazia() and banco.atendente[2].caixa.estaVazia():
                print("Encerrando Sistema de Atendimento..")
                break    
            else:
                print("Ainda Existe Clientes precisando ser atendidos")
    print(f"Historico do Dia: ")
    banco.historicoDia.imprimirFila()
    print("++=====================================++")
    print("Sistema Encerrado Com Sucesso!")
banco()