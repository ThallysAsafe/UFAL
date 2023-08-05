'''Implemente um algoritmo para a Cifra de César
Texto:  a ligeira raposa marrom saltou sobre o cachorro cansado
chave = 5
Cifra: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
'''
frase = input('Digite uma frase para ser codificada: ').upper()
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
frase_criptografada = ''
for caracter in frase:
    if caracter in alfabeto:
        for posicao, letra in enumerate(alfabeto):
            if caracter == letra:
                posicao_criptografada = (posicao + 3) % 26
                frase_criptografada += alfabeto[posicao_criptografada]
    else:
        frase_criptografada += caracter
print(f'{frase_criptografada}')        