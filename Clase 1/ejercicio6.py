import math


a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))

oper1 = (b**2) - (4 * (a * c))
raiz1 = math.sqrt(oper1)
solucion1 = ((b)+ raiz1) / (2 * a)

print(solucion1)