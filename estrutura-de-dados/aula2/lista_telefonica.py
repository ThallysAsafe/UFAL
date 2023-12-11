agenda_telefonica= [
    ['ana', {'telefone': '982','email': 'ana@gmail.com'}], 
    ['carlao', {'telefone': '69','email': 'carlao@gmail.com'}], 
    ['joao', {'telefone': '9822','email': 'jao@gmail.com'}],
    ['ricardao', {'telefone': 82,'email': 'ricardao@gmail.com'}],
    ['yudi', {'telefone': '4002-8922','email': 'yudi@gmail.com'}]]
contato = 'yudi@gmail.com'
def busca_telefonica(contato, agenda_telefonica):
    media = len(agenda_telefonica)//2
    if len(agenda_telefonica) == 0:
        return False
    if agenda_telefonica[media][1]['email'] == contato:
        return contato
    elif contato > agenda_telefonica[media][1]['email']:
        return busca_telefonica(contato,agenda_telefonica[media+1:])
    else:
        return busca_telefonica(contato,agenda_telefonica[:media])
print(busca_telefonica(contato,agenda_telefonica))