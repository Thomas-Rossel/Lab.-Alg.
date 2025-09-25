def sumar(num):
    suma=0
    if num < 0 or isinstance(num, float):
        print('El numero tiene que ser entero y positivo')
    else:
        for a in range(num+1):
            suma+=a
    
        print(suma)
sumar(5)