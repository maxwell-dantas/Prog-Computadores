def lista_troca_menor_primeiro(lista):
    cont_trocas = 0
    cont = 0
    menor = lista[0]
    posicao_menor = 0
 
    for i in lista:
        cont += 1
        if i < menor:
            menor = i
            posicao_menor = cont - 1
 
    if (lista[0]) > lista[posicao_menor]:
        menor = lista[posicao_menor]
        lista[posicao_menor] = lista[0]
        lista[0] = menor
        cont_trocas += 1
 
    return cont_trocas
