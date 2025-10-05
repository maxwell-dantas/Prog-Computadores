a, b, c = map(int, input().split())

if not ((a < b + c) and (b < a + c) and (c < a + b)):
    print("n")
else:    
    if (a >= b) and (a >= c):
        if (a**2 == b**2 + c**2):
            print("r")
        elif (a**2 > b**2 + c**2):
            print("o")
        else:
            print("a")
            
    elif (b >= a) and (b >= c):
        if (b**2 == a**2 + c**2):
            print("r")
        elif (b**2 > a**2 + c**2):
            print("o")
        else:
            print("a")

    else:
        if (c**2 == a**2 + b**2):
            print("r")
        elif (c**2 > a**2 + b**2):
            print("o")
        else:
            print("a")