from calendar import prcal
from persona import Persona
from funciones import capturar_dato

class Estudiante(Persona):

    def __init__(self):
        super().__init__()
        self.materia = None
        self.carrera = None
        self.nota = 0.0

    def agregar_estudiante(self):
        super().agregar()
        self.carrera = capturar_dato("Carrera : ")
        self.materia = capturar_dato("Materia : ")
    
    def mostrar_info(self):
        super().mostrar()
        print(self.materia)
        print(self.carrera)

if __name__ == "__main__":
    e = Estudiante()
    e.agregar_estudiante()
    e.mostrar_info()