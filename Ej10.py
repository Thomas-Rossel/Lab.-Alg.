def digitos_numero(num):

    if num < 10:
        return(1)
    
    else:
        return 1 + digitos_numero(num // 10)

print(digitos_numero(10))