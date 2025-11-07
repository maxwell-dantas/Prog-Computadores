# Escreva uma função recursiva que determine quantos bits são necessários para representar um determinado
# número, ignorando os zeros a esquerda.
# Exemplo: Para o número 4312 são necessários 13 bits, pois 4312(10) = 1000011011000(2)
# Assinatura da função: def conta_bits(n)

def conta_bits(n):
    if (n <= 1):
        return 1
    else:
        return 1 + conta_bits(n // 2)

x = int(input("Digite um número inteiro: "))

print(f"A quantidade de bits necessários para o numero: {x} é {conta_bits(x)}")
