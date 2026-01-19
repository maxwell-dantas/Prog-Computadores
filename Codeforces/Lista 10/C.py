def maior_sequencia(texto):
    cont = 1
    maior = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            cont += 1
        else:
            if cont > maior:
                maior = cont
            cont = 1
    if cont > maior:
        maior = cont
    return maior
    
dna = str(input())
print(maior_sequencia(dna))