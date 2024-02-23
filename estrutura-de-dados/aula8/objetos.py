class Usuario:
    nome = ''
    salario = None

    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def reajuste(self,percentual):
        self.salario = self.salario*percentual + self.salario

u1 = Usuario('Thallao',10000)

print(u1.nome,u1.salario)