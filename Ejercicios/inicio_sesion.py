import mysql.connector

conexion = mysql.connector.connect(user = "redsocial_admin", password="admin_12",
                                   host="localhost", database = "redsocial",
                                   port = 3306)

cursor = conexion.cursor()

# consultar datos
consulta = ("SELECT * FROM Usuarios WHERE email = %s AND contrasena = %s")

email = input("Ingrese su email: ")
clave = input("Ingrese su clave: ")

datos = [email, clave]

cursor.execute(consulta, datos)

contador = 0
for fila in cursor:
    contador += 1
    print(fila)

if contador > 0:
    print("Bienvenido!")
else:
    print("Datos incorrectos")

cursor.close()
conexion.close()
