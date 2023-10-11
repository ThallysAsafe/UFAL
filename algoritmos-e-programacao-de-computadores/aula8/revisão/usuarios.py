# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
caminho = 'usuarios.txt'
def arquivo(caminho):
    arquivo = open(caminho)
    texto = arquivo.read()
    arquivo.close()
    return texto

def usuarios():
    texto = arquivo(caminho)
    texto = texto.replace(' ','\n').split('\n')
    usuariosInter = []
    for i in range(len(texto)):
        if texto[i] != '':
            usuariosInter.append(texto[i])
    soma = 0
    espacoMB = []
    usuarios = []
    for i in range(len(usuariosInter)):
        if i % 2 != 0:
            espacoMB.append(int(usuariosInter[i])/(1024**2))
        else:
            usuarios.append(usuariosInter[i])
    for i in range(len(espacoMB)):
            soma += espacoMB[i]
    porcentagem_Uso = []
    for i in range(len(espacoMB)):
        porcentagem_Uso.append((espacoMB[i]/soma) * 100)
    espaco_medio = soma/len(espacoMB)

    arq = open('relatorio.txt','w')
    if len(usuariosInter) > 0:
        arq.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        arq.write("------------------------------------------------------------------------\n")
        arq.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
        for i in range(len(usuarios)):
            arq.write(f"{i:<4} {usuarios[i]:<15} {espacoMB[i]:>10.2f} MB {porcentagem_Uso[i]:>15.2f}%\n")
        arq.write(f'Espaço total ocupado: {soma} MB\n')
        arq.write(f'Espaço medio ocupado: {espaco_medio} MB\n')
print(usuarios())