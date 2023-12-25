agenda_telefonica= [['yudi', {'telefone': '4002-8922','email': 'yudi@gmail.com'}],
    ['carlao', {'telefone': '69','email': 'carlao@gmail.com'}], 
    ['ana', {'telefone': '982','email': 'ana@gmail.com'}], 
    ['joao', {'telefone': '9822','email': 'jao@gmail.com'}],
    ['ricardao', {'telefone': 82,'email': 'ricardao@gmail.com'}]
    ]


for i in range(len(agenda_telefonica)-1):
    # seleciona o menor elemento
    menor = i
    for j in range(i+1,len(agenda_telefonica)):
        if agenda_telefonica[menor][0] > agenda_telefonica[j][0]:
            menor = j
    # insere na i-ésima
    agenda_telefonica[i][0], agenda_telefonica[menor][0] = agenda_telefonica[menor][0],agenda_telefonica[i][0]
print(agenda_telefonica)