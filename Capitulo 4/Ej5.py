import copy

mi_lista = [100, 10000, 1, 10, 1000, 100000]

def burbuja(lista):
    contador = {"comparaciones": 0, "intercambios": 0}
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-i-1):
            contador["comparaciones"] += 1
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                contador["intercambios"] += 1
    return lista, contador


def burbuja_mejorado(lista):
    contador = {"comparaciones": 0, "intercambios": 0}
    i = 0
    control = True
    while i <= len(lista)-2 and control:
        control = False
        for j in range(0, len(lista)-i-1):
            contador["comparaciones"] += 1
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                contador["intercambios"] += 1
                control = True
        i += 1
    return lista, contador


def coctel(lista):
    contador = {"comparaciones": 0, "intercambios": 0}
    izquierda = 0
    derecha = len(lista) - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            contador["comparaciones"] += 1
            if(lista[i] > lista[i+1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                contador["intercambios"] += 1
                control = True
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            contador["comparaciones"] += 1
            if(lista[j] < lista[j-1]):
                lista[j], lista[j-1] = lista[j-1], lista[j]
                contador["intercambios"] += 1
                control = True
        izquierda += 1
    return lista, contador


def seleccion(lista):
    contador = {"comparaciones": 0, "intercambios": 0}
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            contador["comparaciones"] += 1
            if(lista[j] < lista[minimo]):
                minimo = j
        if minimo != i:
            lista[i], lista[minimo] = lista[minimo], lista[i]
            contador["intercambios"] += 1
    return lista, contador


def insercion(lista):
    contador = {"comparaciones": 0, "intercambios": 0}
    for i in range(1, len(lista)):
        k = i
        while (k > 0):
            contador["comparaciones"] += 1
            if lista[k] < lista[k-1]:
                lista[k], lista[k-1] = lista[k-1], lista[k]
                contador["intercambios"] += 1
                k -= 1
            else:
                break
    return lista, contador


def quicksort(lista, primero, ultimo, contador=None):
    if contador is None:
        contador = {"comparaciones": 0, "intercambios": 0}

    izquierda = primero
    derecha = ultimo-1
    pivote = ultimo
    while (izquierda < derecha):
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha):
            contador["comparaciones"] += 1
            izquierda += 1
        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda):
            contador["comparaciones"] += 1
            derecha -= 1
        if(izquierda < derecha):
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            contador["intercambios"] += 1
    if(lista[pivote] < lista[izquierda]):
        contador["comparaciones"] += 1
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
        contador["intercambios"] += 1
    if(primero < izquierda):
        quicksort(lista, primero, izquierda-1, contador)
    if(ultimo > izquierda):
        quicksort(lista, izquierda+1, ultimo, contador)
    return lista, contador


def merge(izquierda, derecha, contador):
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha) > 0):
        contador["comparaciones"] += 1
        if (izquierda[0] < derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
        contador["intercambios"] += 1
    lista_mezclada += izquierda
    lista_mezclada += derecha
    return lista_mezclada


def mergesort(lista, contador=None):
    if contador is None:
        contador = {"comparaciones": 0, "intercambios": 0}

    if (len(lista) <= 1):
        return lista, contador
    else:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        izquierda, contador = mergesort(izquierda, contador)
        derecha, contador = mergesort(derecha, contador)
        resultado = merge(izquierda, derecha, contador)
        return resultado, contador


def count_sort(lista, maximo):
    contador = {"comparaciones": 0, "intercambios": 0}
    lista_conteo = [0] * (maximo + 1)
    lista_ordenada = [None] * len(lista)

    for i in lista:
        lista_conteo[i] += 1
        contador["intercambios"] += 1

    total = 0
    for i in range(len(lista_conteo)):
        lista_conteo[i], total = total, total + lista_conteo[i]

    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice
        lista_conteo[indice] += 1
        contador["intercambios"] += 1
    return lista_ordenada, contador

print("Burbuja:", burbuja(copy.copy(mi_lista)))
print("Burbuja mejorado:", burbuja_mejorado(copy.copy(mi_lista)))
print("Coctel:", coctel(copy.copy(mi_lista)))
print("Selección:", seleccion(copy.copy(mi_lista)))
print("Inserción:", insercion(copy.copy(mi_lista)))
print("Quicksort:", quicksort(copy.copy(mi_lista), 0, len(mi_lista)-1))
print("Mergesort:", mergesort(copy.copy(mi_lista)))
print("Count sort:", count_sort(copy.copy(mi_lista), max(mi_lista)))