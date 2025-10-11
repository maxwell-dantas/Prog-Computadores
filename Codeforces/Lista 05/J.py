a1, a2, a3, a4 = map(int, input().split())

if (a1 * a2) == (a3 * a4) or (a1 * a3) == (a2 * a4) or (a2 * a3) == (a1 * a4):
    print("S")
else:
    print("N")