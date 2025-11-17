def raiz_rec(n, r):
    nova_raiz = (r + n / r) / 2
    if abs(nova_raiz - r) < 0.001:
        raiz_formatada = f"{nova_raiz:.3f}"
        return raiz_formatada
    else:
        return raiz_rec(n, nova_raiz)
    

def raiz(n):
    return raiz_rec(n, n)
