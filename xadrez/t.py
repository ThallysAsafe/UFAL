import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
valores = [10, 25, 15, 30]

# Criar o gráfico de barras
plt.bar(categorias, valores)

# Adicionar rótulos aos eixos
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Adicionar um título ao gráfico
plt.title('Gráfico de Barras Simples')

# Mostrar o gráfico
plt.show()
