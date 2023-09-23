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
    