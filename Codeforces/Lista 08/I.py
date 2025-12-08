caso = 0
while True:
    try:
        senha_alg = int(input())
        teclas = list(map(float, input().split()))
        senha_user = ""
        caso += 1

        for i in range(senha_alg):
            maior_indice = 0
            for j in range(len(teclas)):
                if teclas[j] > teclas[maior_indice]:
                    maior_indice = j
            teclas[maior_indice] = -1
            senha_user += str(maior_indice)

        print(f"Caso {caso}: {senha_user}")
    except EOFError:
        break