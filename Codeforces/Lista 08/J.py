def cria_lista_id_voluntarios(numeracao):
    lista_voluntarios_dive = []
    for i in range(1, numeracao + 1):
        lista_voluntarios_dive.append(i)
    return lista_voluntarios_dive

def retira_id_voluntarios(id_dive, id_true_return):
    voluntarios_dive = cria_lista_id_voluntarios(id_dive)
    qtd_voluntarios_true_return = id_true_return

    conjunto_dive = set(voluntarios_dive)
    conjunto_true_return = set(qtd_voluntarios_true_return)
    diff = list(conjunto_dive - conjunto_true_return)

    return diff
    
num_voluntarios_dive, num_voluntarios_return = map(int, input().split())
num_voluntarios_true_return = list(map(int, input().split()))

not_voluntarios_return = retira_id_voluntarios(num_voluntarios_dive, num_voluntarios_true_return)
not_voluntarios_return.sort()
print(not_voluntarios_return)

if len(not_voluntarios_return) == 0:
    print("*")
else:
    for i in not_voluntarios_return:
        print(i, end=" ")