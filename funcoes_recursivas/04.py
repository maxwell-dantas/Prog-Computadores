# Escreva uma função recursiva que determine quantos algarismos 
# são necessários para representar um determinado número, 
# ignorando os zeros a esquerda.
# Assinatura da função: def conta_algarismos(n)

def conta_algarismos(n):
    if (n >= 0):
        if (n < 10):
            return 1
        else:
                return 1 + conta_algarismos((n // 10))
        
    if (n > - 10):
        return 1
    else:
            return 1 + conta_algarismos((n // 10))
         
x = int(input("Digite um número inteiro: "))

print(f"A quantidade de algarismos para o numero: {x} é {conta_algarismos(x)}")
