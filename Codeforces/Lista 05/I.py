a1 = int(input())
a2 = int(input())
a3 = int(input())

caso_1 = (a2 * 2) + (a3 * 4)
caso_2 = (a1 * 2) + (a3 * 2)
caso_3 = (a1 * 4) + (a2 * 2)

if caso_1 <= caso_2 and caso_1 <= caso_3:
    menor = caso_1
elif caso_2 <= caso_1 and caso_2 <= caso_3:
    menor = caso_2
else:
    menor = caso_3

print(menor)