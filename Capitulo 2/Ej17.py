def mostrar_vector(vector):
    
    if len(vector) == 0:
        return
    
    else:
        print(vector[-1], )
        vector.pop()
        return mostrar_vector(vector)
    

vec = [1, 8, 9, 42]
print(mostrar_vector(vec))