try:
    terminos = int(input("Digite un numero para hallar el valor de pi : "))
    if terminos > 0:
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
    else:
        print("El numero debe ser mayor a cero.")
except ValueError:
    print("Solo se recibe como dato de entrada valores numericos.")