def bits():
    result = []
    qnt = 1
    cont = 0
    while qnt != 0:
        num = input()
        qnt = int(num)
        num = num.split('\n')
        if qnt != 0:
            cont += 1
            for i in num:
                bits = int(i)
                I = 0
                J = 0
                K = 0
                L = 0
                if i != 0:
                    I = bits // 50
                    bits = bits - (50*I)
                    J =  bits // 10
                    bits = bits - (10*J)
                    K = bits // 5
                    bits = bits - (5*K)
                    L = bits
                    bits = bits - (L)
                    result.append([I,J,K,L])

    for i in range(cont):
        print(f'Teste {i+1}')
        for j in range(4):
            print(result[i][j], end=' ')
        print('\n')
bits()