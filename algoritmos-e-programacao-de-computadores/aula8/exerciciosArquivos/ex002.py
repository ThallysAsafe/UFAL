# 2. Escreva um programa que lê um arquivo contendo endereços IPs, da seguinte forma:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# O programa deve mostrar os IPs indicando os que são válidos e inválidos (um endereço ip válido não pode ter uma de suas partes maior que 255).
caminho = 'arquivos/ip.txt'
def buscArq(caminho):
    arq = open(caminho)
    ips = arq.read()
    arq.close()
    return verificador(ips)
def verificador(ips):
    ips = ips.split('\n')
    for linha in ips:
        condicao = True
        ip = linha.split('.')
        for i in range(0,len(ips)):
            if int(ip[i]) > 255:
                print(f'Ip, {linha} inválido!')
                condicao = False
        if condicao == True:
            print(f'Ip, {linha} válido!')    
buscArq(caminho)       