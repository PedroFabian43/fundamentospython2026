import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")
cursor = connection.cursor()

sql = "SELECT DEPT_NO FROM DEPT"
cursor.execute(sql)

print("----Menú departamento----")
for row in cursor:
    print(row[0])

print("Seleccione un departamento:")
iddept = int(input())
sql = "SELECT APELLIDO, OFICIO FROM EMP WHERE DEPT_NO = :id"
cursor.execute(sql, (iddept,))
print("----Empleados departamento----")
for apellido, oficio in cursor:
    print(f"Nombre: {apellido}, Oficio: {oficio} ")
cursor.close()
connection.close()
print("Fin de programa")


