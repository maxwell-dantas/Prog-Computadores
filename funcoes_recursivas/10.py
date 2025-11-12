# Escreva uma função recursiva que determine se os elementos de uma lista estão ordenados. A função deve
# retornar um valor lógico (boolean). Em Python os possíveis valores lógicos são True ou False.
# Assinatura da função: def ordenada(lista)

def ordenada(lista):
    if (len(lista) <= 1):
        return True
    
    if (lista[-1] > lista[-2]):
        return ordenada(lista[:-1])
    else:
        return False