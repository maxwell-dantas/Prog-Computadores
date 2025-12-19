def tautograma(lista):
    for i in range(1, len(lista)):
        palavra_1 = lista[i]
        palavra_2 = lista[i - 1]

        if palavra_1[0] != palavra_2[0]:
            return "N"
    return "Y"

while True:
    frase = input().lower()

    if frase == "*":
        break

    frase_palavra = frase.split()

    print(tautograma(frase_palavra))
