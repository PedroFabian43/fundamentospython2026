import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")
cursor = connection.cursor()

print("Dime el nombre del hospital")
hospital = input()
print("Dime la cantidad del aumento")
extra = int(input())

sql = "UPDATE PLANTILLA SET SALARIO = SALARIO + :aumento WHERE HOSPITAL_COD = (SELECT HOSPITAL_COD FROM HOSPITAL WHERE NOMBRE = :hospi)"
cursor.execute(sql, (extra, hospital,))
connection.commit()

#Contamos los cambios
afectados = cursor.rowcount
print("Empleados con aumento: " + str(afectados))

#Hacemos la muestra de datos

sql = """
SELECT PLANTILLA.APELLIDO, PLANTILLA.SALARIO, HOSPITAL.NOMBRE
FROM PLANTILLA
INNER JOIN HOSPITAL
ON PLANTILLA.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD
WHERE HOSPITAL.NOMBRE = :hospital
"""
cursor.execute(sql, (hospital,))

for apellido, salario, nom_hospital in cursor:
    print("Nombre: " + apellido, "Salario: " + str(salario), "Hospital: " + hospital)

cursor.close()
connection.close()
print("Fin de programa")

