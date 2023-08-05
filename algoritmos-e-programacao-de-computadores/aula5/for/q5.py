#Calcular o desconto de imposto de renda de uma lista de funcionários
nomes = []
salarios = []
impostos = []
for c in range(0,3):
    nome = str(input('Digite o nome do funcionário: '))
    salario = int(input('Digite o salario dele: R$'))
    if nome == int or salario <= 0:
        print('Entradas inválidas, Tente Novamente!')
        c -= 1
    else:
        imposto = 0
        nomes.append(nome)
        salarios.append(salario)
        imposto = imposto + salario*0.1
        impostos.append(imposto)
for i in range(0,3):
    print(f'{nomes[i]}, com salario de R${salarios[i]}, pagará o imposto de R${impostos[i]}')

