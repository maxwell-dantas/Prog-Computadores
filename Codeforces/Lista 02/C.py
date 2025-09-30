nome = str(input())
sal_fixo = float(input())
total_vendas = float(input())
comissao = (total_vendas * 0.15) + sal_fixo

print(nome)
print(f'R$ {comissao:.2f}')