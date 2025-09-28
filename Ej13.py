def mcm(a, b, multiplo=None):
    
    if a == 0 or b == 0:
        return 0
    
    if multiplo is None:
        multiplo = a
    
    if multiplo % b == 0:
        return multiplo
    
    else:
        return mcm(a, b, multiplo + a)