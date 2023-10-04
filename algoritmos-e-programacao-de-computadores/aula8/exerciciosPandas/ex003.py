# 3. Faça um programa que recebe dados de vários contatos (nome, telefone, email) e escreve os dados em um arquivo csv. O programa tem uma função que lê o arquivo e faz busca pelo nome do contato.
import pandas as pd
import os
arq = 'agenda.csv'

def buscContact(arq):
    agenda = pd.read_csv(arq)
    name=input('Qual contato?')
    resultado = agenda[agenda.nome == f'{name}']
    if len(resultado) == 0:
        print('Contato Inexistente.')
    else:
        print(agenda[agenda.nome == f'{name}'])
        
    
def CreatContact():
    nome = input('Nome: ')
    telefone = int(input('Numero: '))
    email = input('Email: ')
    if not os.path.exists('agenda.csv'):
        arq = open('agenda.csv','a')
        arq.write('nome,telefone,email\n')
        arq.close() 
    arq = open('agenda.csv','a')
    arq.write(f'{nome},{telefone},{email}\n')
    arq.close()

def main():
    opc = -1
    while opc != 0:
        print('''1-Criar Contato
    2-Buscar Contatos
    0-Sair''')
        opc = int(input('Escolha uma Opção: '))
        if opc == 1:
        
CreatContact()
buscContact(arq)