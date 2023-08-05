#Calcular IMC de uma lista de pessoas
imcs = []
nomes = []
pesos = []
alturas = []
for c in range(1,4):
    nome = (str(input(f'Digite o nome da {c}ª pessoa: ')))
    peso = (float(input(f'Digite o peso da {c}ª pessoa, em Kg: ')))
    altura = (float(input(f'Digite a altura da {c}ª pessoa, em Metros: ')))
    if peso < 0 and altura < 0:
        print('Dados inválidos, Tente Novamente!')
        c -= 1
    else:
        nomes.append(nome)
        pesos.append(peso)
        alturas.append(altura)
        imc = peso // altura**2
        imcs.append(imc)
for c in range(0,3):
    print(f'{nomes[c]} e {imcs[c]}')
