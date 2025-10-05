c = int(input()) #km/l
d = int(input()) #distancia
t = int(input()) #tanque atual

dist_litros = d / c
litros = dist_litros - t

if litros <= 0:
    litros = 0
    
print(f"{litros:.1f}")