import oracledb

print("conectando a Oracle")
#tenemos un objeto connection que nos pedirá
#(user, password, server)

connection = oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")

print("estamos conectados!!!")

#las consultas select se ejecutan a partir de connection y se crea un objeto llamado cursor

#cursor = connection.cursor()

#una vez tenemos el cursor se quejecuta el sql.

#cursor.execute(SQL)

#una vez tenemos todo, ya tendremos los datos

#creamos nuestra consulta SQL
#La consulta SQL desde python no finaliza en ";"
sql = "select * from DEPT"

#creamos un cursor para la consulta
cursor = connection.cursor()

#debemos ejecutar la consulta para que nos devuelva los datos de oracle
cursor.execute(sql)

#aquí ya están los datos
#una vez que tenemos el cursor,debemos leer los datos
#tenemos un método llamado FETCHONE() que s emueve una fila cada vez que lo ejecutamos
#nos devuelve dicha fila en la que estamos posicionados

row = cursor.fetchone()#Primera fila
print(row)
row = cursor.fetchone()#segunda fila
print(row)
row = cursor.fetchone()#Tercera fila
print(row)
row = cursor.fetchone()#Cuarta fila
print(row)
#Hasta aquí está la consulta completa de la tabla
#que sucede si leemos una fila cuando no tenemos más?
row = cursor.fetchone()#Quinta Fila
print(row)
#Da none oNull si fuera oracle

#siempre que finalicemos las acciones, debemos liberar los recursos
cursor.close()
connection.close()
print("Fin de programa")