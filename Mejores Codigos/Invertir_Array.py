def inv(A):
    if len(A) <= 1:
        return A
    else:
        return inv(A[1:]) + [A[0]]

print(inv([1,2,3,4,5]))