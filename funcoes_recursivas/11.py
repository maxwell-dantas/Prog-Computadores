# Escreva uma função recursiva que receba uma lista l1 de números inteiros e retorne uma outra lista l2 com os
# números primos de l1.
# Assinatura da função: def primos(lista)
# Obs: Use a função primo(), feita anteriormente, para determinar se um número é primo.

def primo_r(num, div):
    if (div == 1):
        return True
    if (num % div == 0):
        return False
    else:
        return primo_r(num, div-1)

def primo(lista):
    if (len(lista) == 1):
        if (lista[0] <= 1 or not(primo_r(lista[0], lista[0] - 1))):
            return []
        else:
            if (primo_r(lista[0], lista[0] - 1)):
                return [lista[0]]

    elemento = lista[-1]
    verificador_primo = primo_r(elemento, elemento-1)

    if verificador_primo:
        return primo(lista[:-1]) + [elemento]
    else:
        return primo(lista[:-1])