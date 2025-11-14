def primo_r(num, div):
    if num <= 1:
        return False
    if div == 1:
        return True
    if (num % div == 0):
        return False
    return primo_r(num, div-1)

def primos(lista):
    if not lista:
        return []
    
    if len(lista) == 1:
        n = lista[0]
        if n <= 1 or not primo_r(n, n-1):
            return []
        else:
            return [n]

    elemento = lista[-1]

    if elemento <= 1:
        return primos(lista[:-1])
    if primo_r(elemento, elemento-1):
        return primos(lista[:-1]) + [elemento]
    else:
        return primos(lista[:-1])