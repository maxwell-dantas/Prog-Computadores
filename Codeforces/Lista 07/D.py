a = int(input())
divisores_a = []

for i in range(1, a + 1):
    if (a % i == 0):
        divisores_a.append(i)
 
print(*divisores_a)