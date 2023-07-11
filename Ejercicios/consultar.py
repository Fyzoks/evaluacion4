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

# asegurarnos de cerrar
cursor.close()
conexion.close()
