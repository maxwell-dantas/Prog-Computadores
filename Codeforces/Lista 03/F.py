code, quant = map(int, input().split())

if code == 1:
    price = quant * 4.00
elif code == 2:
    price = quant * 4.50
elif code == 3:
    price = quant * 5.00
elif code == 4:
    price = quant * 2.00
elif code == 5:
    price = quant * 1.5
    
print("Total: R$ {:.2f}".format(price))