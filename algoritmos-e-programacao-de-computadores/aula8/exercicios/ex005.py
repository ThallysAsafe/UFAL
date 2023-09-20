# 5. Implemente uma agenda telefônica onde o usuário pode inserir, remover, editar e buscar por telefones de contatos. Cada contato tem um nome e apenas um telefone. Utilize um arquivo para servir como banco de dados da aplicação.
caminho = 'arquivos/agendatelefone.txt'
def agenda(caminho):
    arq = open(caminho)
    agenda = arq.read()
    arq.close()
def inserir()
    arq = open(caminho,'a')
    arq.write(input('Nome: '))
    arq.close()
def remover()
def editar()
def buscar()