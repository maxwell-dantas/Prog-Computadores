jogadores, rodadas = map(int, input().split())
pontos_vitoria = list(map(int, input().split()))
lista_jogadores = []

for i in range(jogadores):
    lista_jogadores.append(pontos_vitoria[i])

for j in range(jogadores, len(pontos_vitoria)):
    ciclo_pontos = j % jogadores
    lista_jogadores[ciclo_pontos] += pontos_vitoria[j]

maior = lista_jogadores[0]
jogador_vencedor = 1

for x in range(1, len(lista_jogadores)):
    if lista_jogadores[x] >= maior:
        maior = lista_jogadores[x]
        jogador_vencedor = x + 1

print(jogador_vencedor)