casos = int(input())
troco_maximo = []

for i in range(casos):
    valor, qtd_marca = map(int, input().split())
    preco_marca = list(map(float, input().split()))
    lista_troco_por_item = []
    
    for j in preco_marca:
        if j <= valor:
            troco_por_item = valor % j
            lista_troco_por_item.append(troco_por_item)
        else:
            troco_por_item = 0
            lista_troco_por_item.append(troco_por_item)
    troco_maximo.append(max(lista_troco_por_item))

for troco in range(casos):
    print(f"{troco_maximo[troco]:.2f}")