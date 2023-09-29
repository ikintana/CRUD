import listado as l

def eliminar_vuelos():
    id_vuelo = int(input("Introduce el ID del Vuelo: "))

    contador = 0

    encontrado = False
    for vuelos in l.listado:
        if vuelos["id_vuelo"] == id_vuelo:
            del l.listado[contador] 
            print ("Vuelo eliminado correctamente")
        else:
            print("Vuelo no encontrado.")
        contador += 1

