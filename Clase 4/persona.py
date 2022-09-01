from funciones import capturar_dato,capturar_tipo_documento,capturar_correo,capturar_fecha,conexion_bd

class Persona():

    def __init__(self):
        self.nombres = None
        self.apellidos = None
        self.tipo_documento = None
        self.numero_documento = None
        self.fecha_nacimiento = None
        self.correo = None
    
    def agregar(self):
        self.nombres = capturar_dato("Nombres: ")
        self.apellidos = capturar_dato("Apellidos: ")
        self.tipo_documento = capturar_tipo_documento("Tipo de documento ti(tarjeta d eidentidad),cc(cedula de ciudadania), ce(cedula de extranjeria): ")
        self.numero_documento = capturar_dato("Número de documento : ")
        self.fecha_nacimiento = capturar_fecha("Fecha de nacimiento (dd/mm/aaaa): ")
        self.correo = capturar_correo("Correo electrónico: ")        

    def mostrar(self):
        print("\n --------------Informacion--------------")
        print(f"{self.nombres} {self.apellidos}")
        print(self.tipo_documento)
        print(self.numero_documento)
        print(self.fecha_nacimiento)
        print(self.correo)

if __name__ == "__main__":
    p = Persona()
    p.agregar()
    p.mostrar()



