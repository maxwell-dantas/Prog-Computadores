num_dive, num_return = map(int, input().split())
retornou = list(map(int, input().split()))
lista_id = []
for i in range(1, num_dive + 1):
    if i not in retornou:
        lista_id.append(i)
lista_id.sort()

if len(lista_id) == 0:
    print("*")
else:
    for i in lista_id:
        print(i, end=" ")