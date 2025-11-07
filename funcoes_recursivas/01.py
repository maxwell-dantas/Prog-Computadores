# Escreva uma função recursiva que receba um inteiro n, não negativo, e retorne a quantidade de divisores de n.
# Assinatura da função: def conta_divisores(n)

def conta_divisores_r(n, div):
    if (div == 1):
        divisores = 1
    else:
        if (n % div == 0):
            divisores = 1 + conta_divisores_r(n, (div - 1))
        else:
            divisores = conta_divisores_r(n, (div - 1))
    return divisores

def conta_divisores(n):
    if (n == 0):
        divisores = "INDETERMINADO"
    else:
        divisores = conta_divisores_r(n, n)
    return divisores

x = int(input("Digite um número natural: "))

print(f"A quantidade de divisores do número {x} é = {conta_divisores(x)}")
