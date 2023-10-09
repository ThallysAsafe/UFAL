# Xadrez tem um tabuleiro de 8x8
# potuação
# 

from colorama import Fore, Back, Style, init

init()

# print(f"{Back.YELLOW}{Fore.BLACK}Texto com fundo amarelo{Style.RESET_ALL}")

def imprimir(tabulerio, round):
    if round != 0:
        print(f"\n{round}º round:")
    for i in range(len(tabuleiro)):
        print(f"{i+1}",end=" ")
        for j in range(len(tabuleiro[0])):
            if ((i+1)+(j+1)) % 2 == 0:
                print(f"{Fore.WHITE}{Back.BLACK} {tabuleiro[i][j]}",end=" ")
            else:
                print(f"{Fore.BLACK}{Back.WHITE} {tabuleiro[i][j]}",end=" ")
        print(f"{Style.RESET_ALL}")
    print("   a   b   c   d   e   f   g   h ")
    print()

def calculandoColuna(j):
    letras = "abcdefgh"
    for i in range(len(letras)):
        if letras[i] == j:
            j = i 
            return j
    return None

def andar(posI, posJ, posTempI, posTempJ, peca, tabuleiro, cond=False):
    if tabuleiro[posTempI][posTempJ][1] == peca[1]:
        return False
    elif tabuleiro[posTempI][posTempJ] == "  ":
        print(f"A {peca} andou para a posicao desejada.")
        tabuleiro[posTempI][posTempJ] == tabuleiro[posI][posJ]
        tabuleiro[posI][posJ] = '  '
        return True
    else:
        print(f"A {peca} matou a {tabuleiro[posTempI][posTempJ]}.")
        #add pontuação
        return True

def peao(posI, posJ, posTempI, posTempJ, peca, tabuleiro):
    if peca[1] == "P" and posI == 1:
        retorno = andar(posI, posJ, posTempI, posTempJ, peca, tabuleiro, cond=True)
        cont = 0
        while cont < (posTempI - posI):
            posI += 1
            if tabuleiro[posI][posJ] != '  ':
            # return False
                print(False)
    elif peca[1] == "B" and posI == 6:
        retorno = andar(posI, posJ, posTempI, posTempJ, peca, tabuleiro, cond=True)
        cont = 0
        while cont < (posI - posTempI):
            posI -= 1
            if tabuleiro[posI][posJ] != '  ':
            # return False
                print(False)
    elif peca[1] == "P":
        retorno = andar(posI, posJ, posTempI, posTempJ, peca, tabuleiro)
    elif peca[1] == "B":
        retorno = andar(posI, posJ, posTempI, posTempJ, peca, tabuleiro)
    return retorno

def torre(posI, posJ, posTempI, posTempJ, peca, tabuleiro):
    return

def cavalo(posI, posJ, posTempI, posTempJ, peca, tabuleiro):
    return

def bispo(posI, posJ, posTempI, posTempJ, peca, tabuleiro):
    return

def rainha(posI, posJ, posTempI, posTempJ, peca, tabuleiro):
    return

def rei(posI, posJ, posTempI, posTempJ, peca, tabuleiro):
    return

tabuleiro = [
    ["TP","CP","BP","KP","RP","BP","CP","TP"],
    ["PP","PP","PP","PP","PP","PP","PP","PP"],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["  ","  ","  ","  ","  ","  ","  ","  "],
    ["PB","PB","PB","PB","PB","PB","PB","PB"],
    ["TB","CB","BB","KB","RB","BB","CB","TB"]
]

# tabuleiro = [
#     ["2", "3", "4", "5", "6", "7", "8", "9"],
#     ["3", "4", "5", "6", "7", "8", "9","10"],
#     ["4", "5", "6", "7", "8", "9","10","11"],
#     ["5", "6", "7", "8", "9","10","11","12"],
#     ["6", "7", "8", "9","10","11","12","13"],
#     ["7", "8", "9","10","11","12","13","14"],
#     ["8", "9","10","11","12","13","14","15"],
#     ["9","10","11","12","13","14","15","16"]
# ]

