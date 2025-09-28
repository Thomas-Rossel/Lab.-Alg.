def sucesion(n):
    
    if n == 1:
        return 2  
    
    return -3 * sucesion(n - 1)

def mostrar_sucesion(n):
    if n == 0:
        return
    mostrar_sucesion(n - 1)
    print(sucesion(n))

print(sucesion(4))
mostrar_sucesion(4)