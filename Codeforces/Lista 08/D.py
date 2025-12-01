def primo(n):
    num = n + 1
    div = 2

    while num % div != 0:
        div += 1
    
    if num == div:
        return num
    else:
        return primo(n + 1)
    
num = int(input())

print(primo(num))
