def suma(A, i):
    if i == 1:
        return A[0]
    else:
        print(A,i)
        return suma(A,i-1) + A[i-1]

print(suma([10, 20, 30, 40],3))