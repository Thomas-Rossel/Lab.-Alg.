def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

numero_decimal = 25
print(f"El número {numero_decimal} en binario es: {decimal_a_binario(numero_decimal)}")