msg_cifrada = list(input())
msg_crib = list(input())
cont = 0
 
for i in range(len(msg_cifrada) - len(msg_crib) + 1):
    verificador = True
    for j in range(len(msg_crib)):
        if msg_cifrada[i + j] == msg_crib[j]:
            verificador = False
            break
    if verificador:
        cont += 1 
 
print(cont)