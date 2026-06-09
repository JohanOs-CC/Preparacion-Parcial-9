def ex_r(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    
    mitad = ex_r(x,n//2)

    if n % 2 == 1:
        return mitad * mitad * x
    else:
        return mitad * mitad
print(ex_r(2,5))
