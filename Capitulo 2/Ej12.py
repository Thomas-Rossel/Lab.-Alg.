def mcd(a, b):
    if b == 0:
        return a
    
    if a == 0:
        return b

    else:    
        return mcd(b, a % b)
    
print(mcd(2, 0))