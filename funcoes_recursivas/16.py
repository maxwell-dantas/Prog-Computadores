# Escreva uma função recursiva que receba duas listas l1 e l2 de números inteiros, ordenadas, e crie uma terceira
# lista, l3, contendo todos os elementos de l1 e l2. A lista l3 deve ter os elementos ordenados.
# Considere l1 = [1, 3, 11, 13] e l2 = [2, 4, 10, 12].
# A lista retornada de ser [1, 2, 3, 4, 10, 11, 12, 13] .
# Assinatura da função: def junta(l1, l2)
# Dica 1: O caso de base é quando uma das listas é vazia. Nesse caso a função retorna a outra lista.
# Dica 2: O caso geral verifica o maior elemento de cada lista, que é obrigatoriamente o último, e chama a função
# passando as listas, onde o maior elemento é removido da respectiva lista, para ser adicionado na lista de retorno.

def junta(l1, l2):
    if (len(l1) == 0):
        return l2
    if (len(l2) == 0):
        return l1
    
    if (l1[-1] > l2[-1]):
        return junta(l1[:-1], l2) + [l1[-1]]
    else:
        return junta(l1, l2[:-1]) + [l2[-1]]