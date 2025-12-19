n = int(input())
n_caracteres = list(input())
cont = 0
i = 0
while i < n:
    if n_caracteres[i] == "a":
        num_a = 1
 
        while i + 1 < n and n_caracteres[i + 1] == "a":
            num_a += 1
            i += 1
 
        if num_a >= 2:
            cont += num_a
    i += 1
 
print(cont)