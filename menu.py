import leer
import aniadir
import modificar
import eliminar

def ejecutar():

    variable = True
    while variable:
            print("\n- - - - - - - - - - - - - - - - - - - -")
            mostrar_menu()
            opcion = str(input("\nElija una opción: "))
           
            match opcion: 
                case "1":
                    leer.mostrar_vuelos(archivo_json)      
                case "2":
                    aniadir.aniadir_vuelo(archivo_json)
                case "3":
                    modificar.modificar_vuelos(archivo_json)
                case "4":
                    eliminar.eliminar_vuelos(archivo_json)
                case "0":
                    variable = False
                case other:
                    print("\nOpción no válida. Intente de nuevo.")

def mostrar_menu():
    print("n\1. Información de los Vuelos")
    print("2. Añadir un Vuelo")
    print("3. Modificar un Vuelo Existente")
    print("4. Borrar un Vuelo")
    print("0. Salir")

if __name__ == "__main__":
    archivo_json = "vuelos.json"
    ejecutar()
    
