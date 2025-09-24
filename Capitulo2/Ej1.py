def fibonacci(num):
    f=0
    lista=[]
    for a in range(num):
        if f == 0 or f == 1:
            lista.append(f)
            f+=1
        else:
            lista.append(lista[a-2]+lista[a-1])
    print(lista[-1])

fibonacci(7)