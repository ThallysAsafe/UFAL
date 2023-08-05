'''Implemente um algoritmo para a Cifra de César
Texto:  a ligeira raposa marrom saltou sobre o cachorro cansado
chave = 5
Cifra: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
'''
frase = input('Digite uma frase para ser criptografada: ').upper()
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
frase_criptografada = ''
i = 0
# Determinando a quantidade de vezes que o while se repete.
while i < len(frase):
    # Dando um valor
    caracter = frase[i]
    if caracter in alfabeto:
        for posicao, alfa in enumerate(alfabeto):
            if caracter == alfa:
                posicao_criptografada = (posicao + 3) % 26
                caracter_criptografado = alfabeto[posicao_criptografada]
                frase_criptografada += caracter_criptografado
    else:
        frase_criptografada += caracter
    i += 1
print(f'Frase criptografada: {frase_criptografada}')

    
        
    
