import mysql.connector

conexion = mysql.connector.connect(user="poo_c2user", password="1234",
                                   host="localhost",
                                   database="poo_c2", port=4406)


def elegirOpcion():
    print("MENU -------------------")
    print("\t1.- Agregar dispositivo")
    print("\t2.- Mostrar todos")
    print("\t3.- Modificar un dispositivo")
    print("\t4.- Eliminar un dispositivo")
    print("\t5.- Salir")
    opcion = input("Ingrese su eleccion: ")
    opcion = int(opcion)
    return opcion

def agregar():
    print("Agregando dispositivo: ")
    cursor = conexion.cursor()
    agregar = ("INSERT INTO Dispositivos "
               "(nombre, ubicacion) "
               "VALUES (%s, %s)")

    nom = input("Ingrese el nombre: ")
    ubi = input("Ingrese la ubicacion: ")

    datos = (nom, ubi)
    cursor.execute(agregar, datos)
    conexion.commit()
    print("Datos guardados")
    cursor.close()

def consultar():
    cursor = conexion.cursor()
    consulta = ("SELECT * FROM Dispositivos")

    cursor.execute(consulta)
    for (idDisp, nombre, ubicacion) in cursor:
        print(idDisp, "-", nombre, "-", ubicacion)

    cursor.close()

def modificar():
    consultar()

    cursor = conexion.cursor()
    
    idDisp = input("Que dispositivo desea modificar? ")
    actualizar = ("UPDATE Dispositivos "
                  "SET nombre = %s, ubicacion = %s "
                  "WHERE idDisp = %s")

    nom = input("Nuevo nombre: ")
    ubi = input("Nueva ubicacion: ")

    datos = (nom, ubi, idDisp)
    cursor.execute(actualizar, datos)
    conexion.commit()
    cursor.close()
    

eleccion = elegirOpcion()
while eleccion != 5:
    if eleccion == 1:
        # agregar
        agregar()
    elif eleccion == 2:
        # consultar
        consultar()
    elif eleccion == 3:
        # modificar
        modificar()
    elif eleccion == 4:
        #eliminar
        pass
    
    eleccion = elegirOpcion()

# desconectar la BD
print("Hasta pronto 👋🏻")
conexion.close()
