def sequencia_saltadora(sequencia:list) -> bool:
  sequencia_bool = True
  valor_n = sequencia[0]
  lista_validacao = []

  if valor_n == 1:
    return sequencia_bool

  for i in range(2, len(sequencia)):
    diferenca = abs(sequencia[i] - sequencia[i - 1])
    if diferenca < 1 or diferenca > valor_n - 1:
      sequencia_bool = False
      break
    else:
      if diferenca not in lista_validacao:
        lista_validacao.append(diferenca)
      else:
        sequencia_bool = False
        break

  return sequencia_bool

while True:
  try:
    lista = list(map(int, input().split()))
    valida_sequencia = sequencia_saltadora(lista)
    if valida_sequencia:
      print("Alegre")
    else:
      print("Nao alegre")
  except EOFError:
    break
