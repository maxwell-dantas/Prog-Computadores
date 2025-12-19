def soma_alg(num):
    soma = 0
    while num > 0:
        ult_alg = num % 10
        soma += ult_alg
        num //= 10
    return soma

while True:

    n, m = map(int, input().split())

    if (n == 0 and m == 0):
        break

    while n > 9:
        n = soma_alg(n)
    
    while m > 9:
        m = soma_alg(m)

    if n > m:
        maior = 1
    elif n < m:
        maior = 2
    else:
        maior = 0
    
    print(maior)