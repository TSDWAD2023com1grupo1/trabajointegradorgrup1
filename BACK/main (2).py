from Conexion import connect
from Persona import Administrador
import mysql.connector

if __name__ == '__main__':
    try:
        conn, cursor = connect() 
        print('Conexión Exitosa')
    except mysql.connector.Error as error:
        print('Conexión Fallida')
        print(error)

    mi_admi = Administrador(1, "admiss", "perrito", "2023-10-11", "admi", "mendoza")

def menu():
    print("-" * 60)
    print("BIENVENIDO AL SISTEMA")
    print("-" * 60)
    print("OPCION 1 - Cargar productos")
    print("OPCION 2 - Eliminar prodcutos")
    print("OPCION 3 - Actualizar productos")
    print("OPCION 4 - Mostrar productos")
    print("OPCION 5 - Salir del sistema")
    print("-" * 60)

while True:
    menu()
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        mi_admi.cargarProd() 

    elif opcion ==  2:
        mi_admi.eliminarProd()
        
    elif opcion == 3:
        mi_admi.modificarProd()
        
    elif opcion == 4:
        mi_admi.verProd()
        
    elif opcion == 5:
        print("-" * 60)
        print("Hasta luego! :)")
        print("-" * 60)
        break
    
    else:
        print("Opcion invalida, vuelva a elegir una opcion")


