def multiplicar(a, b):
    if isinstance(a, float) or isinstance(b, float):
        print("tienen que ser enteros")
    else:
        c = a*b
        print(c)

multiplicar(8.2,7)