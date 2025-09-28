def busqueda_secuencial(vector, valor, i=0):
    
    if i == len(vector):
        return False
    
    if vector[i] == valor:
        return True
    
    return busqueda_secuencial(vector, valor, i + 1)

lista = [5, 8, 12, 20]
print(busqueda_secuencial(lista, 12))