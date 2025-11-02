def sublista_sem_menor(lista):
    menor = lista[0]
    cont = 0
    nova_lista = []
    flag_num = False

    for i in lista:
        cont += 1
        if (i < menor):
            menor = i   

    for i in range(cont):
        if ((lista[i] == menor) and (flag_num == False)):
            flag_num = True
        else:
            nova_lista += [lista[i]]

    return nova_lista
