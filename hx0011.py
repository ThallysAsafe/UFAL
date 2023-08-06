num = int(input())
if (num >= 1 and num <= 40):
    for coluna in range(1, num+1):
        for linha in range(1, coluna+1):
            if (linha<coluna):
                print(linha, end=' ')
            else:
                print(linha, end='')
        print()
    
        
