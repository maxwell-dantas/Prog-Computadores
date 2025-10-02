largura = int(input())
comprimento = int(input())

lajota_1 = largura * comprimento
espacos = (largura - 1) * (comprimento - 1)
lajota_1_total = lajota_1 + espacos
lajota_2 = (largura - 1 ) * 2 + (comprimento - 1) * 2

print(lajota_1_total)
print(lajota_2)