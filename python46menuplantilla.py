import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")
cursor = connection.cursor()

listaFuncion = []
contador = 1

sql = "SELECT DISTINCT FUNCION FROM PLANTILLA ORDER BY FUNCION"
cursor.execute(sql)

for puesto in cursor:
    listaFuncion.append(puesto[0])

print("----Lista de funciones----")
for funcion in listaFuncion:
    print(f"{contador}) {funcion}")
    contador = contador + 1

contador = 1
print("")
print("Seleccione que funcion desea revisar:")
opcion = int(input())

funcionSeleccionada = listaFuncion[opcion - 1]
print(f"Función seleccionada: {funcionSeleccionada}")

sql = "SELECT APELLIDO, FUNCION FROM PLANTILLA WHERE FUNCION = :funcion"
cursor.execute(sql, (funcionSeleccionada,))

print("----Lista de empleados----")
for apellido, trabajo in cursor:
    print(f"{contador}) Nombre: {apellido}, Función: {trabajo}")
    contador = contador + 1

cursor.close()
connection.close()
print("Fin de programa")
