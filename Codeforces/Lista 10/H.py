def valida_sequencia(a:int, b:int, seq_A:list, seq_B:list) -> bool:
  ultimo_indice_encontrado = -1
  for i in range(b):
    validacao = False
    ultimo_indice_encontrado += 1
    for j in range(ultimo_indice_encontrado, a):
      if seq_B[i] == seq_A[j]:
        ultimo_indice_encontrado = j
        validacao = True
        break
    if not validacao:
      return False
  return True

a, b = map(int, input().split())
seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))
validacao = valida_sequencia(a, b, seq_A, seq_B)

if validacao:
  print("S")
else:
  print("N")
