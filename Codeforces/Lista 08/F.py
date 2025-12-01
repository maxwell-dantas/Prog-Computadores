h1, m1, h2, m2 = map(int, input().split())
lista_minutos = []

while (h1 != 0 or m1 != 0 or m2 != 0 or h2 != 0):
    minutos_atuais = h1 * 60 + m1
    minutos_alarme = h2 * 60 + m2

    diff = minutos_alarme - minutos_atuais

    if diff < 0:
        diff += 24 * 60
    
    lista_minutos.append(diff)

    h1, m1, h2, m2 = map(int, input().split())

for i in range(len(lista_minutos)):
    print(lista_minutos[i])
