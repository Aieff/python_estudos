matriz_1 = [[1, 3, 5],
            [6, 9, 5],
            [1, 3, 5]]

matriz_2 = [[1, 2, 3],
            [4, 9, 10],
            [11, 23, 54]]

for linha in range(len(matriz_1)):
    for coluna in range(len(matriz_1)):
        if matriz_1[linha][coluna] == matriz_2[linha][coluna]:
            print(matriz_1[linha][coluna])