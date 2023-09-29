import leer
import aniadir
import modificar
import eliminar
import listado as l

def ejecutar():
    l.cargar()
    variable = True
    while variable:
            print("\n- - - - - - - - - - - - - - - - - - - -")
            mostrar_menu()
            opcion = str(input("\nElija una opción: "))
           
            match opcion: 
                case "1":
                    leer.mostrar_vuelos()      
                case "2":
                    aniadir.aniadir_vuelo()
                case "3":
                    modificar.modificar_vuelos()
                case "4":
                    eliminar.eliminar_vuelos()
                case "0":
                    variable = False
                case other:
                    print("\nOpción no válida. Intente de nuevo.")

def mostrar_menu():
    print("\n1. Información de los Vuelos")
    print("2. Añadir un Vuelo")
    print("3. Modificar un Vuelo Existente")
    print("4. Borrar un Vuelo")
    print("0. Salir")

if __name__ == "__main__":
    ejecutar()
    
