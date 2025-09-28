def mostrar_matriz(matriz, fila=0, col=0):

    if fila == len(matriz):
        return
    
    if col == len(matriz[fila]): 
        print()
        mostrar_matriz(matriz, fila + 1, 0)
        return
    
    print(matriz[fila][col], end=' ')
    mostrar_matriz(matriz, fila, col + 1)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mostrar_matriz(matriz)