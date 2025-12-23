teste = 1
while True:
    num_regioes = int(input())

    if num_regioes == 0:
        break

    x, y, u, v = map(int, input().split())
    
    for i in range(num_regioes - 1):
        x2, y2, u2, v2 = map(int, input().split())

        x = max(x, x2)
        y = min(y, y2)
        u = min(u, u2)
        v = max(v, v2)

    print(f"Teste {teste}")
    teste += 1

    if x < u and y > v:
        print(x, y, u, v)
    else:
        print("nenhum")

    print()