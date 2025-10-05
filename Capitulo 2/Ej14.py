def suma_digitos(num):
    
    if num < 10:
        return num

    else:
        return num % 10 + suma_digitos(num // 10)
    
a=suma_digitos(85725)
print(a)