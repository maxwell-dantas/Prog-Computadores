a, g, ra, rg = map(float, input().split())

if (a / ra) < (g / rg):
    print("A")
elif (a / ra) > (g / rg):
    print("G")
else:
    print("G")