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
        i = 1
        while aux != None:
            print(f"{aux.cliente}",end=" ")
            aux = aux.proximo
            i += 1
    
    def imprimirFila(self):
        
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
        
class Banco:
    fila = Fila()
    historicoDia = Fila()
    caixa01 = Fila()
    caixa02 = Fila()
    caixa03 = Fila() 
    def verSituacao(self):
        self.fila.imprimirFila()
        print("-------------------")
        print("Caixa-01:",end=" ")
        self.caixa01.imprimirCaixa()
        print("\nCaixa-02:",end=" ")
        self.caixa02.imprimirCaixa()
        print("\nCaixa-03:",end=" ")
        self.caixa03.imprimirCaixa()
        print("\n-------------------")
        
    def verSituacaoCaixas(self):
        print("-------------------")
        print("Caixa-01:",end=" ")
        self.caixa01.imprimirCaixa()
        print("\nCaixa-02:",end=" ")
        self.caixa02.imprimirCaixa()
        print("\nCaixa-03:",end=" ")
        self.caixa03.imprimirCaixa()
        print("\n-------------------")
    
def banco():    
    banco = Banco()
    print("ALCANBANK")
    while True:
        banco.verSituacao()
        print("""1-Inserir um novo cliente para Fila de atendimento\n2-Inserir cliente no Caixa Vazio\n3-Finalizar Atendimento\n4-Fechar o horario de Atendimento\n5-Encerrar Programa e Mostrar o Histórico de Senhas""")
        op = int(input("Digite qual opção desejada?"))
        if op == 1:
            banco.fila.inserirFila()
            banco.historicoDia.inserir(banco.fila.fim.cliente)
        elif op == 2:
            if not banco.fila.estaVazia():
                if banco.caixa01.estaVazia():
                    banco.caixa01.inserir(banco.fila.inicio.cliente)
                    banco.fila.remover()
                elif banco.caixa02.estaVazia():
                    banco.caixa02.inserir(banco.fila.inicio.cliente)
                    banco.fila.remover()
                elif banco.caixa03.estaVazia():
                    banco.caixa03.inserir(banco.fila.inicio.cliente)
                    banco.fila.remover()
                else:
                    print("É necessario terminar o atendimento de 1 dos caixas para chamar o proximo")
            else:
                print("Não tem mais ninguem na fila de espera, para ser atendido")
        elif op == 3:
            banco.verSituacaoCaixas()      
            liberar = int(input("Digite qual atendimento foi finalizado: "))
            if liberar >= 1 and liberar <= 3:
                if liberar == 1 and not banco.caixa01.estaVazia():
                    banco.caixa01.remover()
                elif liberar == 2 and not banco.caixa02.estaVazia():
                    banco.caixa02.remover()
                elif liberar == 3 and not banco.caixa03.estaVazia():
                    banco.caixa03.remover()
                else:
                    print("Esta Caixa-de-Atendimento está Vazia, chame o proximo da fila")
        elif op == 4:
            banco.fila.cond = False
            print("Horário de Atendimento fechado")
        elif op == 5:
            if banco.fila.estaVazia() and banco.caixa01.estaVazia() and banco.caixa02.estaVazia() and banco.caixa03.estaVazia():
                print("Encerrando Sistema de Atendimento..")
                break    
            else:
                print("Ainda Existe Clientes precisando ser atendidos")
    print(f"Historico do Dia: ")
    banco.historicoDia.imprimirFila()
    print("Sistema Encerrado Com Sucesso!")
banco()