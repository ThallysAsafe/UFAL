# Roteiro de Laboratório – Mudança de Bases Numéricas

#  Objetivo: Dado um número, sua base de origem e a informação da base de destino, o
# sistema deve receber realizar a conversão de base e apresentar o valor equivalente do
# número na base de destino.

    #  Comportamento desejado:
        # ◦ O sistema deve ler inicialmente uma base (de origem), um número nessa base e uma
        # outra base (de destino).
        # ◦ Em seguida, deve executar uma função converter_base(numero, base_origem,base_destino).
        # ◦ Finalmente, deve apresentar uma mensagem informando que o número “numero”,
        # escrito na base “base_origem” é equivalente ao número “resultado” na base “base_destino”.

    #  Observações Adicionais:
        # ◦ OBS.1: Pode implementar com interface textual mesmo. A implementação com
        # interface gráfica será valorizada como pontuação extra.
        # ◦ OBS.2: A conversão de números inteiros já vale 90% da atividade. Para garantir os
        # 100%, deve incluir a conversão de números reais.
        # ◦ OBS.3: Além da tela do computador em si, o rosto do apresentador também deve
        # aparecer no vídeo de apresentação.
        # ◦ OBS.4: Quem preferir, ao invés de gravar o vídeo, pode agendar com o professor
        # um horário para apresentar pessoalmente.

    #  DICA:
        # ◦ Uma dica seria implementar três funções:
        # ▪ 1- Uma para converter de qualquer base para a base 10
        #  converter_para_base10(numero, base_origem)
        # ▪ 2- Uma para converter da base 10 para qualquer base
        #  converter_da_base10(numero, base_destino)
        # ▪ 3- Uma para utilizar as outras duas, convertendo de qualquer base para
        # qualquer base
        #  converter_base(numero, base_origem, base_destino)
        # ◦ Podemos limitar as bases possíveis de 2 a 36. O limite até a base 36 é para assumir
        # que nos limitaremos aos números e letras do alfabeto, ok?

import tkinter
def inicio(alfabeto):
    numero = input('Digite o numero: ').upper()
    base_origem = int(input('Insira a base de origem: [2 a 36]'))
    base_destino = int(input('Insira qual a base destino: [2 a 36]'))
    condição = False
    if '.' in numero: # Verificador decimal
        numero, decimal = numero.split('.')
        for num in decimal:
            if str(num).isalpha():
                print(alfabeto[num])
                if int(alfabeto[num]) >= base_origem:
                    condição = True
                    break
            else:
                if int(num) >= base_origem:
                    condição = True
                    break
    for num in numero:
        if str(num).isalpha():
            print(alfabeto[num])
            if int(alfabeto[num]) >= base_origem:
                condição = True
                break
        else:
            if int(num) >= base_origem:
                condição = True
                break
    if condição == False:
        resultado = converter_base(numero, base_origem,base_destino, alfabeto)
        print(f'{numero} escrito na base {base_origem} é equivalente a {resultado} na base {base_destino}')
    else:
        print('Não foi possivel calcular este numero, tente novamente mais tarde!')
        print()

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
    resto_divisão = []
    resultado = ''
    verifica = False
    decimais = []
    con = False
    k = 0
    condição = False
    if condição == False:
        while decimal > 0 and len(decimais) < 22:# Mostrar a quantidade de decimais 
            if decimal > 0 :
                con = True
                decimal = str(decimal)
                inteiro, decimal = decimal.split('.')
                tamanho = len(decimal)  
                decimal = int(decimal)
                decimal = (decimal / (10**tamanho))
                decimal = decimal * base_destino
                inteiro = int(inteiro)
                if k == 0:
                    numero = inteiro    
                    k += 1
                elif inteiro >= 0:
                    decimais.append(inteiro)
                    verifica = True
        while base_destino <= numero:
            resto = numero % base_destino
            numero = numero // base_destino
            resto_divisão.insert(0, resto)
        resto_divisão.insert(0, numero)
        for i in range(len(resto_divisão)):
            cond = False
            for letras in alfabeto.keys():
                if alfabeto[letras] == resto_divisão[i]:
                    resultado += f'{letras}'
                    cond = True
                elif alfabeto[letras] != resto_divisão[i] and alfabeto[letras] == 35 and cond == False:
                    resultado += f'{resto_divisão[i]}'
        if verifica == True:
            if con == True:
                resultado += '.'
            for i in range(len(decimais)): # Mostrar a quantidade de decimais 
                cond = False
                decimal = int(decimais[i])
                for letras in alfabeto.keys():
                    if alfabeto[letras] == decimal:
                        resultado += f'{letras}'
                        cond = True
                    elif alfabeto[letras] != decimais[i] and alfabeto[letras] == 35 and cond == False:
                        resultado += f'{decimais[i]}'
        return resultado
    else:
        print('Não foi possivel calcular este numero, tente novamente mais tarde!')
        print()
def converter_para_base10(numero, base_origem, alfabeto):
    resultado = 0
    i = 0
    numero = str(numero)
    verifica = numero
    if '.' in numero:
        numero, decimal = numero.split('.')
        numero = str(numero)
        tamanho = len(decimal)
        j = 0
        p = -1
        somaDecimal = 0
        while j < tamanho:
            if decimal[j] in alfabeto and alfabeto[decimal[j]] > 0:
                somaDecimal += ((alfabeto[decimal[j]]) * (base_origem**p))
                
            else:
                somaDecimal += (int(decimal[j]) * (base_origem**p))
            p -= 1
            j += 1
    while i < len(numero):
        if numero[i].isalpha():
            resultado += (base_origem**(len(numero)-i-1)) * alfabeto[numero[i]]

        else:
            number = int(numero[i])
            resultado += number * (base_origem**(len(numero)-i-1))
        i += 1
    
    if '.' in verifica:
        resultado += somaDecimal
        resultado = str(resultado)
    resultado = str(resultado)    
    return resultado
alfabeto = {"A": 10,"B": 11,"C": 12,"D": 13,"E": 14,"F": 15,"G": 16,"H": 17,"I": 18,"J": 19,
                "K": 20,"L": 21,"M": 22,"N": 23,"O": 24,"P": 25,"Q": 26,"R": 27,"S": 28,"T": 29,
                "U": 30,"V": 31,"W": 32,"X": 33,"Y": 34,"Z": 35}
inicio(alfabeto)