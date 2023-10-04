MAX_ALUNOS = 1000
turma = 1
alunos = []
n = int(input())

while n > 0:
    for _ in range(n):
        codigo, media = map(int, input().split())
        alunos.append({'codigo': codigo, 'media': media})

    indice_melhor = 0
    for i in range(1, n):
        if alunos[i]['media'] > alunos[indice_melhor]['media']:
            indice_melhor = i

    print(f'Turma {turma}')
    print(alunos[indice_melhor]['codigo'])
    print()

