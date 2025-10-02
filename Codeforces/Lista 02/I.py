l, d = map(int, input().split())
k, p = map(int, input().split())
pedagio = l // d
custo_total = (k * l) + (pedagio * p)
print(custo_total)