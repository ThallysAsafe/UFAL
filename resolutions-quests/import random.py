import random

carrinho = []
camisa = []
caneca = []
quadrinho = []

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.numero_serie = None

    def __str__(self):
        return f"Nome: {self.nome} | Preço: {self.preco}"

    def __repr__(self):
        return f"Nome: {self.nome} | Preço: {self.preco}"

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

def gerar_numero_serie(tipo_produto, quantidade):
    numeros_serie = []
    quantidade = quantidade
    if quantidade < 1:
        quantidade = 1
    while len(numeros_serie) < quantidade:
        if tipo_produto == 'camisa':
            numero_serie = random.randint(10000, 99999)
            if numero_serie % 5 == 0:
                numeros_serie.append(numero_serie)
        elif tipo_produto == 'caneca':
            numero_serie = random.randint(100, 999)
            if numero_serie % 3 == 0:
                numeros_serie.append(numero_serie)
        elif tipo_produto == 'quadrinho':
            numero_serie = random.randint(1000000, 9999999)
            if numero_serie % 7 == 0:
                numeros_serie.append(numero_serie)

    return numeros_serie

class Camisa(Produto):
    def __init__(self, nome, preco, tamanho, quantidade):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.tipo = "camisa"
        self.quantidade = quantidade
        self.numero_serie = gerar_numero_serie('camisa', quantidade)

    def __str__(self):
        return f"Tipo: {self.tipo} Nome: {self.nome} | Preço: {self.preco} | {self.tamanho} | Número de Série: {self.numero_serie} | Quantidade: {self.quantidade}"

    def __repr__(self):
        return f"Tipo: {self.tipo} Nome: {self.nome} | Preço: {self.preco} | {self.tamanho} | Número de Série: {self.numero_serie} | Quantidade: {self.quantidade}"

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

class Caneca(Produto):
    def __init__(self, nome, preco, capacidade, quantidade):
        super().__init__(nome, preco)
        self.capacidade = capacidade
        self.tipo = "caneca"
        self.quantidade = quantidade
        self.numero_serie = gerar_numero_serie('caneca', quantidade)

    def __str__(self):
        return f"Tipo: {self.tipo} Nome: {self.nome} | Preço: {self.preco} | {self.capacidade} | Número de Série: {self.numero_serie} | Quantidade: {self.quantidade}"

    def __repr__(self):
        return f"Tipo: {self.tipo} Nome: {self.nome} | Preço: {self.preco} | {self.capacidade} | Número de Série: {self.numero_serie} | Quantidade: {self.quantidade}"

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

class Quadrinho(Produto):
    def __init__(self, nome, preco, autor, editora, quantidade):
        super().__init__(nome, preco)
        self.autor = autor
        self.editora = editora
        self.quantidade = quantidade
        self.tipo = "quadrinho"
        self.numero_serie = gerar_numero_serie('quadrinho', quantidade)

    def __str__(self):
        return f"Tipo: {self.tipo} Nome: {self.nome} | Preço: {self.preco} | Autor: {self.autor} | Editora: {self.editora} | Número de Série: {self.numero_serie} | Quantidade: {self.quantidade}"

    def __repr__(self):
        return f"Tipo: {self.tipo} Nome: {self.nome} | Preço: {self.preco} | Autor: {self.autor} | Editora: {self.editora} | Número de Série: {self.numero_serie} | Quantidade: {self.quantidade}"

    def get_autor(self):
        return self.autor

    def get_editora(self):
        return self.editora

    def set_autor(self, autor):
        self.autor = autor

    def set_editora(self, editora):
        self.editora = editora

def remover_produto(carrinho):
    if not carrinho:
        print("Carrinho vazio. Nada para Remover.")
        return

    print("Itens do Carrinho:")
    for pos, item in enumerate(carrinho, 1):
        print(f"{pos} {item['produto'].get_nome()['Nome']} - Quantidade: {item['quantidade']}")

    id = int(input('Digite a numeração do item que deseja remover: '))
    id = id - 1

    if 0 <= id < len(carrinho):
        produto = carrinho[id]['produto']
        nome_produto = produto.get_nome()['Nome']

        carrinho.pop(id)
        print(f'Todo o item {nome_produto} removido do carrinho.')
    else:
        print('Número de item inválido. Nenhum item removido.')

