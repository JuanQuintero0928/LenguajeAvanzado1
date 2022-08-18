import math

class Geometria():

    #Metodo Constructor:
    def __init__(self):
        self.dato = None
        self.area = None
        self.altura = None
        self.radio = None

    def mostrar_menu(self):
        self.dato = int(input("""------------ MENU ------------
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
            
    def cubo(self):
        self.area = int(input("Digite el area de un lado del cubo : "))
        AreaCubo = 6 * (self.area**2)
        VolumenCubo = self.area**3
        print("El Area total del Cubo es de : " + str(AreaCubo))
        print("El Volumen total del Cubo es de : " + str(VolumenCubo))

    def cilindro(self):
        self.altura = int(input("Digite la altura del cilindro : "))
        self.radio = int(input("Digite el radio del cilindro : "))
        AreaCilindro = 2 * math.pi * self.radio * (self.altura + self.radio)
        VolumenCilindro = math.pi * (self.radio**2) * self.altura 
        print("El Area total del Cilindro es de : " + str(AreaCilindro))
        print("El Volumen total del Cilindro es de : " + str(VolumenCilindro))

    def esfera(self):
        pass

    def cono(self):
        pass

if __name__ == "__main__":
    u = Geometria()
    u.mostrar_menu()
    