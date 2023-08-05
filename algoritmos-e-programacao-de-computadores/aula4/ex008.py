'''8. Escreva  um algoritmo que lê dois inteiros A e B e os escreve com a mensagem: “São múltiplos” ou “Não são múltiplos”.'''
a = int(input('Digite o numero inteiro: '))
b = int(input('Digite outro numero inteiro: '))
if a % b == 0 and b % a == 0:
    print('São numeros inteiros!')
else:
    print('numero inválido!')