def adicionar_produto_ao_carrinho(carrinho, produto, quantidade):
    for item in carrinho:
        if (
            item['produto'].get_nome() == produto.get_nome()
            and item['produto'].numero_serie == produto.numero_serie
            and type(produto) != dict
        ):
            if isinstance(produto, Camisa) and 'Caneca(s) de brinde(s)' in produto.get_nome():
                item['quantidade'] += quantidade
                print(f"{quantidade} {produto.get_nome()} adicionado(s) ao carrinho. Número de Série: {produto.numero_serie}")
                return
            return

    carrinho.append({'produto': produto, 'quantidade': quantidade, 'numero_serie': produto.numero_serie})
    if isinstance(produto, dict):
        print(f"{quantidade} {produto['Nome']} adicionado(s) ao carrinho. Número de Série: {produto.numero_serie}")
def finalizar_compra():
    carrinho
    if not carrinho:
        print("Carrinho vazio. Nada a finalizar.")
        return
    print("\nItens do carrinho:")
    print(carrinho)
    for i, itens in enumerate(carrinho,1):
        produtos = itens['produto']
        quantidade = itens['quantidade']
        numero_serie = itens['numero_serie']
        if produtos.tipo.capitalize() == 'Camisa':
            print(f"{i} - Camisa: {produtos.get_nome()['Nome']} | Quantidade: {quantidade} | Tamanho: {produtos.tamanho.upper()} | Número(s) de Série: {numero_serie}")
        elif produtos.tipo.capitalize() == 'Caneca':
            print(f"{i} - Caneca: {produtos.get_nome()['Nome']} | Quantidade: {quantidade} | Capacidade: {produtos.capacidade} Litros | Número(s) de Série: {numero_serie}")
        elif produtos.tipo.capitalize() == 'Quadrinho':
            print(f"{i} - Quadrinho: {produtos.get_nome()['Nome']} | Quantidade: {quantidade} | Preço: {produtos.preco} | Autor: {produtos.autor} | Editora: {produtos.editora} | Número(s) de Série: {numero_serie}")

    print("\nResumo da compra:")
    carrinho.sort(key=lambda item: item['produto'].get_preco())

    print()
    total = 0
    produtos_na_promocao = []
    for j, item in enumerate(carrinho, 1):
        produto = item['produto']
        quantidade = item['quantidade']
        preco_total = produto.get_preco() * quantidade
        
        if isinstance(produto.get_nome(), dict):
            print(f"{j} - Quantidade: {quantidade} | {produto.get_nome()['Nome']} - Preço unitário: {produto.get_preco()} - Preço total: {preco_total:.1f}")
        else:
            print(f"{j} - Quantidade: {produto.quantidade} | {produto.get_nome()} - Preço unitário: {produto.get_preco()} - Preço total: {preco_total:.1f}")
        total += preco_total
        if isinstance(produto, Camisa) and quantidade >= 4:
            quantidades = quantidade // 4
            caneca_brinde = Caneca("Caneca(s) de brinde(s)", 0, 0, quantidades)
            adicionar_produto_ao_carrinho(carrinho, caneca_brinde, 1)
            produtos_na_promocao.append(caneca_brinde.get_nome())

        if isinstance(produto, Quadrinho) and quantidade >= 5:
            produtos_na_promocao.append(produto.get_nome())

    #aplica o desconto
    if len(produtos_na_promocao) > 0:
        for item in carrinho:
            if item['produto'].get_nome() in produtos_na_promocao:
                quantidade_minima_promocao = 5 if isinstance(item['produto'], Quadrinho) else 4
                if item['quantidade'] >= quantidade_minima_promocao:
                    preco_unitario = item['produto'].get_preco()
                    preco_total_unitario = preco_unitario * item['quantidade']
                    menor_preco_unitario = min(preco_total_unitario / item['quantidade'] for item in carrinho if isinstance(item['produto'], Quadrinho) and item['produto'].get_nome() in produtos_na_promocao)
                    if preco_total_unitario / item['quantidade'] == menor_preco_unitario:
                        print(f"Promoção: Quadrinho de menor valor '{item['produto'].get_nome()['Nome']}' sai de graça.")
                        carrinho.remove(item)
                        print("Parabéns! Você recebeu um brinde pela promoção.")
                        break

    print(f"\nTotal da compra: {total:.1f}")

