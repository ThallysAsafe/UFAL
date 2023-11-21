i = 0
senha = '0001'
n = 0
x = 0
limite = "1"+"0"*len(senha)
for i in range(int(limite)):
    n = str(i)
    numero = ""
    for x in range(abs(len(n)-len(senha))):
        numero+="0"
        x += 1
    numero += n
    if numero == senha:
        print(numero)
        break