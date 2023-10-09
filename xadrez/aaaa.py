tabuleiro = [["TP","CP","BP","KP","RP","BP","CP","TP"],
            ["PP","PP","  ","PP","PP","PP","PP","PP"],
            ["  ","QP","  ","  ","  ","CP","  ","  "],
            ["  ","  ","  ","PP","  ","  ","  ","  "],
            ["RP","PB","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","MP","  ","  ","  "],
            ["  ","  ","PB","PB","PB","PB","PB","PB"],
            ["TB","CB","BB","TB","RB","BB","CB","KB"]]

for linha in range(8):
    for coluna in range(8):
        if tabuleiro[linha][coluna] == 'KB':
            posI =  linha
            posJ = coluna

if posJ >= 0 and posJ <= 7:
    print(2)
    if posI == 7 and posJ < 7:
        cont = posJ - 1
        i = posI
        j = posJ
        # as diagonais estão sendo feitas com base a coluna q o rei está
        #lado direito
        while cont < 7:
            if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                print(tabuleiro[i][j])
                if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP' or tabuleiro[posI-1][posJ+1] == 'PP':
                    print(False)
                    break
                i -= 1
                j += 1
            else: # caso tenha uma peça protegendo ele imrpimira true
                print(True)
                break
            cont += 1
        cont = posJ + 1
        i = posI
        j = posJ
        # lado esquerdo
        while cont > 0:
            if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                print(tabuleiro[i][j])
                if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP' or tabuleiro[posI-1][posJ-1] == 'PP':
                    print(False)
                    break
                i -= 1
                j -= 1
            else:
                print(tabuleiro[i][j])
                print(True)
                break
            cont -= 1
    elif (posI == 0 and posJ == 7) or (posI == 7 and posJ == 0):
        cont = posJ - 1
        i = posI
        j = posJ
        # as diagonais estão sendo feitas com base a coluna q o rei está
        #lado direito
        while cont < 7:
            if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                print(tabuleiro[i][j])
                if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                    print(False)
                    break
                i += 1
                j += 1
            else: # caso tenha uma peça protegendo ele imrpimira true
                print(True)
                break
            cont += 1
        cont = posJ + 1
        i = posI
        j = posJ
        # lado esquerdo
        while cont > 0:
            if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                print(tabuleiro[i][j])
                if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                    print(False)
                    break
                i += 1
                j -= 1
            else:
                print(tabuleiro[i][j])
                print(True)
                break
            cont -= 1
    elif posI >= 0 and posI <= 7:
        print(3)
        if posJ > 7 and posI <= 7:
            i = posI
            j = posJ
            while i <= 7 and j >= 0:
                if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                    print(tabuleiro[i][j])
                    if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                        print(False)
                        break
                i += 1
                j -= 1
                
            if j == -1:
                print(5)
                while j <= 7 and i <= 7:
                    print(i)
                    if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                        print(tabuleiro[i][j])
                        if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP' or tabuleiro[posI-1][posJ-1] == 'PP' or tabuleiro[posI-1][posJ+1] == 'PP':
                            print(False)
                            break
                        elif tabuleiro[i][j] == 'PP':
                            print(True)
                    i -= 1
                    j += 1
            i = posI
            j = posJ
            while i <= 7 and j >= 0:
                print(1.2)
                if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                    print(tabuleiro[i][j])
                    if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                        print(False)
                        break
                i -= 1
                j -= 1
            if j == -1:
                while j <= 7 and i <= 7:
                    if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                        print(tabuleiro[i][j])
                        if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                            print(False)
                            break
                    i -= 1
                    j += 1
                print(4)
            i = posI
            j = posJ
            while i <= 7 and j >= 0:
                if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                    print(tabuleiro[i][j])
                    if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                        print(False)
                        break
                i += 1
                j -= 1
            if i == 8 or j == -1:
                i -= 1
                j += 1
                while i >= 0 and j <= 7:
                    if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
                        print(tabuleiro[i][j])
                        if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP':
                            print(False)
                            break
                    i -= 1
                    j += 1
        elif posJ > 0 and posI <
        # while i >= 0 and j <= 7:
        #     if tabuleiro[i][j][1] != 'B' or tabuleiro[i][j] == 'KB':
        #         print(tabuleiro[i][j])
        #         if tabuleiro[i][j] == 'RP' or tabuleiro[i][j] == 'BP' or tabuleiro[posI-1][posJ-1] == 'PP':
        #             print(False)
        #             break
        #     elif tabuleiro[i][j][1] == 'P':
        #             print(True)
        #             break     
        #     i -= 1
        #     j += 1

                



# if (posI and posJ) == 0 or (posI and posJ) == 8:
#     for i in range(len(tabuleiro)):
#         for j in range(len(tabuleiro)):
#             if i == j and tabuleiro[i][j] !=:
#                 print(i, j)

# if ((posI == 8 and linha == 0) or (posI == 0 and linha == 8)):

        
            