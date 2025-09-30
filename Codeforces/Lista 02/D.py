valor_item = int(input())
quant_itens = int(input())
valor_pago = int(input())
total = valor_item * quant_itens
troco = valor_pago - total

print(f'A pagar: {total}')
print(f'Troco  : {troco}')