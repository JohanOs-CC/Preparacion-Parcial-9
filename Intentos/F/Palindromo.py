def palindromo(A):
    
    n = len(A)

    for i in range(n // 2):
        if A[i] != A[n - 1 - i]:
            print(f"Fallo en: {A[i]} vs {A[n - 1 - i]}")
            return False 
    return True


print(palindromo([1, 2, 3, 2, 1])) 
print(palindromo([4, 7, 2, 9, 1])) 