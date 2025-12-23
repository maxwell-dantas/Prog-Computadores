n = int(input())
seq = list(map(int, input().split()))

if n <= 2:
    cont = 1
else:
    cont = 1

    diff_anterior = seq[1] - seq[0]

    for i in range(2, n):
        diff_atual = seq[i] - seq[i - 1]

        if diff_atual != diff_anterior:
            diff_anterior = diff_atual
            cont += 1

print(cont)