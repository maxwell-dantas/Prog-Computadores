cases = int(input())
qtd_seq = 0

if (cases > 0):

    lista = []

    for i in range(cases):
        num_seq = int(input())
        lista.append(num_seq)

    for i in range(cases):
        if (i < len(lista) - 1):
            if (lista[i] != lista[i + 1]):
                qtd_seq += 1
        else:
            qtd_seq += 1
    
print(qtd_seq)