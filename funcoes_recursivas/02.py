# Escreva uma função recursiva que receba um número inteiro, não negativo, e retorne se ele é primo.
# Assinatura da função: def primo(n)

def primo_r(num, div):
    if (div == 1):
        return True
    
    if (num % div == 0):
        return False
    else:
        return primo_r(num, div-1)

def primo(num):
    if (num <= 1):
        return "não é primo!"
    
    resultado = primo_r(num, num-1)

    if (resultado):
        return "é primo!"
    else:
        return "não é primo!"

x = int(input("Digite um número natural: "))

print(f"O número {x} {primo(x)}")