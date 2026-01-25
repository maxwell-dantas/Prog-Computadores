def ordem_cores(qtd_quadrados, quadrados) -> list:
  quadrados_numerados = [10001 for x in range(qtd_quadrados)]
  for i in range(qtd_quadrados):
    if quadrados[i] == 0:
      for j in range(qtd_quadrados):
        if quadrados[j] == 0:
          quadrados_numerados[j] = 0
          continue
        if abs(i - j) < quadrados_numerados[j]:
          if abs(i - j) >= 9:
            quadrados_numerados[j] = 9
          else:
            quadrados_numerados[j] = abs(i - j)
  return quadrados_numerados

qtd_quadrados = int(input())
quadrados = list(map(int, input().split()))

print(*(ordem_cores(qtd_quadrados, quadrados)))