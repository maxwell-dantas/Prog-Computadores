monica = int(input())
filho_1 = int(input())
filho_2 = int(input())
filho_3 = monica - filho_1 - filho_2

if (filho_1 >= filho_2) and (filho_1 >= filho_3):
    maior = filho_1
elif (filho_2 >= filho_1) and (filho_2 >= filho_3):
    maior = filho_2
else:
    maior = filho_3

print(maior)