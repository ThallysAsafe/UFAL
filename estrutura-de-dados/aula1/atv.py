lista = {'Iceberg': 500,'VOSS': 400,'Itaipava': 900,'Brasken': 10000,'Shein':15000}
maiorempresa = ''
maioracao = lista['Iceberg']
for empresa in lista:
    if maioracao < lista[empresa]:
        maiorempresa = empresa
        maioracao = lista[empresa]
print(maiorempresa,maioracao)        

print('quadrinhos')
    for pos, quadrinhos in enumerate(shop_items['quadrinhos']):
        print(f"{pos} - Produto: {quadrinhos['Nome']} | Tamanho: {quadrinhos['Tamanhos']}| Preço: {quadrinhos['Preço']} ")