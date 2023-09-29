import listado as l

def modificar_vuelos():
    id_vuelo = int(input("\nIntroduce el ID del vuelo: "))

    encontrado = False
    for diccionario in l.lista:
        if diccionario["id_vuelo"] == id_vuelo:
            fecha = str(input("\nIntroduce la fecha (dd/mm/aaaa): "))
            bucle_fecha = True
            while bucle_fecha:
                if l.comprobar_fecha(fecha) == False: 
                    print("\nERROR: Fecha incorrecta. Introduce los datos de nuevo.\n")
                    fecha = str(input("\nIntroduce la fecha : "))
                else:
                    bucle_fecha = False
            hora = str(input("\nIntroduce la hora (hh:mm): "))
            bucle_hora = True
            while bucle_hora:
                if l.comprobar_hora(hora) == False: 
                    print("\nERROR: Hora incorrecta. Introduce los datos de nuevo.\n")
                    hora = str(input("\nIntroduce la hora: "))
                else:
                    bucle_hora = False
            diccionario["destino"] = input("Introduce el nuevo destino: ")
            diccionario["plazas"] = input("Introduce el nuevo plazas: ")
            eliminar.eliminar_vuelos_reconocido(id_vuelo)
            l.aniadir_nuevo_carga(diccionario["id_vuelo"], l.fecha_completa(fecha, hora), diccionario["destino"], diccionario["plazas"])
            
            encontrado = True
            break
    if(encontrado == True):
        print("Se ha modificado correctamente.")
    else:
        print("El vuelo introducido no se ha encontrado.")
    return None  # Devuelve None si no se encuentra ninguna coincidencia

