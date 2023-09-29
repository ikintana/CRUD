import json
import datetime
import time

nombre_fichero = "datos.json"
lista = []

def aniadir_nuevo(fecha, hora, destino, plazas):
    #crear diccionario y añadir con append a lista
    #input con fecha, hora, destino, plaza
    #llamar a fecha completa con hora y fecha
    id_vuelo = crear_id()
    diccionario = {"id_vuelo": id_vuelo, "fecha_completa":fecha_completa(fecha, hora), "destino": destino, "plazas": plazas}
    lista.append(diccionario)

def aniadir_nuevo_carga(id_vuelo, fecha_completa, destino, plazas):
    #crear diccionario y añadir con append a lista
    #input con fecha, hora, destino, plaza
    #llamar a fecha completa con hora y fecha
    diccionario = {"id_vuelo": id_vuelo, "fecha_completa":fecha_completa, "destino": destino, "plazas": plazas}
    lista.append(diccionario)
    guardar()

def cargar():
    try:
        # Intentar abrir el archivo JSON en modo lectura
        with open(nombre_fichero, "r") as archivo:
            lista_descarga = json.load(archivo)
            for diccionario in lista_descarga:
                aniadir_nuevo_carga(diccionario["id_vuelo"], diccionario["fecha_completa"], diccionario["destino"], diccionario["plazas"])
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
    return int(time.time())

def fecha_completa(fecha, hora):
    return fecha + " " + hora

def comprobar_fecha(fecha):
    try:
        # Intenta convertir la cadena de fecha en un objeto datetime
        datetime.datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        # Si ocurre un error, la fecha no es válida
        return False

def comprobar_hora(hora):
    try:
        time.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
    