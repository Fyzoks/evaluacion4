import mysql.connector

conexion = mysql.connector.connect(user="poo_c2user", password="1234",
                                   host="localhost",
                                   database="poo_c2", port=4406)

cursor = conexion.cursor()

cmd_consulta = ("SELECT id_encargado, nombre, apellido, rut "
                "FROM encargado")

cursor.execute(cmd_consulta)

for (id_encargado, nombre, apellido, rut) in cursor:
    print(id_encargado, "-", nombre, "-", apellido, "-", rut)

idencargado = input("Que encargado desea modificar? ")

cmd_modificar = ("UPDATE encargado "
                 "SET nombre = %s, apellido = %s , rut = %s"
                 "WHERE id_encargado > %s")

nom = input("Ingrese el nuevo nombre: ")
ape = input("Ingrese el nuevo apellido: ")
rut = input("ingrese el nuevo rut: ")

valores = (nom, apellido, rut, id_encargado)

cursor.execute(cmd_modificar, valores)
conexion.commit()
print("Datos guardados")

# asegurarnos de cerrar
cursor.close()
conexion.close()












