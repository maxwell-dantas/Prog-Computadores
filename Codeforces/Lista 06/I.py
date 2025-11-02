def lista_troca_menor_primeiro(lista):
    indice = 0
    menor = lista[0]
    troca = 0
    for i in lista:
        if menor > i:
            lista[indice] = i
            troca += 1
            indice += 1
    return menor

lista = list(map(int, input().split()))
print(lista_troca_menor_primeiro(lista))