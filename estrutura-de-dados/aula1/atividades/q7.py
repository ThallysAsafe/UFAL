# 7. Algoritmo que tenta quebrar uma senha de
# quatro dígitos numéricos
i = 0
senha = '0001'
n = 0
x = 0
limite = "1"+"0"*len(senha)
for i in range(int(limite)):  # O(N)
    n = str(i)
    numero = ""
    for x in range(abs(len(n)-len(senha))): # O(M)
        numero+="0"
        x += 1
    numero += n
    if numero == senha:
        print(numero)
        break

# O(N) x O(M) ---> O(M x N)