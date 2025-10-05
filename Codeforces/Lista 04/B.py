a, b, c, d = map(int, input().split())

abc = (a < b + c) and (b < a + c) and (c < a + b)
abd = (a < b + d) and (b < a + d) and (d < a + b)
acd = (a < c + d) and (c < a + d) and (d < a + c)
bcd = (b < c + d) and (c < b + d) and (d < b + c)

if (abc == True) or (abd == True) or (acd == True) or (bcd == True):
    print("S")
else:
    print("N")