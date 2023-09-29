import json
import datetime
import time

nombre_fichero = "datos.json"
lista = []

def aniadir_nuevo():
    #crear diccionario y añadir con append a lista
    #input con fecha, hora, destino, plaza
    #llamar a fecha completa con hora y fecha
    id_vuelo = int(time.time())
    destino = str(input("Introduce destino: "))
    plazas = str(input("Introduce plazas: "))
    fecha_test = comprobar_fecha(str(input("Introducir fecha: ")))
    hora_test = comprobar_hora(str("Introducir hora: "))
    if fecha_test == True and hora_test == True:
        fecha_completa(fecha_test, hora_test)
    else:
        pass
    pass
    diccionario = {"id_vuelo": id_vuelo, "fecha_completa":fecha_completa, "destino": destino, "plazas": plazas}
    lista.append(diccionario)

def cargar():
    try:
        # Intentar abrir el archivo JSON en modo lectura
        with open(nombre_fichero, "r") as archivo:
            lista_descarga = json.load(archivo)
            for diccionario in lista_descarga:
                aniadir_nuevo(diccionario["fecha_completa"], diccionario["destino"], diccionario["plazas"])
    except:
        # Crear un archivo JSON vacío si no existe
        with open(nombre_fichero, "w") as archivo:
            json.dump({},archivo)  # Crear fichero
        return []  # Devolver una lista vacía como contenido

def guardar():
    try:
        with open(nombre_fichero, "w") as f: 
            json.dump(lista, f)
    except:
            print("No ha sido posible guardar el JSON.")

def crear_id():
    pass

def fecha_completa(fecha_test, hora_test):
    pass

def comprobar_fecha(fecha):
    return True

def comprobar_hora(hora):
    return True