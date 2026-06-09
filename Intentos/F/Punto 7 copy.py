def mx_mn(A: list):
        if len(A) == 1:
            return (A[0], A[0])
        elif len(A) == 2:
            if A[0] < A[1]:
                return (A[0], A[1])
            else:
                return (A[1], A[0])
        
        mitad = len(A) // 2

        min_izq, max_izq = mx_mn(A[:mitad])
        min_der, max_der = mx_mn(A[mitad:])
        
        if min_izq < min_der:
            finalmi = min_izq
        else:
            finalmi = min_der
        
        if max_izq > max_der:
            finalma = max_izq
        else:
            finalma = max_der
        
        return (finalmi, finalma)
numeros = [12, 45, 2, 8, 33, 1,100]
print(mx_mn(numeros))