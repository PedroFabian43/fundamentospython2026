import oracledb

connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

print("Dime el turno que estás buscando (M,T,N)")
turno = input()

sql = "SELECT APELLIDO, FUNCION FROM PLANTILLA WHERE TURNO = "+ "'" + turno + "'" 
print(sql)

cursor = connection.cursor()
cursor.execute(sql)

for row in cursor:
    apellido = row[0]
    funcion2 = row[1]
    print(apellido + ", " + funcion2)

# for nombre, funcion in cursor:
#     print("Nombre:", nombre, "//", "Función:", funcion)

cursor.close()
connection.close()

print("fin de programa")
