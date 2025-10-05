b = int(input())
t = int(input())

area_nota = 160 * 70
area_felix = (b + t) * 70 // 2
area_metade = area_nota // 2

if area_felix > area_metade:
    print("1")
elif area_felix < area_metade:
    print("2")
else:
    print("0")