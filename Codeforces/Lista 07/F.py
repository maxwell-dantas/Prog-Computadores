def primo(num):
    if (num <= 1):
        return "Nao"
        
    primo = "Sim"
    
    for i in range(2, num):
        if (num % i == 0):
            primo = "Nao"
            break
    return primo
    
n = int(input())
print(primo(n))