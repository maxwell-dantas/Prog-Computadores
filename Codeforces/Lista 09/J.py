num_comp = int(input())
num_comp_pass = int(input())
nota_comp = []

for i in range(num_comp):
    comp = int(input())
    nota_comp.append(comp)
nota_comp.sort()

cont = num_comp_pass
ultimo_colocado = nota_comp[num_comp - num_comp_pass]

for j in range(num_comp - num_comp_pass, 0, - 1):

    if nota_comp[j - 1] >= ultimo_colocado:
        cont += 1

print(cont)