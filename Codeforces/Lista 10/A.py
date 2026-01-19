def pega_estoque(numero_itens):
    lista_tamanhos = []
    for item in range(numero_itens):
        estoque = int(input())
        lista_tamanhos.append(estoque)
    return lista_tamanhos
 
def reduz_estoque(lista, pedidos):
    cont = 0
    for numero_pedidos in range(pedidos):
        pedido = int(input())
        pedido -= 1
        if pedido >= 0 and pedido <= len(lista) - 1:
            if lista[pedido] > 0:
                lista[pedido] -= 1
                cont += 1
    return cont
 
num_tamanhos = int(input())
estoque = pega_estoque(num_tamanhos)
num_pedidos = int(input())
pedidos_aceitos = reduz_estoque(estoque, num_pedidos)
print(pedidos_aceitos)