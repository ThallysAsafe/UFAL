import random

carrinho = []
camisa = []
caneca = []
quadrinho = []

class Produto:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.numero_serie = None

    def _str_(self):
        return f"Nome: {self.nome} | Preço: {self.preco}"

    def _repr_(self):
        return f"Nome: {self.nome} | Preço: {self.preco}"

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

def gerar_numero_serie(tipo_produto, quantidade=1):
    numeros_serie = []
    
    while len(numeros_serie) < quantidade:
        if tipo_produto == 'camisa':
            numero_serie = random.randint(10000, 99999)
            if numero_serie % 5 == 0:
                print(f'Número de série da camisa: {numero_serie}')
                numeros_serie.append(numero_serie)
        elif tipo_produto == 'caneca':
            numero_serie = random.randint(100, 999)
            if numero_serie % 3 == 0:
                print(f'Número de série da caneca: {numero_serie}')
                numeros_serie.append(numero_serie)
        elif tipo_produto == 'quadrinho':
            numero_serie = random.randint(1000000, 9999999)
            if numero_serie % 7 == 0:
                print(f'Número de série do quadrinho: {numero_serie}')
                numeros_serie.append(numero_serie)

    return numeros_serie

numeros_camisas = gerar_numero_serie('camisa', quantidade=2)
for numero in numeros_camisas:
    print(numero)
    
numeros_quadrinhos = gerar_numero_serie('quadrinho', quantidade=1)
for numero in numeros_quadrinhos:
    print(numero)
    
numeros_canecas = gerar_numero_serie('caneca', quantidade=1)
for numero in numeros_canecas:
    print(numero)

