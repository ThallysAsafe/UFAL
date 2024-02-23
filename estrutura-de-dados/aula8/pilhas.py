
tam= 10
pilha = [None]*tam
fim = 0
def inserir(valor,fim):
    if fim < tam:
        pilha[fim] = valor
        fim+=1
        return fim 
    return "Pilha Cheia"

def remover(fim):
    if fim > 0:
        fim -= 1
        pilha[fim] = None
        return fim
    return "Pilha Vazia"
fim = inserir(5,fim)
print(pilha)


fim = inserir(3,fim)
print(pilha)



fim = inserir(-1,fim)
print(pilha)

fim = inserir(-1,fim)
print(pilha)
fim = inserir(-1,fim)
print(pilha)
fim = inserir(-5,fim)
print(pilha)
fim = inserir(-5,fim)
print(pilha)
fim = inserir(-5,fim)
print(pilha)
fim = inserir(-5,fim)
print(pilha)
fim = inserir(-5,fim)
print(pilha)
fim = inserir(-5,fim)
print(pilha)
fim = remover(fim)
print(pilha)
print(fim)