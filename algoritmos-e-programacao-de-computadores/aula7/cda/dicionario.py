usuario = {'nome': 'Thallys',
           'email': 'thallys.cpta@arapiraca.ufal.br',
           'senha': '12442' 
           }

usuario['nome'] = 'bob'
print(usuario['nome'])

print(usuario.keys())
for key in usuario.keys():
    print(usuario[key])

dicionario = {1: 'Ana', 2: '2142412'}
print(dicionario)
print(dicionario[1])