def busqueda_binaria_rec(A, objetivo, izq, der):
    if izq > der:
        return -1
    mid = (izq + der) // 2

    if A[mid] == objetivo:
        return mid
    
    elif A[mid] < objetivo:
        return busqueda_binaria_rec(A, objetivo, mid + 1, der)
    else:
        return busqueda_binaria_rec(A, objetivo, izq, mid - 1)


B = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
resultado = busqueda_binaria_rec(B, 38, 0, len(B) - 1)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado.")