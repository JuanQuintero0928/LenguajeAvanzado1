class Usuarios():

    #Metodo Constructor
    def __init__(self):
        #Atributos o caracteristicas
        self.nombres = None
        self.apellidos = None
        self.id = None
        self.correo = None
        self.usuario = None
        self.password = None

    def crear(self):
        self.nombres = input("Ingrese el nombre : ")
        self.apellidos = input("Ingrese el apellido : ")
        self.id = input("Ingrese su cedula : ")
        self.correo = input("Digite el correo : ")
        self.usuario = input("Digite el usuario : ")
        self.password = input("Ingrese su contraseña : ")
    
    def mostrar(self):
        print("Datos del usuario : \n")
        print(f"Nombre : {self.nombres}")
        print(f"Apellido : {self.apellidos}")
        print(f"Cedula : {self.id}")
        print(f"Correo : {self.correo}")
        print(f"Usuario : {self.usuario}")
        print(f"Contraseña : {self.password}")

if __name__ == "__main__":
    u = Usuarios()
    u.crear()
    u.mostrar()