class Camisa(Produto):
    def _init_(self, nome, preco, tamanho):
        super()._init_(nome, preco)
        self.tamanho = tamanho
        self.numero_serie = gerar_numero_serie('camisa')

    def _str_(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | {self.tamanho} | Número de Série: {self.numero_serie}"

    def _repr_(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | {self.tamanho} | Número de Série: {self.numero_serie}"

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

class Caneca(Produto):
    def _init_(self, nome, preco, capacidade):
        super()._init_(nome, preco)
        self.capacidade = capacidade
        self.numero_serie = gerar_numero_serie('caneca')

    def _str_(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | {self.capacidade} | Número de Série: {self.numero_serie}"

    def _repr_(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | {self.capacidade} | Número de Série: {self.numero_serie}"

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

class Quadrinho(Produto):
    def _init_(self, nome, preco, autor, editora):
        super()._init_(nome, preco)
        self.autor = autor
        self.editora = editora
        self.numero_serie = gerar_numero_serie('quadrinho')

    def _str_(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | {self.autor} | {self.editora} | Número de Série: {self.numero_serie}"

    def _repr_(self):
        return f"Nome: {self.nome} | Preço: {self.preco} | {self.autor} | {self.editora} | Número de Série: {self.numero_serie}"

    def get_autor(self):
        return self.autor

    def get_editora(self):
        return self.editora

    def set_autor(self, autor):
        self.autor = autor

    def set_editora(self, editora):
        self.editora = editora

def remover_produto(nome_produto):
    carrinho

    produto_encontrado = False

    for produto in carrinho:
        if produto['produto'].get_nome() == nome_produto:
            quantidade_remover = int(input(f'Digite a quantidade de {nome_produto} a ser removida: '))

            if quantidade_remover >= produto['quantidade']:
                carrinho.remove(produto)
                print(f'Uma unidade de {nome_produto} removida do carrinho.')
            elif quantidade_remover > 0:
                produto['quantidade'] -= quantidade_remover
                print(f"{quantidade_remover} {nome_produto} removido(s) do carrinho.")

            else: 
                print('Quantidade inválida. Nenhum item removido')

            produto_encontrado = True 
            break

    if not produto_encontrado:
        print(f"{nome_produto} não encontrado no carrinho.")

def adicionar_produto_ao_carrinho(carrinho, produto, quantidade):
    for item in carrinho:
        if item['produto'].get_nome() == produto.get_nome():
            item['quantidade'] += quantidade
            print(f"{quantidade} {produto.get_nome()} adicionado(s) ao carrinho. Número de Série: {produto.numero_serie}")
            return

    carrinho.append({'produto': produto, 'quantidade': quantidade})
    print(f"{quantidade} {produto.get_nome()} adicionado(s) ao carrinho. Número de Série: {produto.numero_serie}")


def finalizar_compra():
    carrinho

    if not carrinho:
        print("Carrinho vazio. Nada a finalizar.")
        return

    print("\nResumo da compra:")
    carrinho.sort(key=lambda item: item['produto'].get_preco())

    total = 0
    produtos_na_promocao = []
    for item in carrinho:
        produto = item['produto']
        quantidade = item['quantidade']
        preco_total = produto.get_preco() * quantidade

        print(f"{quantidade} {produto.get_nome()} - Preço unitário: {produto.get_preco()} - Preço total: {preco_total}")

        total += preco_total

        if isinstance(produto, Camisa) and quantidade >= 4:
            caneca_brinde = Caneca("Caneca de brinde", 0, 0)
            adicionar_produto_ao_carrinho(carrinho, caneca_brinde, 1)
            produtos_na_promocao.append(caneca_brinde.get_nome())

        if isinstance(produto, Quadrinho) and quantidade >= 5:
            produtos_na_promocao.append(produto.get_nome())

    #aplica o desconto
    if len(produtos_na_promocao) > 0:
        for item in carrinho:
            if item['produto'].get_nome() in    produtos_na_promocao:
                quantidade_minima_promocao = 5 if isinstance(item['produto'], Quadrinho) else 4
                if item['quantidade'] >= quantidade_minima_promocao:
                    preco_unitario = item['produto'].get_preco()
                    preco_total_unitario = preco_unitario * item['quantidade']
                    menor_preco_unitario = min(preco_total_unitario / item['quantidade'] for item in carrinho if isinstance(item['produto'], Quadrinho) and item['produto'].get_nome() in produtos_na_promocao)
                    if preco_total_unitario / item['quantidade'] == menor_preco_unitario:
                        print(f"Promoção: Quadrinho de menor valor '{item['produto'].get_nome()}' sai de graça.")
                        carrinho.remove(item)
                        print("Parabéns! Você recebeu um brinde pela promoção.")
                        break

    print("\nTotal da compra:", total)

while True: #loop para receber os comandos
    print("\nComandos:")
    print("1. Adicionar produto ao carrinho")
    print("2. Remover produto do carrinho")
    print("3. Finalizar compra")
    print("4. Sair")

    comando = input("Digite o número do comando desejado: ")

    try:
        comando = int(comando)
    except ValueError:
        print("Digite um número válido.")
        continue

    if comando == 1:  #para adicionar os produto
        nome_produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))

        tipo_produto = input("Digite o tipo de produto (camisa, caneca, quadrinho): ")

        if tipo_produto == 'camisa':
            tamanho = input("Digite o tamanho da camisa (P, M, G): ")
            produto = Camisa(nome_produto, 10, tamanho)
        elif tipo_produto == 'caneca':
            capacidade = float(input("Digite a capacidade da caneca em litros: "))
            produto = Caneca(nome_produto, 15, capacidade)
        elif tipo_produto == 'quadrinho':
            autor = input("Digite o autor do quadrinho: ")
            editora = input("Digite a editora do quadrinho: ")
            produto = Quadrinho(nome_produto, 20, autor, editora)
        else:
            print("Tipo de produto inválido.")
            continue

        adicionar_produto_ao_carrinho(carrinho, produto, quantidade)
    elif comando == 2:
        nome_produto = input("Digite o nome do produto a ser removido: ")
        remover_produto(nome_produto)
    elif comando == 3:
        finalizar_compra()
        break
    elif comando == 4:
        break  # para o comando
    else:
        print("Comando inválido. Digite um número válido.")