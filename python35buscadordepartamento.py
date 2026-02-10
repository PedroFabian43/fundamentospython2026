#vamos a realizar un buscador de ID de departamento.
#pediremos al usuario que nos diga un Id y le devolveremos los datos si ese dept existe
import oracledb

#creamos la conexion a oracle
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

print("Conectado")

#pedimos el departamento al usuario
print("Introduzca un ID de departamento")
iddepartamento = input()

#necesitamos una consulta para buscar el departamento
sql = "select * from DEPT where DEPT_NO = " + iddepartamento
#aquí pedimos que lo muestre para que lo veamos bien
print(sql)

#Creamos un cursor
cursor = connection.cursor()

#ejecutamos la consulta para traer los datos

cursor.execute(sql)
#recuperamos la primera fila
row = cursor.fetchone()

#comprobamos si tenemos datos o no en la fila
if (row == None):
    print("No hay ningún departamento asignado a ese ID")
else:
    #recuperamos los datos
    nombre = row[1] # DNOMBRE
    localidad = row[2] # LOC
    print(nombre + ", " + localidad)
#liberamos recursos
cursor.close()
connection.close()
print("Fin de programa")

