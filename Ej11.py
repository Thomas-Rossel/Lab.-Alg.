def invertir(num, invertido=0):

    if num == 0:
        return invertido
    
    else:
        return invertir(num // 10, invertido * 10 + num % 10)

print(invertir(405))
