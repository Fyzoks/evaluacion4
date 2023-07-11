import mysql.connector

print("Abriendo conexion...")
conexion = mysql.connector.connect(user="poo_c2user", password="1234",
                                   host="127.0.0.1", database="poo_c2",
                                   port=4406)
print("Conexion abierta.")

cursor = conexion.cursor()

print("ESTADO DE LA CONEXION: ", conexion.is_connected())

agregar_dispositivo = ("INSERT INTO Dispositivos "
                       "(nombre, ubicacion) "
                       "VALUES (%s, %s)")

nom = input("Ingrese el nombre del dispositivo")
ubi = input("Ingresar la ubicacion del dispositivo")

datos_disp = (nom, ubi)

print("Insertando datos")
cursor.execute(agregar_dispositivo, datos_disp)

idDisp = cursor.lastrowid
tipo = input("Ingrese el tipo de la medicion: ")
fecha = input("Ingrese la fecha de la medicion: ")
valor = input("Ingrese el valor de la medicion")
valor = int(valor)

cmd_insert_med = ("INSERT INTO Mediciones "
                  "(tipo, fecha, valor, idDisp) "
                  "VALUES (%s, %s, %s, %s)")

valores = (tipo, fecha, valor, idDisp)

cursor.execute(cmd_insert_med, valores)

conexion.commit()
print("Datos guardados")

print("Cerrando conexion...")
cursor.close()
conexion.close()
print("Conexion cerrada")






