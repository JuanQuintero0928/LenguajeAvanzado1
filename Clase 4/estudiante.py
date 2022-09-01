from calendar import prcal
from persona import Persona
from funciones import capturar_dato, conexion_bd

class Estudiante(Persona):

    def __init__(self):
        super().__init__()
        self.carrera = None
        self.nota = 0.0

    def agregar_estudiante(self):
        super().agregar()
        self.carrera = capturar_dato("Carrera : ")
        sql = f"insert into estudiante (nombres, apellidos, tipo_documento, numero_documento, fecha_nacimiento, correo, carrera) values ('{self.nombres}','{self.apellidos}','{self.tipo_documento}', '{self.numero_documento}','{self.fecha_nacimiento}','{self.correo}','{self.carrera}')"
        conexion_bd(sql)
    
    def mostrar_info(self):
        super().mostrar()
        print(self.carrera)
        

if __name__ == "__main__":
    e = Estudiante()
    e.agregar_estudiante()
    e.mostrar_info()