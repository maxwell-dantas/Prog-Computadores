cont = 0

def ackermann(m, n):
    global cont
    cont += 1
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 0)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
