consumo = int(input())

if consumo <= 10:
    price = 7
elif consumo <= 30:
    price = 7 + (consumo - 10) * 1
elif consumo <= 100:
    price = 7 + 20 + (consumo - 30) * 2
elif consumo >= 101:
    price = 7 + 20 + 140 + (consumo - 100) * 5

print(price)