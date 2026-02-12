import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")
cursor = connection.cursor()

sql = "SELECT MAX(EMPLEADO_NO) + 1 AS MAXIMO FROM PLANTILLA"
cursor.execute(sql)
row = cursor.fetchone()
idEmpleado = row[0]

print("----Contratación plantilla----")
print("Introduce el nombre:")
nombre = input()
print("Introduzca la función:")
funcion = input()
print("Seleccione el turno (M, T, N):")
turno = input()
print("Introduzca su salario:")
salario = int(input())
print("Introduzca la sala en la que trabajará:")
sala = int(input())

#Sacamos la lista de hospitales
print("----Lista de Hospitales----")
sql = "SELECT NOMBRE, HOSPITAL_COD FROM HOSPITAL"
cursor.execute(sql)
listaCodigos = []
contador = 1

for row in cursor:
    print(f"{contador}) {row[0]}")
    listaCodigos.append(row[1])
    contador = contador + 1

print("Seleccione el hospital donde trabajará:")
opcion = int(input())

idHospital = listaCodigos[opcion - 1]

sql = "INSERT INTO PLANTILLA VALUES (:hospital, :sala, :idemp, :apellido, :puesto, :turno, :dinero)"
cursor.execute(sql, (idHospital, sala, idEmpleado, nombre, funcion, turno, salario))
connection.commit()

print("Empleado añadido")
cursor.close()
connection.close()
print("Fin de programa")
