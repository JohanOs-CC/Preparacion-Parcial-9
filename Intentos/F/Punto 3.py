def revertir(A: list):
    if len(A) <= 1:
        return A
    else:
        copia = list(A)
        ultimo = [copia.pop()]
        return ultimo + revertir(copia)
print(revertir([4, 7, 2, 9, 1, 5, 8, 3, 6]))

def palindromo(A):
    for i in range(len(A)):
        if A[i] == A[i-1]:
            print(f"{A[i]}={A[i-1]}")
        else:
            print("No es palindromo")
            return False
            break
    return True
print(palindromo([4, 7, 2, 9, 1, 5, 8, 3, 6]))