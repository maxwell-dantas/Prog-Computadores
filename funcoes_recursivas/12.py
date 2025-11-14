# Escreva uma função recursiva que receba uma lista l de números inteiros e um número inteiro x. A função deve
# retornar quantas vezes x ocorre na lista.
# Assinatura da função: def ocorrencias(lista, x)

def ocorrencias(lista, x):
    if (len(lista) == 1):
        if (lista[0] == x):
            return 1
        else:
            return 0
          
    elemento = lista[-1]

    if (elemento == x):
        return 1 + ocorrencias(lista[:-1], x)
    else:
        return ocorrencias(lista[:-1], x)