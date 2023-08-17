'''5. Um professor teve uma ideia de como avaliar seus alunos em uma atividade que vale entre 0 e 10 de modo a incentivar a competição entre os alunos. Quem tirar a maior nota terá 10. Quem tirar a menor nota, terá 0. As outras notas serão algo entre 0 e 10 da seguinte forma:
Nota = ((nota-min)/(max – min))*10
Faça um programa para calcular as notas dos alunos segundo essa regra, utilizando funções'''
notas = [5,1,2,7,9,10]
nota_aluno = []
def notas_geral(notas):
    maior = menor = notas[0]
    for numero in notas:
        if numero > maior:
            maior = numero 
        if numero < menor:
            menor = numero
        if numero > 10 or numero < 0:
            notas.remove(numero)
    for numero in notas:
        if numero == maior:
            nota_aluno.append(10)
        elif numero == menor:
            nota_aluno.append(0)
        else:
            nota_aluno.append(((numero-menor)/(maior-menor))*10)     
    return nota_aluno
for pos, notas in enumerate(notas_geral(notas)):
    print(f'Aluno {pos}: {notas:.2f}')
