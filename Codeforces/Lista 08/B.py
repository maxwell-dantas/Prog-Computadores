def timer(time):
    dias = time // 86400
    resto = time % 86400
    horas = resto // 3600
    resto = time % 3600
    minutos = resto // 60
    segundos = resto % 60

    horario_formatado = f"{dias} dias {horas:02d}:{minutos:02d}:{segundos:02d}"
    return horario_formatado

tempo, massa_inicial = map(int, input().split())
cont = 0

while massa_inicial >= 0.5:
    massa_inicial /= 2
    cont += 1

segundos_totais = tempo * cont

print(timer(segundos_totais))