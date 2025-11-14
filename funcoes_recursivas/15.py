# Escreva uma função recursiva Pn(x). A função deve receber como parâmetro uma lista (array) com os coeficientes
# do polinômio e o valor de x.
# Assinatura da função: def polinomio(coeficientes,x)

def polinomio(coeficientes,x):
    if (len(coeficientes) == 1):
        return coeficientes[0]
    
    elemento = coeficientes[-1]
    p = x * polinomio(coeficientes[:-1], x) + elemento

    return p