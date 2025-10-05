cap_cabine = int(input())
quant_alunos = int(input())

viagem_alunos = quant_alunos // (cap_cabine - 1)

if (quant_alunos % (cap_cabine - 1)) != 0:
    viagem_alunos = viagem_alunos + 1
    
print(viagem_alunos)