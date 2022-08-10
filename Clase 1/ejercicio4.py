import math

valores = {}

i = 1

while i <= 4:
    funcion = math.sin(i) + math.log(i)
    valores[i] = funcion
    i = round(float(i+0.1),1)

for e in valores.items():
    print(e)

mayor = max(valores, key = valores.get)
print("El mayor valor esta en el numero : " + str(mayor) + ", y es de : ")
print(valores[mayor])



