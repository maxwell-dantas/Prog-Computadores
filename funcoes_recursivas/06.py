# # Uma combinação sem repetição, em análise combinatória, é um subconjunto com k elementos em um conjunto
# # U, com n elementos.
# Assinatura da função: def comb(n,k)

def comb(n, k):
    if (n == k):
        return 1
    elif (k == 1):
        return n
    else:
        return comb(n-1, k-1) + comb(n-1, k)
