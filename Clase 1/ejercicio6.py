import math


a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))

oper1 = (b**2) - (4 * (a * c))
raiz1 = math.sqrt(oper1)
solucion1 = ((-b)+ raiz1) / (2 * a)
solucion2 = ((-b)- raiz1) / (2 * a)

print("El resultado para x1 es de : " + str(round( solucion1,2)))
print("El resultado para x2 es de : " + str(round(solucion2,2)))