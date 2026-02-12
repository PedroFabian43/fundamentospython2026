import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")
cursor = connection.cursor()

sql = "SELECT MAX(DOCTOR_NO) + 1 AS MAXIMO FROM DOCTOR"
cursor.execute(sql)
row = cursor.fetchone()
idDoctor = row[0]

print("----Contratación doctor----")
print("Introduce su nombre:")
nombre = input()
print("Especialidad del doctor:")
especialidad = input()
print("Introduce su salario:")
salario = int(input())

#Necesitamos mostrar los hospitales porque nos interesa el código
print("----Lista de Hospitales----")
sql = "SELECT NOMBRE, HOSPITAL_COD FROM HOSPITAL"
cursor.execute(sql)

listaCodigos = []
contador = 1
for row in cursor:
    print(f"{contador}) {row[0]}")
    listaCodigos.append(row[1])
    contador = contador + 1

print("Seleccione el hospital al que desea enviarlo:")
opcion = int(input())


idHospital = listaCodigos[opcion - 1]
contador =1


sql = "INSERT INTO DOCTOR  VALUES (:hospital, :iddoctor, :nombre, :puesto, :salario)"
cursor.execute(sql, (idHospital, idDoctor, nombre, especialidad, salario,))
connection.commit()
print("Doctor insertado")
cursor.close()
connection.close()
print("Fin de programa") 
