l = int(input())
c = int(input())

impar = (l % 2) != 0 and (c % 2) != 0
par = (l % 2) == 0 and (c % 2) == 0

if (par == True) or (impar == True):
    print("1")
else:
    print("0")