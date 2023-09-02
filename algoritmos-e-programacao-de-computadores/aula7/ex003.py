# # 3. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

# incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
# incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí­lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. ­ ­ 
# excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve serexcluída da agenda.
# excluirNome – essa função exclui uma pessoa da agenda. ­ 

def incluirNovoNome(listaTelefone, nome=''):
    numeros = []
    while numeros == [] or continuar == 'S':
        if nome == '':
            nome = input('Digite o nome do Contato: ')
        numero = input(f'Numero para {nome}: ')
        numeros.append(numero)
        continuar = input('Deseja adicionar mais um numero: [S/N]').upper()
        if continuar == 'N':
            break
        elif continuar != 'S':
            print('Resposta inválida, por favor digite novamente')
    if listaTelefone == {}:
        listaTelefone[nome] = numeros   
    elif listaTelefone[nome] != numeros:
        listaTelefone[nome] += numeros  
    print('Contato adicionado com êxito!')
    return listaTelefone

def incluirTelefone(listaTelefone):
    contador = 1
    nome = input('Em qual contato você quer adicionar um novo numero?: ')
    for contatos in listaTelefone.keys():
        if contatos == nome:
            listaTelefone = incluirNovoNome(listaTelefone,nome)
            return listaTelefone
        else:
            contador += 1
    if contador > len(listaTelefone.keys()) or len(listaTelefone.keys()) == 0:
        adicionarContato = input('Contato Não Existente. Deseja incluir esse Contato? [S/N]').upper()
        if adicionarContato == 'S':
            listaTelefone = incluirNovoNome(listaTelefone,nome)
            return listaTelefone
        elif adicionarContato == 'N':
            return print('Contato não adicionado!')
        else:
            while adicionarContato != 'SN':
                adicionarContato = input('Contato Não Existente. Deseja incluir esse Contato? [S/N]').upper()
                if adicionarContato == 'S':
                    listaTelefone = incluirNovoNome(listaTelefone,nome)
                    return listaTelefone 
                elif adicionarContato == 'N':
                    return print('Contato não adicionado!')

def excluirTelefone(listaTelefone):
    for contato in listaTelefone.keys():
        print(f'{contato}')
    contato = input('Digite o contato que você quer excluir o numero da Agenda: ')
    for contatos in listaTelefone:
        if contato == contatos:
            if len(listaTelefone[contato]) < 2:
                print('Contato excluído com sucesso!') 
                del listaTelefone[contato]
                break
            else:
                for posição, numeros in enumerate(listaTelefone[contato]):
                    print(f'{posição}-{numeros}')
                excluir = int(input(f'''Escolha qual dos numeros deseja excluir: '''))
                if excluir > len(listaTelefone[contato]) or excluir < 0:
                    print('Numero inválido')
                else:
                    del listaTelefone[contato][excluir]
                    print(f'Numero: {listaTelefone[contato][excluir]} excluido com sucesso!')
        else:
            print('Contato inexistente')
    return listaTelefone

def excluirNome(listaTelefone):
    if len(listaTelefone.keys()) > 0:
        for contato in listaTelefone.keys():
            print(f'{contato}')
    contato = input('Digite o contato quer excluir da Agenda: ')
    del listaTelefone[contato]
    
def consultarTelefone(listaTelefone):
    print(listaTelefone)
    if len(listaTelefone.keys()) > 0:
        print('Contatos:')
        for contato in listaTelefone.keys():
            print(f'{contato}')
        contato = input('Digite o contato que deve ser exibido: ')
    else:
        print('Não tem nenhum contato na lista')
    cond = True
    for i in listaTelefone.keys():
        if contato == i:
            cond = False
    if cond == False:
        print("Contato| Numeros:")
        print(f"{contato}: {listaTelefone[contato]}")
    else:
        print('Contato inexistente!')
    return listaTelefone

listaTelefone = {}
while True:
    opção = int(input('''1- Adicionar Novo Contato
2- Adicionar Novo Telefone
3- Excluir Telefone
4- Excluir Contato
5- Consultar Agenda
0- Finalizar Programa
Escolha uma das opções: '''))
    if opção == 0:
        print('Finalizando programa!')
        break
    elif opção == 1:
        listaTelefone = incluirNovoNome(listaTelefone)
    elif opção == 2:
        listaTelefone = incluirTelefone(listaTelefone)
    elif opção == 3:
        listaTelefone = excluirTelefone(listaTelefone)
    elif opção == 4:
        listaTelefone = excluirNome(listaTelefone)
    elif opção == 5:
        listaTelefone = consultarTelefone(listaTelefone)
    else:
        print('Opção inválida')
print('Programa Finalizado com Sucesso!')

print(listaTelefone)