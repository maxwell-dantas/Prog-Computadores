# Escreva uma função recursiva que receba uma lista l e inverta a ordem dos elementos da lista, trocando o
# primeiro com o último, o segundo com o penúltimo, o terceiro com com antepenúltimo, até que a lista fique
# totalmente invertida.
# Se a função receber a lista [1,2,3,4,5], deve retornar a lista [5,4,3,2,1] .
# Assinatura da função: def inveter_lista(lista)
# Dica: Defina parâmetros para auxilar no controle da recursividade.

def inveter_lista(lista):
    if (len(lista) == 1):
        return [lista[0]]
    return [lista[-1]] + inveter_lista(lista[:-1])
