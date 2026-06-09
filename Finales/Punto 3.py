def revertir(A: list):
    if len(A) <= 1:
        return A
    else:
        copia = list(A)
        ultimo = [copia.pop()]
        return ultimo + revertir(copia)
print(revertir([1,2,3,4,5,6]))