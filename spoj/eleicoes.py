
def função():
    qnt = 1
    candidatos = {}
    qnt = int(input())
    if qnt >= 1 and qnt <= 100000:
        candi = int(input().split('\n'))
        for i in range(qnt):
            if candi not in candidatos.keys() and candi > 1 and candi <= 1000000000:
                candidatos[candi] = 0
            elif candi > 1 and candi <= 1000000000:
                candidatos[candi] += 1
    maior = candidatos[candi]
    result = candi
    for key, value in candidatos.items():
        if value > maior:
            maior = value
            result = key
    print(result)
função()