a, b = map(int, input().split())
 
multiplos_a = [a]
 
for i in range(a + 1, b + 1):
    if (i % a == 0):
        multiplos_a.append(i)
 
print(*multiplos_a)