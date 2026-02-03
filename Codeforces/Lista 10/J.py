def escada_perfeita(num_elementos, lista):
  contador = 0
  for i in range(len(lista)):
    num_elementos -= 1
    for j in range(1, num_elementos + 1):
      if lista[i] > lista[-j]:
        diferenca = lista[i] - lista[-j]
        lista[i] -= diferenca
        lista[-j] += diferenca
        contador += diferenca
      elif lista[i] == lista[-j]:
        lista[i] -= 1
        lista[-j] += 1
        contador += 1
  for i in range(1, len(lista)):
    if lista[i] - lista[i - 1] != 1:
      return -1
  return contador

quantidade_pilhas = int(input())
pilha = list(map(int, input().split()))
print(escada_perfeita(quantidade_pilhas, pilha))