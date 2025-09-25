def romano(str):
    contador = 0
    for valor in str.upper():
        if valor == 'I':
            contador+=1
        elif valor == 'V':
            contador+=5
        elif valor == 'X':
            contador+=10
        elif valor == 'L':
            contador+=50
        elif valor == 'C':
            contador+=100
        elif valor == 'D':
            contador+=500
        elif valor == 'M':
            contador+=1000
        else:
            print("Se ingreso un valor no valido")
            break
    
    if contador != 0:
        print(contador)

romano("CCC")