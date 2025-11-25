cases = int(input())
lista = list(map(int, input().split()))
  
if (cases == 0):
    print(0.0)
    print(0)
    print(0)
else:
    soma = 0
    abaixo_media = []
    acima_igual_media = []
    
    for i in range(cases):
        soma += lista[i]
    
    media = soma / cases
    
    for i in lista:
        if (i < media):
            abaixo_media.append(i)
        else:
            acima_igual_media.append(i)
            
    abaixo_media.insert(0, len(abaixo_media))
    acima_igual_media.insert(0, len(acima_igual_media))
    
    print(f"{media:.1f}")
    print(*abaixo_media)
    print(*acima_igual_media)
