def potencia(x,n):
    if n == 1:
        return x
    else:
        return x * potencia(x,n-1)

print(potencia(2,8))