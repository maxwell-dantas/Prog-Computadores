# A expressão a seguir deveria calcular a média aritmética entre 7 e 9.5: 7+9.5/2.
# O resultado não é o esperado. Isso acontece porque a divisão é realizada antes de somar.
# Para resolver este problema deve-se colocar em prioridade a soma.
# Em Python3 usa-se os parênteses. A expressão correta é (7+9.5)/2. Verifique e confirme.

media_errada = 7 + 9.5 / 2
print(media_errada)

media_corrigida = (7 + 9.5) / 2
print(media_corrigida)