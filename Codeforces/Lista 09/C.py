serie = int(input())
num_serie = list(map(int, input().split()))

estado_a = 0
estado_b = 0

for i in range(serie):
    if (num_serie[i] == 1):
        if (estado_a == 0):
            estado_a = 1
        else:
            estado_a = 0
    else:
        if (estado_a == 0):
            estado_a = 1
        else:
            estado_a = 0
        
        if (estado_b == 0):
            estado_b = 1
        else:
            estado_b = 0

print(estado_a)
print(estado_b)