while True: #loop para receber os comandos
    print('\nProdutos disponíveis no Catalogo da Loja')
    shop_items = {
    'Camisas': [
        {'Nome': 'Pixel Adventure', 'Tamanhos': ['P', 'M', 'G'], 'Preço': 49.90},
        {'Nome': 'Code Master', 'Tamanhos': ['P', 'M', 'G'], 'Preço': 39.90},
        {'Nome': 'Galaxy Explorer', 'Tamanhos': ['P', 'M', 'G'], 'Preço': 54.90},
        {'Nome': 'Retro Gamer', 'Tamanhos': ['P', 'M', 'G'], 'Preço': 45.00}
    ],

    'Canecas': [
        {'Nome': 'Binary Brew', 'Litros': 1, 'Preço': 29.90},
        {'Nome': 'Code Conqueror', 'Litros': 2, 'Preço': 39.90},
        {'Nome': 'Space Invader', 'Litros': 3, 'Preço': 49.90},
        {'Nome': 'Pixel Potion', 'Litros': 1, 'Preço': 24.90}
    ],

    'Quadrinhos': [
        {'Nome': 'Chronicles of Code', 'Autor': 'Alex Developer', 'Editora': 'TechComics', 'Preço': 19.90},
        {'Nome': 'Galactic Gamers', 'Autor': 'Sarah Pixel', 'Editora': 'GeekPress', 'Preço': 25.00},
        {'Nome': 'Code Warriors', 'Autor': 'Chris Algorithm', 'Editora': 'ByteComics', 'Preço': 22.50},
        {'Nome': 'Retro Adventures', 'Autor': 'Max Bit', 'Editora': 'PixelBooks', 'Preço': 18.00}
    ]
}
    print('\nCamisas')
    for pos, camisas in enumerate(shop_items['Camisas'],1):
        print(f"{pos} - Produto: {camisas['Nome']} | Tamanho: {camisas['Tamanhos']}| Preço: {camisas['Preço']} ")
    print('\nCanecas')
    for pos, canecas in enumerate(shop_items['Canecas'],1):
        print(f"{pos} - Produto: {canecas['Nome']} | Capacidade: {canecas['Litros']}| Preço: {canecas['Preço']} ")
    print('\nQuadrinhos')
    for pos, quadrinhos in enumerate(shop_items['Quadrinhos'],1):
        print(f"{pos} - Produto: {quadrinhos['Nome']} | Autor: {quadrinhos['Autor']}| Editora {quadrinhos['Editora']} | Preço: {quadrinhos['Preço']} ")
    print("\nComandos:")
    print("1. Adicionar produto ao carrinho")
    print("2. Remover produto do carrinho")
    print("3. Finalizar compra")

    comando = input("Digite o número do comando desejado: ")

    try:
        comando = int(comando)
    except ValueError:
        print("Digite um número válido.")
        continue
    if comando == 1:  #para adicionar os produtos
        tipo_produto = input("Digite o tipo de produto (camisas, canecas, quadrinhos): ")
        if tipo_produto == 'camisas':
            for pos, camisas in enumerate(shop_items['Camisas'],1):
                print(f"{pos} - Produto: {camisas['Nome']} | Tamanho: {camisas['Tamanhos']}| Preço: {camisas['Preço']} ")
            id = int(input('Digite a numeração do item que deseja:'))
            id = id - 1
            nome_produto = shop_items['Camisas'][id]
            valor = shop_items['Camisas'][id]['Preço']
            quantidade = int(input("Digite a quantidade: "))
            tamanho = input("Digite o tamanho da camisa (P, M, G): ")
            produto = Camisa(nome_produto, valor, tamanho, quantidade)
        elif tipo_produto == 'canecas':
            for pos, canecas in enumerate(shop_items['Canecas'],1):
                print(f"{pos} - Produto: {canecas['Nome']} | Capacidade: {canecas['Litros']}| Preço: {canecas['Preço']} ")
            id = int(input('Digite a numeração do item que deseja:'))
            id = id - 1
            nome_produto = shop_items['Canecas'][id]
            valor = shop_items['Canecas'][id]['Preço']
            quantidade = int(input("Digite a quantidade: "))
            capacidade = shop_items['Canecas'][id]['Litros']
            produto = Caneca(nome_produto, valor, capacidade, quantidade)
        elif tipo_produto == 'quadrinhos':
            for pos, quadrinhos in enumerate(shop_items['Quadrinhos'],1):
                print(f"{pos} - Produto: {quadrinhos['Nome']} | Autor: {quadrinhos['Autor']}| Editora {quadrinhos['Editora']} | Preço: {quadrinhos['Preço']} ")
            id = int(input('Digite a numeração do item que deseja:'))
            id = id - 1
            nome_produto = shop_items['Quadrinhos'][id]
            valor = shop_items['Quadrinhos'][id]['Preço']
            quantidade = int(input("Digite a quantidade: "))
            autor = shop_items['Quadrinhos'][id]['Autor']
            editora = shop_items['Quadrinhos'][id]['Editora']
            produto = Quadrinho(nome_produto, valor, autor, editora, quantidade)
        else:
            print("Tipo de produto inválido.")
            continue
        cond = False
        adicionar_produto_ao_carrinho(carrinho, produto, quantidade)
    elif comando == 2:
        remover_produto(carrinho)
    elif comando == 3:
        finalizar_compra()
        break
    else:
        print("Comando inválido. Digite um número válido.")