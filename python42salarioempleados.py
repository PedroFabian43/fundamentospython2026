import oracledb
connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")
cursor = connection.cursor()

print("Introduce un oficio al que quieras subir el salario:")
oficio = input()
print("Introduce la cantidad de dinero del aumento:")
aumento = int(input())

sql = "UPDATE EMP SET SALARIO = SALARIO + :extra WHERE OFICIO = :funcion"

cursor.execute(sql, (aumento, oficio,))
connection.commit()
print("---------------------------------------------------------------------")
#Pasamos a mostrar los que han sido afectados
suertudos = cursor.rowcount
print("Salarios aumentados:", suertudos)

print("---------------------------------------------------------------------")

sql = "SELECT APELLIDO, OFICIO, SALARIO FROM EMP WHERE OFICIO = :funcion"
cursor.execute(sql, (oficio,))

for persona, trabajo, salario in cursor:
    print(f"Apellido: {persona}, Oficio: {trabajo}, Salario: {salario}")

cursor.close()
connection.close()
print("Fin de programa")
