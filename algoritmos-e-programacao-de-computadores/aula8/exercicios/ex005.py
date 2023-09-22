# 5. Implemente uma agenda telefônica onde o usuário pode inserir, remover, editar e buscar por telefones de contatos. Cada contato tem um nome e apenas um telefone. Utilize um arquivo para servir como banco de dados da aplicação.
from time import sleep
def lerAgenda():
    arq = open('arquivos/agendatelefone.txt')
    agenda = arq.read()
    arq.close()
    return agenda

def inserir():
    c = 'S'
    lis = []
    agenda = lerAgenda()
    agenda = agenda.split('\n')
    if agenda[-1] != '':
        condicao = True
    while c == 'S':
        lis.append(input('Contato: '))
        lis.append(input('Numero: '))
        c = input('Deseja continuar: [S/N]').upper()
    arq = open('arquivos/agendatelefone.txt','a')
    for i in range(0,len(lis)-1):
        if condicao == True:
            arq.write('\n')
            condicao = False
        if i % 2 == 0 and i == len(lis)-2:
            arq.write(f'{lis[i]},{lis[i+1]}')
        elif i % 2 == 0:
            arq.write(f'{lis[i]},{lis[i+1]}'+'\n') 
    arq.close()
    

def remover():
    agenda = lerAgenda()
    agenda = agenda.split('\n')
    c = "S"
    while c == 'S':
        print('Contatos  |  Numeros')
        for i in agenda:
            if i != '':
                cont, num = i.replace('\n','').split(',')
                print(f'{cont:>7}  |  {num}')
        remov = input('Digite o Nome do contato que deseja remover da lista: ')
        lis = []
        for i in agenda:
            cont, num = i.replace('\n','').split(',')
            if cont != remov:
                lis.append(cont)
                lis.append(num)
        c = input('Deseja remover outro contato? [S/N]').upper()
    arq = open('arquivos/agendatelefone.txt','w')
    for i in range(0,len(lis)-1):
        if i % 2 == 0 and i == len(lis)-2:
            arq.write(f'{lis[i]},{lis[i+1]}')
        elif i % 2 == 0:
            arq.write(f'{lis[i]},{lis[i+1]}'+'\n')            
    arq.close()

def editar():
    agenda = lerAgenda()
    agenda = agenda.split('\n')
    c = 'S'
    while c == "S":
        print('Contatos  |  Numeros')
        for i in agenda:
            a = i.replace('\n','').split(',')
            if a != '':
                print(f'{a[0]:>7}  |  {a[1]}')
        edit = input('Digite o nome do contato que deseja altualizar: ')
        print("Caso não queria alterar determinada parte repita exatamente como está na agenda")
        arq = open('arquivos/agendatelefone.txt','w')
        lis = []
        for i in agenda:
            contato, numero = i.replace('\n','').split(',')
            lis.append(contato)
            lis.append(numero)
            if edit == contato:
                p = lis.index(contato)
                lis[p]= (input('NovoNome: '))
                lis[p+1]= (input('NovoNumero: '))
        c = input('Deseja atualizar outro contato? [S/N]').upper()
    for i in range(0,len(lis)-1):
        if i % 2 == 0 and i == len(lis)-2:
            arq.write(f'{lis[i]},{lis[i+1]}')
        elif i % 2 == 0:
            arq.write(f'{lis[i]},{lis[i+1]}'+'\n')            
    arq.close()

def buscar():
    agenda = lerAgenda()
    cont = input('Contato que deseja buscar: ')
    agenda = agenda.split('\n')
    print('Contato  |  Numero')
    for i in agenda:
        if i != '':
            cnt, num = i.replace('\n','').split(',')
            if cont == cnt:
                print(f'{cnt:>7}  |  {num}')

opc = 1

while opc != 5:
    print("""AGENDA TELEFONICA
----------------------
1-Inserir Contato
2-Remover Contato
3-Editar Contato
4-Buscar Contato
5-Sair
----------------------""")
    opc = int(input('Escolha uma das opções: '))
    if opc == 1:
        inserir()
    elif opc == 2:
        remover()
    elif opc == 3:
        editar()
    elif opc == 4:
        buscar()
    elif opc == 5:
        print('Finalizando programa...')
        sleep(1)
        print('Programa finalizado com sucesso!')



# def exibirAgenda():
#     agenda = lerAgenda()
#     for i in agenda:
#         i = i.replace('\n','').split(', ')
#         print(i)