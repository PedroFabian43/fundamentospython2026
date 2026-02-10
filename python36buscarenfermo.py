import oracledb

#Consulta: "SELECT * FROM ENFERMO WHERE INSCRIPCION =" +

#CREAMOS CONNECTION
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

print("Buscador de pacientes")

#creamos la pregunta que le pedirá al usuario
print("Introduzca el número de inscripción del paciente:")
inscripcion = input()

#hacemos la consulta
sql = "SELECT * FROM ENFERMO WHERE INSCRIPCION = " + inscripcion

#creamos el cursor
cursor = connection.cursor()

#ejecutamos la consulta
cursor.execute(sql)

#recuperamos la fila
row = cursor.fetchone()

print("-----------------------------------")
#comprobamos si es válido
if (row == None):
    print("Usuario no encontrado")
else:
    #Recuperamos los datos
    numero = row[0] #INSCRIPCION
    nombre = row[1] #APELLIDO
    direccion = row[2] #DIRECCION
    fecha = row[3] #FECHA_NAC
    genero = row[4] #SEXO
    nnss = row[5] #NSS
    print("N. Inscripción:", numero)
    print("Sr/Sra:", nombre)
    print("Dirección:", direccion)
    print("Fecha de nacimiento:", fecha)
    print("Género:", genero)
    print("NNSS:", nnss)

print("-----------------------------------")
#cuando acabamos la consulta cerramos el cursor para liberar memoria
cursor.close()
#Cerramos la conexion cuando acabamos finalmente del todo
connection.close()
print("Fin de programa")

#Numeros validos: 10995, 18004, 14024