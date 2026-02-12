import oracledb
class OracleEmpleados:
    #Aquí declarabamos lo que tiene la clase
    #declarar las propiedades en el constructor
    def __init__(self):
        self.connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

    def eliminarEmpleado(self, idEmpleado):
        #Creamos un cursor: Entrar
        cursor = self.connection.cursor()
        sql = "DELETE FROM EMP WHERE EMP_NO = :id"
        cursor.execute(sql, (idEmpleado,))
        registros = cursor.rowcount
        self.connection.commit()
        #Ahora cerramos el cursor: Cerrar
        cursor.close()
        return registros

