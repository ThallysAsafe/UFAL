from flask import Flask, request, render_template

app = Flask(__name__)


def converter_base(numero, base_origem,base_destino, alfabeto):

    if base_origem != 10:
        numero = converter_para_base10(numero, base_origem, alfabeto)
        if base_destino != 10 and numero != None:
            resultado = converter_da_base10(numero, base_destino, alfabeto)
            return resultado
    elif base_destino != 10:
        resultado = converter_da_base10(numero, base_destino, alfabeto)
        return resultado
    return numero

def converter_da_base10(numero, base_destino, alfabeto):
    # Inicialização de variáveis
    resto_divisão = []
    resultado = ''
    verifica = False  # Variável para verificar se há parte decimal
    decimais = []  # Lista para armazenar os dígitos da parte decimal
    con = False  # Variável para controlar se houve parte decimal
    k = 0  # Variável para controlar a primeira iteração
    condição = False  # Variável para verificar condições de validade
    decimal = str(numero)  # Converte o número em uma string

    if condição == False:
        # Loop para calcular a parte decimal em base_destino
        while len(decimais) < 5 and decimal != 0:  # Mostrar a quantidade de decimais 
            decimal = float(decimal)
            if decimal > 0:
                con = True
                decimal = str(decimal)
                inteiro, decimal = decimal.split('.')  # Divide em parte inteira e decimal
                decimal = int(decimal) * base_destino / (10 ** len(decimal))  # Calcula a parte decimal em base_destino
                inteiro = int(inteiro)
                if k == 0:
                    numero = inteiro
                    k += 1
                elif inteiro >= 0:
                    decimais.append(inteiro)  # Armazena os dígitos da parte decimal
                    verifica = True

        # Loop para calcular a parte inteira em base_destino
        while base_destino <= numero:
            resto = numero % base_destino
            numero = numero // base_destino
            resto_divisão.insert(0, resto)

        resto_divisão.insert(0, numero)

        # Loop para converter os dígitos da parte inteira em caracteres alfabéticos (se aplicável)
        for i in range(len(resto_divisão)):
            cond = False
            for letras in alfabeto.keys():
                if alfabeto[letras] == resto_divisão[i]:
                    resultado += f'{letras}'
                    cond = True
                elif alfabeto[letras] != resto_divisão[i] and alfabeto[letras] == 35 and cond == False:
                    resultado += f'{resto_divisão[i]}'

        # Verifica se há parte decimal para ser adicionada
        if verifica == True:
            if con == True:
                resultado += '.'

            # Loop para converter os dígitos da parte decimal em caracteres alfabéticos (se aplicável)
            for i in range(len(decimais)): # Mostrar a quantidade de decimais 
                cond = False
                decimal = int(decimais[i])
                for letras in alfabeto.keys():
                    if alfabeto[letras] == decimal:
                        resultado += f'{letras}'
                        cond = True
                    elif alfabeto[letras] != decimais[i] and alfabeto[letras] == 35 and cond == False:
                        resultado += f'{decimais[i]}'
        return resultado  # Retorna o resultado da conversão

def converter_para_base10(numero, base_origem, alfabeto):
    resultado = 0
    i = 0
    numero = str(numero)
    verifica = numero  # Variável para verificar se há parte decimal
    if '.' in numero:
        numero, decimal = numero.split('.')  # Divide o número em parte inteira e decimal
        numero = str(numero)
        tamanho = len(decimal)
        j = 0
        p = -1
        somaDecimal = 0  # Inicializa a soma da parte decimal

        # Loop para calcular a parte decimal
        while j < tamanho:
            if decimal[j] in alfabeto and alfabeto[decimal[j]] > 0:
                somaDecimal += ((alfabeto[decimal[j]]) * (base_origem**p))  # Converte dígitos alfabéticos
            else:
                somaDecimal += (int(decimal[j]) * (base_origem**p))  # Converte dígitos numéricos
            p -= 1
            j += 1

    # Loop para calcular a parte inteira
    while i < len(numero):
        if numero[i].isalpha():
            resultado += (base_origem**(len(numero)-i-1)) * alfabeto[numero[i]]  # Converte dígitos alfabéticos
        else:
            number = int(numero[i])
            resultado += number * (base_origem**(len(numero)-i-1))  # Converte dígitos numéricos
        i += 1

    # Verifica se há parte decimal e a adiciona à parte inteira
    if '.' in verifica:
        resultado += somaDecimal

    resultado = str(resultado)  # Converte o resultado para uma string
    return resultado  # Retorna o resultado da conversão

@app.route('/', methods=['GET', 'POST'])
def inicio():
    numero = '0'
    alfabeto = {
            "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
            "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
            "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
        }
    
    resultado = ''

    if request.method == 'POST':
        numero = str(request.form['numero']).upper()
        base_origem = int(request.form['base_origem'])
        base_destino = int(request.form['base_destino'])
        numero = numero.replace(",", ".")
        condição = False

        # Verifica se o número de entrada é decimal
        numer = numero
        if '.' in numero:
            numer, decimal = numero.split('.')
            # Loop para verificar cada dígito da parte decimal
            for num in decimal:
                if str(num).isalpha():
                    # Mostra o valor do dígito alfabético
                    if int(alfabeto[num]) >= base_origem:
                        condição = True  # Define a condição como verdadeira e sai do loop
                        break
                else:
                    if int(num) >= base_origem:
                        condição = True  # Define a condição como verdadeira e sai do loop
                        break

        # Loop para verificar cada dígito da parte inteira
        for num in numer:
            if str(num).isalpha():
                if int(alfabeto[num]) >= base_origem:
                    condição = True  # Define a condição como verdadeira e sai do loop
                    break
            else:
                if int(num) >= base_origem:
                    condição = True  # Define a condição como verdadeira e sai do loop
                    break

        # Verifica se a condição é falsa (não houve problemas de validação)
        if not condição:
            result = converter_base(numero, base_origem, base_destino, alfabeto)
            resultado = f'O numero {numero} escrito na base {base_origem} é equivalente a {result} na base {base_destino}'
        else:
            resultado = 'Não foi possível calcular este número, tente novamente mais tarde!'
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
