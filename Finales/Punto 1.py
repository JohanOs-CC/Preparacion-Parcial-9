def generar_A(n):
    lista = []

    for i in range(1,n+1):
        di = 3*i-1
        lista.append(di)
    return lista
print(generar_A(6))