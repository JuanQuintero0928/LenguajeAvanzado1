import math

valores = {}

i = 1

while i <= 4:
    funcion = math.sin(i) + math.log(i)
    valores[i] = funcion
    i = round(float(i+0.1),1)

mayor = max(valores, key = valores.get)
print("El mayor valor esta en el numero : " + str(mayor) + ", y es de : ")
print(valores[mayor])

imprimir = input("¿Desea imprimir todos los resultados? y/n : ")
if imprimir == "y":
    for e in valores.items():
        print(e)