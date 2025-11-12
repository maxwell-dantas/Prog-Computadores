# Escreva uma função recursiva que receba uma lista de números inteiros e retorne o índice do maior elemento.
# Assinatura da função: def indice_do_maior(lista)

def indice_do_maior(lista):
    if (len(lista) == 1):
        return 0
    
    maior_indice = indice_do_maior(lista[:-1])
    ultimo_elemento = len(lista) - 1

    if (lista[maior_indice] < lista[ultimo_elemento]):
        maior_indice = len(lista) - 1
    return maior_indice