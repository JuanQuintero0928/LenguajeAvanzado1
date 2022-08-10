terminos = int(input("Digite un numero para hallar el valor de pi : "))

denominador = 3
resultado = 1
    
for i in range (terminos):
    division = 1 / denominador
    denominador = denominador + 2
    if i % 2 == 0:
        resultado = resultado - division
    else:
        resultado = resultado + division

pi = resultado * 4
print("El resultado de pi es de : " + str(pi))
