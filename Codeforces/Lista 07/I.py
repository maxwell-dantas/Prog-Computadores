num_simulacoes = int(input())
qnt_acertos = 0
 
for i in range(num_simulacoes):
    carro = int(input())
    if (carro != 1):
        qnt_acertos += 1
 
print(qnt_acertos)