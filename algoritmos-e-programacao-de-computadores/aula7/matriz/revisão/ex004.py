# Determinante de Matriz
# Implemente uma função que calcula o determinante de uma matriz quadrada.

def determinante_matriz(matriz):
    n = len(matriz)
    
    # Caso base: Matriz 1x1
    if n == 1:
        return matriz[0][0]
    
    # Caso base: Matriz 2x2
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    for coluna in range(n):
        # Calcula o cofator
        cofator = []
        for i in range(1, n):
            linha = []
            for j in range(n):
                if j != coluna:
                    linha.append(matriz[i][j])
            cofator.append(linha)
        
        # Aplica a fórmula recursivamente
        det += matriz[0][coluna] * (-1) ** coluna * determinante_matriz(cofator)
    
    return det

# Exemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = determinante_matriz(matriz)
print(f"O determinante da matriz é {resultado}")
