import mysql.connector

print("Abriendo conexion...")
conexion = mysql.connector.connect(user="poo_c2user", password="1234",
                                   host="127.0.0.1", database="poo_c2",
                                   port=3306)
print("Conexion abierta.")

cursor = conexion.cursor()

print("ESTADO DE LA CONEXION: ", conexion.is_connected())

agregar_encargado = ("INSERT INTO encargado "
                       "(nombre, apellido, RUT) "
                       "VALUES (%s, %s)")

nom = input("Ingrese el nombre del Encargado")
ape = input("Ingresar el apellido del encargado")
rut = input("ingrese el rut del encargado")

datos_encar = (nom, ape, rut)

print("Insertando datos")
cursor.execute(agregar_encargado, datos_encar)

conexion.commit()
print("Datos guardados")

print("Cerrando conexion...")
cursor.close()
conexion.close()
print("Conexion cerrada")






