# Escreva uma função recursiva que receba uma lista de números inteiros e mostre a soma dos números pares
# da lista.
# Assinatura da função: def soma_pares(lista)

def soma_pares(lista):
    if (len(lista) == 1):
        if (lista[0] % 2 == 0):
            return lista[0] 
        else:
            return 0
    elemento = lista[-1]
    if (elemento % 2 == 0):
        return elemento + soma_pares(lista[:-1])
    else:
        return soma_pares(lista[:-1])
