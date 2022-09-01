from datetime import datetime
import re # expresiones regulares
import psycopg2 # intalar la libreria

def capturar_dato(mensaje=None):
    while True:
        try:
            dato = input(mensaje)
            if dato != "":
                return(dato)
            else:
                print("\tERROR --> Debe ingresar un valor")
        except ValueError:
            print("ERROR --> se generó un error al capturar el dato")

def capturar_tipo_documento(mensaje=None):
    tipos = ["ti","cc","ce"]
    while True:
        try:
            dato = input(mensaje)
            if dato in tipos:
                return(dato)
            else:
                print("\tERROR --> Debe ingresar un valor correcto(ti,cc,ce)")
        except ValueError:
            print("ERROR --> se generó un error al capturar el dato")

def capturar_correo(mensaje=None):
    regex1 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{3}.\w{2}$'
    regex2 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        try:
            dato = input(mensaje)
            if re.search(regex1,dato) or re.search(regex2,dato):
                return(dato)
            else:
                #i = re.search(regex,dato)
                #print(i)
                print("\tERROR --> Debe ingresar un correo electrónico valido")
        except ValueError:
            print("ERROR --> se generó un error al capturar el dato")
    pass

def capturar_fecha(mensaje=None):
    while True:
        try:
            dato = datetime.strptime(input(mensaje),'%d/%m/%Y').date()
            return(dato)
        except ValueError as e:
            print("\tERROR --> se generó un error al capturar el dato")
            #print("\t"+e)

def conexion_bd(consulta):
    conexion = psycopg2.connect(host='localhost',database='remington',user='user_remington',password='1q2w3e4r')
    cursor = conexion.cursor()
    cursor.execute(consulta)
    if consulta.upper().startswith('SELECT'): 
        datos = cursor.fetchall()
    else:
        conexion.commit()               
        datos = None 			
    return datos