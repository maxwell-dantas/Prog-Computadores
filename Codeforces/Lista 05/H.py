a = int(input())
b = int(input())
c = int(input())
d = int(input())

dif_1 = abs((a + b) - (c + d))
dif_2 = abs((a + c) - (b + d))
dif_3 = abs((a + d) - (b + c))

if dif_1 <= dif_2 and dif_1 <= dif_3:
    menor = dif_1
elif (dif_2 <= dif_1) and (dif_2 <= dif_3):
    menor = dif_2
else:
    menor = dif_3 

print(menor)