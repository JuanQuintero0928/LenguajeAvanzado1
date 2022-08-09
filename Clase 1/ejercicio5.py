opcion = int(input("""Menú
    1. Suma de términos
    2. Cantidad de términos
    3. Primer término
    4. Último término
    5. Salir
    --------------
    """))

if opcion <= 0 or opcion > 5:
    print("Opcion invalida")
else:
    if opcion == 1:
        terminos = int(input("Digite cantidad de terminos : "))
        primert = int(input("Digite el primer termino : "))
        ultimot = int(input("Digite el ultimo termino : "))

        suma = ((primert+ultimot) * terminos ) / 2

        print("El resultado de la sucesion aritmetica es : " + str(suma))
    if opcion == 2:
        suma = int(input("Digite la suma de terminos : "))
        primert = int(input("Digite el primer termino : "))
        ultimot = int(input("Digite el ultimo termino : "))

        terminos = (suma / (primert+ultimot))*2

        print("La cantidad de terminos es de : " + str(terminos))
        
    if opcion == 3:
        suma = int(input("Digite la suma de terminos : "))
        terminos = int(input("Digite cantidad de terminos : "))
        ultimot = int(input("Digite el ultimo termino : "))

        primert = ((suma * 2) - (ultimot*terminos)) / terminos
        
        print("El Primer digito es : " +str(primert))

    if opcion == 4:
        suma = int(input("Digite la suma de terminos : "))
        terminos = int(input("Digite cantidad de terminos : "))
        primert = int(input("Digite el primer termino : "))

        ultimot = ((suma * 2) - (primert * terminos)) / terminos
        
        print("El ultimo digito es : " +str(ultimot))

    if opcion == 5:
        exit