a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (a >= c):
    if b >= c:
        idade = b
    else:
        idade = c
elif (b >= a) and (b >= c):
    if a >= c:
        idade = a
    else:
        idade = c
elif (c >= a) and (c >= b):
    if a >= b:
        idade = a
    else:
        idade = b

print(idade)