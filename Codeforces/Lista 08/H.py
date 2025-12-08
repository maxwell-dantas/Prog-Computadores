while True:
    num_amostras = int(input())
    
    if num_amostras == 0:
        break
    
    seq_mag = list(map(int, input().split()))
    picos = 0

    for i in range(num_amostras):
        indice_esq = (i - 1) % num_amostras
        indice_dir = (i + 1) % num_amostras

        if seq_mag[i] > seq_mag[indice_esq] and seq_mag[i] > seq_mag[indice_dir]:
            picos += 1
        elif seq_mag[i] < seq_mag[indice_esq] and seq_mag[i] < seq_mag[indice_dir]:
            picos += 1
            
    print(picos)