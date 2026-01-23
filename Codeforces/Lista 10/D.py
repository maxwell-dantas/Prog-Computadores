def segredo_imperador(lista:list, tamanho:int) -> int:
    maior_sequencia = 1
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if lista[i] == lista[j]:
                continue
            atual = lista[i]
            proximo = lista[j]
            maior_sequencia_atual = 2
            for k in range(j + 1, tamanho):
                if lista[k] == atual:
                    maior_sequencia_atual += 1
                    atual, proximo = proximo, atual
            if maior_sequencia_atual > maior_sequencia:
                maior_sequencia = maior_sequencia_atual
    return maior_sequencia
 
def pega_sequencia(tamanho:int) -> list:
    sequencia = []
    for _ in range(tamanho):
        numero = int(input())
        sequencia.append(numero)
    return sequencia
 
tamanho_sequencia = int(input())
sequencia_inserida = pega_sequencia(tamanho_sequencia)
print(segredo_imperador(sequencia_inserida, tamanho_sequencia))