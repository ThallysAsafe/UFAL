quantidade = int(input())
dic = {}
if quantidade >= 3 and quantidade <= 20:
    for i in range(quantidade):
        personagem = input().split(' ')
        lista = []
        for i in range(1,4):
            lista.append(personagem[i])
        dic[personagem[0]] = lista
    busc = ''
    while busc != 'FIM': 
        busc = input().split(' ')
        if busc[0] != 'FIM':
            if busc[0] in  dic:
                if busc[1] in dic[busc[0]]:
                    print('Uhul! Seu amigo secreto vai adorar')
                else:
                    print('Tente Novamente!')
            else:
                print('Tente Novamente!')
        else:
            break