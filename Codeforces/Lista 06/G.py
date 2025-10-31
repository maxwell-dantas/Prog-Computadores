def dia(dia, mes, ano):
    flag_data = True
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho",
             "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    if (mes < 1) or (mes > 12): #Verificação dos meses
        flag_data = False
    
    if flag_data:
        if (mes == 2) and ((dia < 1) or (dia > 28)): #Verificação do mês de Fevereiro
            flag_data = False
        elif (mes in [4, 6, 9, 11]) and ((dia < 1) or (dia > 30)): #Verificação dos meses terminados no dia 30
            flag_data = False
        elif (dia < 1) or (dia > 31): #Verificação dos meses terminados no dia 31
            flag_data =  False
    
    if flag_data:
        mes = meses[mes - 1]
        data = f"{dia:02d} de {mes} de {ano}"
    else:
        data = "Data Invalida"
    return data
