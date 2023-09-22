
arq = open('arquivos/agendatelefone.txt','r')
agenda = arq.read()
arq.close()
cont = input('Contato que deseja buscar: ')
agenda = agenda.split('\n')
print('Contato  |  Numero')
for i in agenda:
    if i != '':
        cnt, num = i.replace('\n','').split(',')
        if cont == cnt:
            print(f'{cnt:>7}  |  {num}')