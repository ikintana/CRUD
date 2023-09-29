import listado as l

def aniadir_vuelos():

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
    
    destino = str(input("\nIntroduce el destino: "))
    bucle_destino = True
    while bucle_destino:
        if not destino.isalpha():
            print("\nERROR: Destino incorrecto. Introduce los datos de nuevo.\n")
        else:
            bucle_destino = True

    plazas = int(input("\nIntroduce las plazas: "))
    bucle_plazas= True
    while bucle_plazas:
        try:
            plazas = int(input("\nIntroduce las plazas: "))
            bucle_plazas = False
        except:
            print("\nERROR: Plazas incorrectas. Introduce un numero.\n")
    
    l.aniadir_nuevo(fecha, hora, destino, plazas)