num_medicoes = int(input())
lista_batimentos = []

for i in range(num_medicoes):
    batimentos = int(input())
    lista_batimentos.append(batimentos)

media = sum(lista_batimentos) // len(lista_batimentos)
variacao = 0

limite_inferior = (media * 90) // 100
limite_superior = (media * 110) // 100

for batimento in lista_batimentos:
    if batimento < limite_inferior or batimento > limite_superior:
        variacao += 1
        
print(media)
print(variacao)