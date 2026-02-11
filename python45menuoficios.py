import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

cursor = connection.cursor()
listaOficios = []
contador = 1

#agregamos oficios mediante una consulta SQL
sql = "SELECT DISTINCT OFICIO FROM EMP"
cursor.execute(sql)

for row in cursor:
    #agregamos cada oficio
    listaOficios.append(row[0])

#creamos un contador
contador = 1

for ofi in listaOficios:
    print(f"{contador}) {ofi}")
    contador = contador + 1

contador = 1
print("Seleccione una opción:")
opcion = int(input())
oficioSeleccionado = listaOficios[opcion - 1]
print(f"Opción seleccionada: {oficioSeleccionado}")

#Consultamos los empleados con el oficio seleccionado
sql = "SELECT * FROM EMP WHERE OFICIO = :oficio"
cursor.execute(sql, (oficioSeleccionado,))
print("----Lista empleados----")
for row in cursor:
    print(f"{contador}) Apellido: {row[1]}, Salario: {row[5]}")
    contador = contador + 1

cursor.close()
connection.close()
print("Fin")