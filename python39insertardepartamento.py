import oracledb

connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

#creamos el cursor
cursor = connection.cursor()

print("ID departamento")
id = input()
print("Nombre departamento")
nombre = input()
print("Localidad")
localidad = input()

#en python tenemos una forma de concatenar utilizando solamente un string sin usar +
#para ello se usa la letra f fuera del string
#y cada variable irá entre llaves dentro del string
sql = f"INSERT INTO DEPT VALUES ({id}, '{nombre}', '{localidad}')"

#ejecutamos la accion de insertar
cursor.execute(sql)
connection.commit()

print("--------------------------------------------")
#realizamos la consulta de seleccion
sql = "SELECT * FROM DEPT"
cursor.execute(sql)

for row in cursor:
    numero = row[0]
    nombre = row[1]
    loc = row[2] 
    print(f"ID: {numero}, Nombre: {nombre}, Localidad: {loc}")

print("--------------------------------------------")
cursor.close()
connection.close()
print("Fin de programa")

