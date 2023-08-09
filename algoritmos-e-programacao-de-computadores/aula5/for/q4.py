#Calcular IMC de uma lista de pessoas
imcs = []
nomes = []
pesos = []
alturas = []
x = 0  
qnt = int(input('quantas pessoas voce quer adicionar a lista? '))
for c in range(1,qnt+1):
    nome = (str(input(f'Digite o nome da {c}ª pessoa: ')))
    peso = (float(input(f'Digite o peso da {c}ª pessoa, em Kg: ')))
    altura = (float(input(f'Digite a altura da {c}ª pessoa, em Metros: ')))
    if peso < 0 or altura < 0:
        print('Dados inválidos, Valor não adicionado!')     
    else:
        x += 1
        nomes.append(nome)
        pesos.append(peso)
        alturas.append(altura)
        imc = peso // (altura**2)
        imcs.append(imc)
for c in range(x):
    print(f'{nomes[c]} e {imcs[c]}')
