def dia_da_semana(h, d):
    dias_da_semana = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira",
       "Sexta-feira", "Sabado"]
    
    indice_hoje = 0

    while (dias_da_semana[indice_hoje]!= h):
        indice_hoje += 1

    indice_futuro = (indice_hoje + d) % 7
    return dias_da_semana[indice_futuro]
