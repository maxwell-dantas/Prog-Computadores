dist = int(input())
vel = int(input())
med = dist / vel
hora = int(med)
min = int((med - hora) * 60)
print(f'{hora:02d}:{min:02d}')