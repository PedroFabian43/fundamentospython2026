import oracledb

connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

cursor = connection.cursor()
print("Introduzca número de departamento")
dato = int(input())
sql = "SELECT APELLIDO, OFICIO, DEPT_NO FROM EMP WHERE DEPT_NO = :deptno"
cursor.execute(sql, (dato,))

for apellido, oficio, dept in cursor:
    print(f"Apellido: {apellido}, Oficio: {oficio}, Departamento: {dept}")

cursor.close()
connection.close()

#si cuando nos pide el departamento y ponemos 0 or 1 = 1 hacemos que muestre todo
#lo que acabamos de realizar se llama SQL Injection que es una medida de acceso a las aplicaciones
#nuestras aplicaciones están expuestas si usamos las consultas SQL como los hemos hecho hasta ahora en python
#en lugar de concatenar textos o variables, se utilizan parámetros
#Los parámetros impiden SQL injection

#En lugar de incluir variables dentro de la consulta SQL se utilizan "palabras clave" que son sustituidas posteriormente.

#nota: Si utilizamos parámetros debemos enviar el tipo de dato que necesita la consulta.
#dato = int(input()) o otro tipo si es otra cosa

#los parámetros en la consulta ya nos los veremos hasta que no se ejecuten

#los nombres de parámetros dependen de la BBDD:

#En oracle, los parámetros se declaran como :nombreparametro
#EJ) sql = f"SELECT APELLIDO, OFICIO, DEPT_NO FROM EMP WHERE DEPT_NO = :iddepartamento" ---> ORACLE

#En SQL Server es @nombreparametro
#EJ) sql = f"SELECT APELLIDO, OFICIO, DEPT_NO FROM EMP WHERE DEPT_NO = @iddepartamento" ---> SQL Server

#posteriormente, con el EXECUTE debemos incluir el valor del parámetro
#cursor.execute(sql, (parametro,))

#ahora siempre lo usaremos así y SIEMPRE VAN EN ORDEN de izquierda a derecha y así los va sustituyendo
