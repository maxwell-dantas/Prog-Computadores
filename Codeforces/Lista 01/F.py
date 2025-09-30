a, b = map(int, input().split())
peso_1, peso_2 = map(int, input().split())
media = (a * peso_1 + b * peso_2) // (peso_1 + peso_2)
print(media)