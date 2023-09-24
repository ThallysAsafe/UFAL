a = [["TP","CP","BP","KP","RP","BP","CP","TP"],
    ["PP","PP","PP","PP","PP","PP","PP","PP"],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["PB","  ","  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["  ","PB","PB","PB","PB","PB","PB","PB"],
    ["TB","CB","BB","KB","RB","BB","CB","TB"]
]
posi = 3
posj = 0

pi = 1
pj = 0
i = pi
j = pj

def movimento_rei_valido(posI,posJ,posTempI,posTempJ):
    dx = abs(posI-posTempI)
    dy = abs(posJ-posTempJ)

    if dx <= 1 and dy <= 1 and posI  != posTempI and posJ != posTempJ:
        return "Movimento válido do rei."
    else:
        return "Movimento inválido do rei."

# Exemplo de uso
posI = 2
posJ = 2

posTempI=3
posTempJ=3

resultado = movimento_rei_valido(posI,posJ,posTempI,posTempJ)
print(resultado)

def is_check(peca,tabuleiro):
    if peca[1] == 'B':
        for linha in range(8):
            for coluna in range(8):
                if a[linha][coluna] == 'KB':
                    posI =  linha
                    posJ = coluna
                
        # horizontal 
        for j in range(len(a)):
            if posJ > 1 and posJ < 7:
                if a[posI][posJ-1][1] != 'B' and a[posI][posJ+1][1] != 'B':
                    if a[posI][j] == 'TP' or a[posI][j] == 'RP':
                        return True
                   
            elif posJ == 0:
                if a[posI][posJ+1][1] != 'B':
                    if a[posI][j] == 'TP' or a[posI][j] == 'RP':
                        return True
                   
            elif posJ == 7:
                if a[posI][posJ-1][1] != 'P':
                    if a[posI][j] == 'TP' or a[posI][j] == 'RP':
                        return True
                   
        
        # Vertical BRANCO
        for i in range(len(a)):
            if posI > 1 and posI < 7:
                if a[posI-1][posJ][1] != 'B' and a[posI+1][posJ][1] != 'B':
                    if a[i][posJ] == 'TP' or a[i][posJ] == 'TP':
                        return True
                   
            elif posI == 0:
                if a[posI+1][posJ][1] != 'B':
                    if a[i][posJ] == 'TP' or a[i][posJ] == 'RP':
                        return True
                   
            elif posJ == 7:
                if a[posI][posJ-1][1] != 'B':
                    if a[posI][j] == 'TP' or a[posI][j] == 'RP':
                        return True
                   
    elif peca[1] == 'P':
        for linha in range(8):
            for coluna in range(8):
                if a[linha][coluna] == 'KP':
                    posI =  linha
                    posJ = coluna
                
        # horizontal Preto
        for j in range(len(a)):
            if posJ > 1 and posJ < 7:
                if a[posI][posJ-1][1] != 'P' and a[posI][posJ+1][1] != 'P':
                    if a[posI][j] == 'TB' or a[posI][j] == 'RB':
                        return True
                   
            elif posJ == 0:
                if a[posI][posJ+1][1] != 'P':
                    if a[posI][j] == 'TB' or a[posI][j] == 'RB':
                        return True
                   
            elif posJ == 7:
                if a[posI][posJ-1][1] != 'P':
                    if a[posI][j] == 'TB' or a[posI][j] == 'RB':
                        return True
                   

        # Vertical Preto
        for i in range(len(a)):
            if posI > 1 and posI < 7:
                if a[posI-1][posJ][1] != 'P' and a[posI+1][posJ][1] != 'P':
                    if a[i][posJ] == 'TB' or a[i][posJ] == 'RB':
                        return True
                   
            elif posI == 0:
                if a[posI+1][posJ][1] != 'P':
                    if a[i][posJ] == 'TB' or a[i][posJ] == 'RB':
                        return True
                   
            elif posJ == 7:
                if a[posI][posJ-1][1] != 'B':
                    if a[posI][j] == 'TB' or a[posI][j] == 'RB':
                        return True
                         
    return False

    
            





'''
cont = 0
# Movimento peao Preto
while cont < (posTempI - posI):
    i += 1
    if a[i][j] != '  ':
      # return False
      print(False)
    cont += 1
# Movimento peao Branco    
while cont < (posI - posTempI):
            posI -= 1
            if tabuleiro[posI][posJ] != '  ':
            # return False
                print(False)
'''



# Verificando movimento  do Rainha
'''i = pi
j = pj
cont = 0
if (pi == posi and pj != posj) or (pi != posi and pj == posj):
    # Herdando poder TORRE
    def Torre()
    if posi != pi:
        # vertical
        for i in range(len(a)):
            if a[i][pj] != '  ':
                if a[i][pj][1] == a[pi][pj][1]:
                    print(False)
                else:
                    # MATAR
                    print(False)
    elif posj != pj:
        # horizontal
        for i in range(len(a)):
            if a[pi][i] != '  ':
                if a[i][pj][1] == a[pi][pj][1]:
                    print(False)
                else:
                    # MATAR
                    print(False)
else:
    herdando poder bispo
    def Bispo 
    if pi > posi:
        if pj > posj:
            while cont < (pj - posj):
                j -= 1
                i -= 1
                if a[i][j] != '  ':
                    if a[i][pj][1] == a[pi][pj][1]:
                        print(False)
                    else:
                        # MATAR
                        print(False)
                cont += 1
        else:
            while cont < (posj - pj):
                j += 1
                i -= 1
                if a[i][j] != '  ':
                    if a[i][pj][1] == a[pi][pj][1]:
                        print(False)
                    else:
                        # MATAR
                        print(False)
                cont += 1
    else:
        if pj > posj:
            while cont < (posj - pj):
                j -= 1
                i += 1
                if a[i][j] != '  ':
                    if a[i][pj][1] == a[pi][pj][1]:
                        print(False)
                    else:
                        # MATAR
                        print(False)
                cont += 1
        else:
            while cont < (pj - posj):
                j += 1
                i += 1
                if a[i][j] != '  ':
                    if a[i][pj][1] == a[pi][pj][1]:
                        print(False)
                    else:
                        # MATAR
                        print(False)
                cont += 1
'''













# Verificando movimento de bispo
"""i = pi
j = pj
cont = 0

if pi > posi:
    if pj > posj:
        while cont < (pj - posj):
            j -= 1
            i -= 1
            if a[i][j] != '  ':
                print(False)
            cont += 1
    else:
        while cont < (posj - pj):
            j += 1
            i -= 1
            if a[i][j] != '  ':
                print(False)
            cont += 1
else:
    if pj > posj:
        while cont < (posj - pj):
            j -= 1
            i += 1
            if a[i][j] != '  ':
                print(False)
            cont += 1
    else:
        while cont < (pj - posj):
            j += 1
            i += 1
            if a[i][j] != '  ':
                print(False)
            cont += 1
"""




# Verificador de Movimento da Torre
'''if (pi == posi and pj != posj) or (pi != posi and pj == posj):
    if posi != pi:
        # vertical
        for i in range(len(a)):
            if a[i][pj] != '  ':
                print(False)
    elif posj != pj:
        # horizontal
        for i in range(len(a)):
            if a[pi][i] != '  ':
                print(False)'''
    