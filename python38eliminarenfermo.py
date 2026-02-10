import oracledb

connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

print("Eliminación de enfermos")
#Creamos el cursor que vamos a usar
cursor = connection.cursor()

#mostramos los enfermos (apellido, inscripcion)
sql = "SELECT INSCRIPCION, APELLIDO FROM ENFERMO"
cursor.execute(sql)
contador = 0
for row in cursor:
    contador = contador + 1
    print(str(contador) + ")", str(row[0]) + ", " + row[1])
#cursor.close() en otros lensuajes es neceasario cerra cada vez, aquí no

print("Dime la inscripción del enfermo que deseas eliminar:")
dato = input()

sql = "DELETE FROM ENFERMO WHERE INSCRIPCION = " + dato
cursor.execute(sql)

#como es una consulta de accion, simplemente dibujamos los registros eliminados
afectados = cursor.rowcount
print("Registros eliminados: " + str(afectados))
connection.rollback() #Para no dejar los cambios permanentes
# connection.commit() si lo queremos permanente
cursor.close()
connection.close()
print("fin de programa")