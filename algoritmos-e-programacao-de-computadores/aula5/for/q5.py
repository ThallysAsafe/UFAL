#Calcular o desconto de imposto de renda de uma lista de funcionários
nomes = []
salarios = []
impostos = []
x = 0
qnt = int(input('Quantos funcionarios deseja adicionar a lista? '))
for c in range(qnt):
    nome = str(input('Digite o nome do funcionário: '))
    salario = int(input('Digite o salario dele: R$'))
    if nome == int or salario <= 0:
        print('Entradas inválidas, não foram adicionados a lista!')
    else:
        x += 1
        imposto = 0
        nomes.append(nome)
        salarios.append(salario)
        imposto = imposto + salario*0.1
        impostos.append(imposto)
for i in range(x):
    print(f'{nomes[i]}, com salario de R${salarios[i]}, pagará o imposto de R${impostos[i]}')

