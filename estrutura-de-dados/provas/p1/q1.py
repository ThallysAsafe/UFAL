# 1. Você está implementando uma agenda telefônica. Um contato tem nome e telefone. Esta agenda
# tem uma função de inserir novo contato que, caso o contato não exista, ela insere o novo contato. Caso o
# contato já exista, ele deve ser substituído pelo novo contato. Não podem haver dois contatos com mesmo
# nome na lista. Implemente um algoritmo em Python que recebe uma lista de contatos (com nome e
# telefone) e insira um a um na agenda


lista_add_contatos = [['Icaro', 1243],['Joana',1234],['Ana', 123]]
lista = [['Icaro', 1243],['Joana',1234]]
def contato(lista_add_contatos, lista, i=0, j=0):
    if i > len(lista_add_contatos)-1:
        return agenda(lista_add_contatos, lista, ex=1)
    if lista_add_contatos[i][0] == lista[j][0]:
        lista.pop(j)
        lista.insert(j,lista_add_contatos[i])
        lista.sort()
        print(f'Contato: {lista_add_contatos[i]}, adicionado com sucesso')
        print(lista)
        return contato(lista_add_contatos,lista,i+1, j)
    elif lista_add_contatos[i][0] != lista[j][0]:
        if j >= len(lista) -1:
            lista.append(lista_add_contatos[i])
            lista.sort()
            print(f'Contato: {lista_add_contatos[i]}, adicionado com sucesso')
            print(lista)
            return contato(lista_add_contatos,lista,i+1, j)
        return contato(lista_add_contatos,lista,i, j+1)

def agenda(lista_add_contatos, lista, ex=0):
    
    i = 0
    if i < ex:
        print('Atualização Final da lista:')
        return print(lista)
    lista_add_contatos.sort()
    return contato(lista_add_contatos, lista, i=0, j=0)

agenda(lista_add_contatos, lista, ex=0)