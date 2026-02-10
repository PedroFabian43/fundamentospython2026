import oracledb

connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

cursor = connection.cursor()

print("Introduce el nombre del hospital:")
hospi = input()
print("Introduce el código de hospital:")
id = input()
print("Introduce la dirección del hospital:")
direc = input()
print("Introduce el tlf del  hospital:")
tlf = input()
print("Introduce el número de camas que tiene el hospital:")
cama = input()

sql = f"INSERT INTO HOSPITAL VALUES ({id}, '{hospi}', '{direc}', '{tlf}', {cama})"
print(sql)

cursor.execute(sql)
connection.commit()

print("--------------------------------------------")

sql = "SELECT * FROM HOSPITAL"

cursor.execute(sql)

for row in cursor:
    id = row[0]
    nombre = row[1]
    direccion = row[2] 
    telefono = row[3]
    camas = row[4]
    print(f"Hospital_Id: {id}, Nombre: {nombre}, Dirección: {direccion}, Teléfono: {telefono}, Número_Camas: {camas}")


print("--------------------------------------------")
cursor.close()
connection.close()
print("Fin de programa")