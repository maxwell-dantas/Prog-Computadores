# Escreva uma função recursiva que receba um número inteiro n e retorne uma lista com os divisores de n.
# Assinatura da função: def divisores(n,k)

def divisores(n,k):
    if (k == 0):
        return []
    
    if (k > 0):
        if (n % k == 0):
            return divisores(n, k-1) + [k]
        else:
            return divisores(n, k-1)
    else:
        if (n % k == 0):
            return divisores(n, k+1) + [k]
        else:
            return divisores(n, k+1)

        
def divisores_auxiliar(n):
    positivo = divisores(n, n)
    negativos = divisores(n, -n)
    return negativos + positivo

x = int(input("Digite um número inteiro: "))

print(f"Todos os divisores possíveis do número {x} = {divisores_auxiliar(x)}")
