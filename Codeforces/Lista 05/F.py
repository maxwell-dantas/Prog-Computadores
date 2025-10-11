carne_D, bife_D, massa_D = map(int, input().split())
carne_P, bife_P, massa_P = map(int, input().split())

carne = carne_D - carne_P
bife = bife_D - bife_P
massa = massa_D - massa_P

soma_1 = 0
soma_2 = 0
soma_3 = 0

if carne < 0:
    soma_1 = abs(carne)

if bife < 0:
    soma_2 = abs(bife)

if massa < 0:
    soma_3 = abs(massa)

soma = soma_1 + soma_2 + soma_3

print(soma)