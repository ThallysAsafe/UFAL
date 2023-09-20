def inicio(name):
    print(f'Seja bem-vindo, {name}')
    notas()

def notas():
    nota1 = float(input('Digite a nota da AB1: '))
    nota2 = float(input('Digite a nota da AB2: '))
    if nota1 < 7 or nota2 < 7:
        reavaliação = float(input('Nota da reavaliação: '))
        if reavaliação >= nota1 and nota1 > nota2:
            nota2 = reavaliação
        elif reavaliação >= nota2 and nota2 > nota1:
            nota1 = reavaliação
    return calculadora_media(nota1,nota2)

def calculadora_media(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        status = 'AP'
    elif media >= 5 and media < 7:
        notaf = float(input('Nota final: '))        
        media_final = ((media*6)+(4*notaf)) / 10
        if media_final >= 5.5:
            status = 'AF'
        else:
            status = 'RF'
    else:
        status = 'RP'
    return print(f'Situação: {status}')
name = input('Digite seu nome: ')
inicio(name)    
