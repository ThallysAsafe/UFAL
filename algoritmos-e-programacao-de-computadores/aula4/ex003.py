'''3. Faça um programa que receba três números e ordene eles em ordem crescente.
'''
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro: '))
n3 = int(input('Digite um numero inteiro: '))
if n1 <= n2 <= n3:
    print(f'A ordem da sequencia é: {n1},{n2},{n3}')
elif n3 <= n1 <= n2:
    print(f'A ordem da sequencia é: {n3},{n1},{n2}')
elif n2 <= n3 <= n1:
    print(f'A ordem da sequencia é: {n2},{n3},{n1}')
elif n3 <= n2 <= n1:
    print(f'A ordem da sequencia é: {n3},{n2},{n1}')
