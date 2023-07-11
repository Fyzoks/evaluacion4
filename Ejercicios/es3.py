import mysql.connector

conexion = mysql.connector.connect(user="pato", password="1234",
                                   host="localhost",
                                   database="evaluacion4", port=3306)


def elegirOpcion():
    print("MENU -------------------")
    print("\t1.- agregar encargado")
    print("\t2.- consultar lista de encargados")
    print("\t3.- modificar encargado")
    print("\t4.- eliminar encargado")
    print("\t5.- salir del menu")
    opcion = input("Ingrese su eleccion: ")
    opcion = int(opcion)
    return opcion

def agregar():
    print("Agregando encargado: ")
    cursor = conexion.cursor()
    agregar = ("INSERT INTO encargado "
               "(nombre, apellido, rut) "
               "VALUES (%s, %s,%s)")

    nom = input("Ingrese el nombre: ")
    ape = input("Ingrese el apellido: ")
    rut = input("ingrese el rut: ")

    datos = (nom, ape, rut)
    cursor.execute(agregar, datos)
    conexion.commit()
    print("Datos guardados")
    cursor.close()

def consultar():
    cursor = conexion.cursor()
    consulta = ("SELECT * FROM encargado")

    cursor.execute(consulta)
    for (id_encargado, nombre, apellido, rut) in cursor:
        print(id_encargado, "-", nombre, "-", apellido,"-",rut)

    cursor.close()

def modificar():
    consultar()

    cursor = conexion.cursor()
    
    id_encargado = input("Que encargado desea modificar? ")
    actualizar = ("UPDATE encargado "
                  "SET nombre = %s, apellido = %s,rut = %s"
                  "WHERE id_encargado = %s")

    nom = input("Nuevo nombre: ")
    ape = input("Nuevo apellido: ")
    rut = input("nuevo rut: ")

    datos = (nom, ape,rut, id_encargado)
    cursor.execute(actualizar, datos)
    conexion.commit()
    cursor.close()

def eliminar():
    consultar()

    cursor = conexion.cursor()

    consulta = ("SELECT * FROM encargado")

    cursor.execute(consulta)

    id_encargado = input("Que encargado desea eliminar? ")

    for (id_encargado, nombre, apellido, rut) in cursor:
        print(id_encargado, "-", nombre, "-", apellido,"-",rut)

    eliminar = ("DELETE FROM encargado "
                 "WHERE id_encargado = %s")
    
    valores = [id_encargado]

    cursor.execute(eliminar, valores)
    conexion.commit()
    print("Datos eliminados")
    
    
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
        eliminar()
        
    
    eleccion = elegirOpcion()

# desconectar la BD
print("Hasta pronto 👋🏻")
conexion.close()
