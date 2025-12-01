altura_pulo, numero_canos = map(int, input().split())
lista_canos = list(map(int, input().split()))

tamanho_lista = len(lista_canos)
indice = 0

while indice < tamanho_lista - 1:
    diff = abs(lista_canos[indice] - lista_canos[indice + 1])
    if diff <= altura_pulo:
        indice += 1
    else:
        indice = -1
        break

if indice >= 0:
    print("YOU WIN")
else:
    print("GAME OVER")
