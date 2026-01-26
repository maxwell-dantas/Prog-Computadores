def validacao_batalha(quantidade_navios, tabuleiro):
  valido = True
  for i in range(quantidade_navios):
        d, l, r, c = map(int, input().split())

        if not valido:
           continue
    
        r -= 1
        c -= 1
        if (d == 0):
            indice_final = c + l - 1
            if r >= 0 and r <= 9 and indice_final >= 0 and indice_final <= 9:
                for j in range(c, indice_final + 1):
                  if tabuleiro[r][j] == False:
                    tabuleiro[r][j] = True
                  else:
                    valido = False
                    break
            else:
                valido = False   
        else:
            indice_final = r + l - 1
            if c >= 0 and c <= 9 and indice_final >= 0 and indice_final <= 9:
                for j in range(r, indice_final + 1):
                    if tabuleiro[j][c] == False:
                      tabuleiro[j][c] = True
                    else:
                      valido = False
                      break
            else:
                valido = False
  return valido
              
quantidade_navios = int(input())
tabuleiro = [[False for _ in range(10)] for _ in range(10)]
 
if validacao_batalha(quantidade_navios, tabuleiro):
    print("Y")
else:
    print("N")