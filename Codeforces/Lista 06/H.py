def media_lista(lista):
    soma = 0
    elementos = 0
    for i in lista:
        soma += i
        elementos += 1
    media = soma // elementos
    return media