def jogo():
    print("\n--------Tabuleiro-Xadrex--------\n")
    round = 0
    ganhador = 0 
    
    while ganhador == 0:
        imprimir(tabuleiro, round)
        retorno = posI = posTempI = posJ = posTempJ = 0
        while (posI == posTempI and posJ == posTempJ) or retorno == 0:
            if round % 2 == 0:
                try:
                    posI = int(input("Jogador Branco, digite o número da linha da peça que desejas mover: ")) -1
                except ValueError:
                    posI = -1
                while posI > 7 or posI < 0:
                    print("Você digitou um valor inválido, tente novamente!")
                    try:
                        posI = int(input("Jogador Branco, digite o número da linha da peça que desejas mover: ")) -1
                    except ValueError:
                        posI = -1

                posJ = input("Jogador Branco, digite a letra da coluna da peça que desejas mover: ")
                posJ = calculandoColuna(posJ)
                while posJ == None:
                    print("Você digitou um valor inválido, tente novamente!")
                    posJ = input("Jogador Branco, digite a letra da coluna para onde desejas se mover: ")  
                    posJ = calculandoColuna(posJ)
                
                try:
                    posTempI = int(input("Jogador Branco, digite o número da linha para onde desejas se mover: "))-1
                except ValueError:
                        posI = -1
                while posTempI > 7 or posTempI < 0:
                    print("Você digitou um valor inválido, tente novamente!")
                    try:
                        posTempI = int(input("Jogador Branco, digite o número da linha para onde desejas se mover: "))-1 
                    except ValueError:
                        posI = -1

                posTempJ = input("Jogador Branco, digite a letra da coluna para onde desejas se mover: ")
                posTempJ = calculandoColuna(posTempJ)
                while posTempJ == None:
                    print("Você digitou um valor inválido, tente novamente!")
                    posTempJ = input("Jogador Preto, digite a letra da coluna para onde desejas se mover: ") 
                    posTempJ = calculandoColuna(posTempJ)
            else:
                try:
                    posI = int(input("Jogador Preto, digite o número da linha da peça que desejas mover: ")) -1
                except ValueError:
                    posI = -1
                while posI > 7 or posI < 0:
                    print("Você digitou um valor inválido, tente novamente!")
                    try:
                        posI = int(input("Jogador Preto, digite o número da linha da peça que desejas mover: ")) -1
                    except ValueError:
                        posI = -1

                posJ = input("Jogador Preto, digite a letra da coluna da peça que desejas mover: ")
                posJ = calculandoColuna(posJ)
                while posJ == None:
                    print("Você digitou um valor inválido, tente novamente!")
                    posJ = input("Jogador Preto, digite a letra da coluna para onde desejas se mover: ") 
                    posJ = calculandoColuna(posJ)
                    
                try:
                    posTempI = int(input("Jogador Preto, digite o número da linha para onde desejas se mover: "))-1
                except ValueError:
                    posI = -1
                while posTempI > 7 or posTempI < 0:
                    print("Você digitou um valor inválido, tente novamente!")
                    try:
                        posTempI = int(input("Jogador Preto, digite o número da linha para onde desejas se mover: "))-1
                    except ValueError:
                        posI = -1
                        
                posTempJ = input("Jogador Preto, digite a letra da coluna para onde desejas se mover: ")
                posTempJ = calculandoColuna(posTempJ)
                while posTempJ == None:
                    print("Você digitou um valor inválido, tente novamente!")
                    posTempJ = input("Jogador Preto, digite a letra da coluna para onde desejas se mover: ")  
                    posTempJ = calculandoColuna(posTempJ)

    print(posJ, posI, posTempJ, posTempI)
    
    round += 1
    ganhador = 3

    if ganhador == 1:
        print("O jogador das peças Brancas ganhou!")
    elif ganhador == 2:
        print("O jogador das peças Pretas ganhou!")
    elif ganhador == 3:
            print("Houve um Empate")
jogo()