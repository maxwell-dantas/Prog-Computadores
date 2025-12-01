def leitura_dados(quantidade_casos):
    lista_suprimentos = []
    for i in range(quantidade_casos):
        qtd_suprimento = float(input())
        lista_suprimentos.append(qtd_suprimento)
    return lista_suprimentos

def calcular_dias(lista_suprimentos):
    for i in range(len(lista_suprimentos)):
        cont_dias = 0
        suprimento_inicial = lista_suprimentos[i]
        while suprimento_inicial > 1:
            suprimento_inicial /= 2
            cont_dias += 1
        print(f"{cont_dias} dias")

casos = int(input())
dados_lidos = leitura_dados(casos)
dados_processados = calcular_dias(dados_lidos)
