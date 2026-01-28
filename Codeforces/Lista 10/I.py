def sequencias_pa(elementos:int, sequencia:list) -> int:
  if elementos <= 2:
    return 1
  
  diferenca_anterior = sequencia[1] - sequencia[0]
  contador = 1
  validador = True

  for i in range(2, elementos):
    if not validador:
      diferenca_anterior = sequencia[i] - sequencia[i - 1]
      validador = True
      continue
    diferenca_atual = sequencia[i] - sequencia[i - 1]
    if diferenca_atual != diferenca_anterior:
      contador += 1
      validador = False
  return contador

numero_elementos = int(input())
sequencia = list(map(int, input().split()))
print(sequencias_pa(numero_elementos, sequencia))