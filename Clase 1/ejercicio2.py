dolar = int(input("Digite el numero de Dolares : "))

b100 = dolar // 100
rb100 = dolar % 100
b50 = rb100 // 50
rb50 = rb100 % 50
b20 = rb50 // 20
rb20 = rb50 % 20
b10 = rb20 // 10
rb10 = rb20 % 10
b5 = rb10 // 5
rb5 = rb10 % 5

if b100 > 0:
    print(f"Billetes de 100 : {b100}")
if b50 > 0:
    print(f"Billetes de 50 : {b50}")
if b20 > 0:
    print(f"Billetes de 20 : {b20}")
if b10 > 0:
    print(f"Billetes de 10 : {b10}")
if b5 > 0:
    print(f"Billetes de 5 : {b5}")
if rb5 > 0:
    print(f"Billetes de 1 : {rb5}")
