def sum(A,n):
    if len(A) <= 1:
        return A
    else:
        return sum(A, n-1) + A[n-1]