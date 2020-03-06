""" Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0 os demais elementos. No final escreva a matriz
obtida."""
matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for linha in range(0, 5):
    for coluna in range(0, 5):
        if linha == coluna:
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0
print(matriz)
