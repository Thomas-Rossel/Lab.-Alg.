def potencia(a,b):
    if isinstance(a, float) or isinstance(b, float):
        print("tienen que ser numerosenteros")
    else:
        c = a**b
        print(c)

potencia(2,3)

