def candidatos(competidores, ponto_min):
    candidatos_aceitos = 0
    for i in range(competidores):
        fase_a, fase_b = map(int, input().split())
        if (fase_a + fase_b >= ponto_min):
            candidatos_aceitos += 1
    return candidatos_aceitos
 
num_competidores, ponto_minimo = map(int, input().split())
aceitos = candidatos(num_competidores, ponto_minimo)
print(aceitos)