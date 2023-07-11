import mysql.connector

conexion = mysql.connector.connect(user="pato", password="1234",
                                   host="localhost",
                                   database="evaluacion4", port=3306)

cursor = conexion.cursor()

cmd_consulta = ("SELECT id_encargado, nombre, apellido, rut "
                "FROM encargado")

cursor.execute(cmd_consulta)

for (id_encargado, nombre, apellido, rut) in cursor:
    print(id_encargado, "-", nombre, "-", apellido, "-", rut)

id_encargado = input("Que Encargado desea eliminar? ")

cmd_eliminar = ("DELETE FROM encargado "
                 "WHERE id_encargado = %s")

valores = [id_encargado]

cursor.execute(cmd_eliminar, valores)
conexion.commit()
print("Datos eliminados")

# asegurarnos de cerrar
cursor.close()
conexion.close()












