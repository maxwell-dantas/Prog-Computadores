nome = str(input())
quant_hora = int(input())
valor_hora = float(input())
pagamento = quant_hora * valor_hora

print(nome)
print('R$ {:.2f}'.format(pagamento))