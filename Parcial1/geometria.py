import math


class Geometria():

    # Metodo Constructor:
    def __init__(self):
        self.dato = None
        self.area = None
        self.altura = None
        self.radio = None
        self.generatriz = None

    def mostrar_menu(self):
        try:
            self.dato = int(input("""

            ------------ MENU ------------
                1. Hallar el Area y Volumen de un Cubo.
                2. Hallar el Area y Volumen de un Cilindro.
                3. Hallar el Area y Volumen de una Esfera.
                4. Hallar el Area y Volumen de un Cono.
                5. Salir

                Digite su opcion -> """))

            if self.dato == 1:
                u.cubo()
            if self.dato == 2:
                u.cilindro()
            if self.dato == 3:
                u.esfera()
            if self.dato == 4:
                u.cono()
            if self.dato == 5:
                print("Saliendo ... ")
                exit()
            if self.dato > 5 or self.dato < 1:
                print(
                    "la opcion ingresada no se encuentra en el menu, Digite de nuevo una opcion.")
                u.mostrar_menu()
        except ValueError:
            print("Solo se aceptan valores numericos. Digite de nuevo una opcion.")
            u.mostrar_menu()

    def mostrar_resultados(var1, area, volumen, objeto):
        print("""
            ------------ RESULTADOS ------------
            """)
        print("El Area del " + objeto + " es de : " + str(round(area,2)))
        print("El Volumen del " + objeto + " es de : " + str(round(volumen,2)))
        u.mostrar_menu()

    def cubo(self):
        print("""
            ------------ CUBO ------------
            """)
        try:
            self.area = float(input("Digite el area de un lado del cubo : "))
            if self.area > 0:
                Objeto = "Cubo"
                AreaCubo = 6 * (self.area**2)
                VolumenCubo = self.area**3
                u.mostrar_resultados(AreaCubo,VolumenCubo,Objeto)
            else:
                print("El numero debe ser mayor a 0.")
                u.cubo()
        except ValueError:
            print("Solo se aceptan valores numericos.")
            u.cubo()

    def cilindro(self):
        print("""
            ------------ CILINDRO ------------
            """)
        try:
            self.altura = float(input("Digite la altura del cilindro : "))
            self.radio = float(input("Digite el radio del cilindro : "))
            if self.altura > 0 and self.radio > 0:
                Objeto = "Cilindro"
                AreaCilindro = 2 * math.pi * self.radio * (self.altura + self.radio)
                VolumenCilindro = math.pi * (self.radio**2) * self.altura
                u.mostrar_resultados(AreaCilindro,VolumenCilindro,Objeto)
            else:
                print("Los numeros deben ser mayores a 0.")
                u.cilindro()
        except ValueError:
            print("Solo se aceptan valores numericos.")
            u.cilindro()

    def esfera(self):
        print("""
            ------------ ESFERA ------------
            """)
        try:
            self.radio = float(input("Digite el radio de la esfera : "))
            if self.radio > 0:
                Objeto = "Esfera"
                AreaEsfera = 4 * math.pi * self.radio**2
                VolumenEsfera = (4/3) * math.pi * self.radio**3
                u.mostrar_resultados(AreaEsfera,VolumenEsfera,Objeto)
            else:
                print("El numero debe ser mayor a 0.")
                u.esfera()
        except ValueError:
            print("Solo se aceptan valores numericos.")
            u.esfera()

    def cono(self):
        print("""
            ------------ CONO ------------
            """)
        try:
            self.radio = float(input("Digite el radio del Cono : "))
            self.generatriz = float(input("Digite la generatriz del Cono : "))
            self.altura = float(input("Digite la altura del Cono : "))
            if self.radio > 0 and self.generatriz > 0 and self.altura > 0:
                Objeto = "Cono"
                AreaCono = math.pi * self.radio**2 + math.pi * self.radio * self.generatriz
                VolumenCono = (math.pi * self.radio**2 * self.altura)/3
                u.mostrar_resultados(AreaCono,VolumenCono,Objeto)
            else:
                print("El numero debe ser mayor a 0.")
                u.cono()
        except ValueError:
            print("Solo se aceptan valores numericos.")
            u.cono()


if __name__ == "__main__":
    u = Geometria()
    u.mostrar_menu()
