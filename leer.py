import listado as l

def mostrar_vuelos():
    for diccionario in l.lista:
        print(f"Fecha de Salida: {diccionario['fecha_completa']}, ID Vuelo: {diccionario['id_vuelo']}, Destino: {diccionario['destino']}, Plazas Libres: {diccionario['plazas']}")