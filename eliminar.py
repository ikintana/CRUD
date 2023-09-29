import listado as l

def eliminar_vuelos():
    id_vuelo = int(input("Introduce el ID del Vuelo: "))

    contador = 0

    for vuelos in l.lista:
        if vuelos["id_vuelo"] == id_vuelo:
            del l.lista[contador] 
            l.guardar()
            print ("\nVuelo eliminado correctamente")
        else:
            print("\nVuelo no encontrado.")
        contador += 1

   
