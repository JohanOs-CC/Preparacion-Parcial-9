def Lucas(n: int):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        Lu = [2,1]
        while len(Lu) < n:
            Lu.append(Lu[-2]+Lu[-1])
    return Lu[-1]
print(Lucas(9))