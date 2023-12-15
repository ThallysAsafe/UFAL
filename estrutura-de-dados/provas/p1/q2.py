# 2. Você está implementando um sistema de busca em um banco de dados. Esse sistema possui uma
# base de dados de alunos de toda a rede de educação. Cada aluno tem nome, número de matrícula e data
# de nascimento. A base é mantida ordenada em ordem alfabética pelo nome do aluno. Implemente uma
# função de busca eficiente para esse sistema.

Aluno = {'nome': 'Anderson','numero-matricula':'212423','nasc':'01/05/2003'}

Banco_Dados= [
{'nome': 'Anderson','numero-matricula':'212423','nasc':'01/05/2003'},
{'nome': 'Chico','numero-matricula':'212424','nasc':'08/02/2000'},
{'nome': 'Jonatas','numero-matricula':'212425','nasc':'18/05/2002'},
{'nome': 'Rayane','numero-matricula':'212426','nasc':'08/03/2005'},
{'nome': 'Thallão','numero-matricula':'212427','nasc':'08/05/2005'}]

def Busca_Banc(Banco_Dados, Aluno):
    media = len(Banco_Dados)//2
    if Banco_Dados[media]['nome'] == Aluno['nome']:
        return Banco_Dados[media]
    elif Banco_Dados[media]['nome'] > Aluno['nome']:
        return Busca_Banc(Banco_Dados[:media],Aluno)
    elif Banco_Dados[media]['nome'] < Aluno['nome']:
        return Busca_Banc(Banco_Dados[media+1:],Aluno)
    else:
        return False
print(Busca_Banc(Banco_Dados,Aluno))