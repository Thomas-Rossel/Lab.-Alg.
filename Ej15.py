def raiz_entera(num):
    
    def funcion(x):
        
        if (x+1) * (x+1) > num:
            return x

        else:
            return funcion(x+1)
    
    return funcion(0)

print(raiz_entera(8))