# Escreva uma função recursiva que receba uma string s e retorne se a mesma é um palíndromo.
# Um palíndromo é um texto que possui a mesma sequencia de letras tanto lido da esquerda para a direita como
# da direita para a esquerda. Exemplo: abba é um palíndromo, enquanto abab não é. .
# Assinatura da função: def palindromo(s)
# OBS: Para este problema considere que a string já foi tratada e só contém letras minúsculas, sem acentos, sem
# pontuação e sem espaços.

def palindromo(s):
    if (len(s) <= 1):
        return True
    if (s[0] != s[-1]):
        return False
    return palindromo(s[1:-1])