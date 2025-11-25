cases = int(input())
lista = list(map(int, input().split()))
 
if (cases == 0):
    print(0.0)
    print(0)
    print(0)
else:
    soma = 0
    abaixo_media = 0
    acima_igual_media = 0
    
    for i in range(cases):
        soma += lista[i]
        
    media = soma / cases
    
    for i in range(cases):
        if lista[i] < media:
            abaixo_media += 1
        else:
            acima_igual_media +=1
            
    print("{:.1f}".format(media))
    print(abaixo_media)
    print(acima_igual_media)
