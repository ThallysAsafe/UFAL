import os
arquivo = open('ips.txt','r')
def ip_validação(arquivo):
    enderecovalido =  []
    enderecoinvalido =  []
    for linha in arquivo.readlines():
        ip = linha.replace('\n','').split('.')
        cond = False
        for i in range(4):
            if int(ip[i]) < 255 and int(ip[i]) > 0:
              cond = True
            else: 
                cond = False
                break
        if cond == True:
            # validos
            enderecovalido.append(linha.replace('\n',''))

        else:
            # Invalidos
            enderecoinvalido.append(linha.replace('\n',''))
    resultado = enderecovalido, enderecoinvalido
    return resultado

def imprimir():
    enderecovalido, enderecoinvalido = ip_validação(arquivo)
    arq = open('resposta.txt','wt')
    if len(enderecovalido) > 0:
        arq.write('[Endereços válidos]:\n')
        for ip in enderecovalido:
            arq.write(ip+'\n')
    if len(enderecoinvalido) > 0:
        arq.write('[Endereços Inválidos]:\n')
        for ip in enderecoinvalido:
            arq.write(ip+'\n')
imprimir()