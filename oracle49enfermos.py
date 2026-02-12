import oracledb
class OracleEnfermos:
    #Aquí declarabamos lo que tiene la clase
    #declarar las propiedades en el constructor
    def __init__(self):
        self.connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

    #Los métodos que queramos. Cada método tendrá la norma de Entrar/Salir
    def eliminarEnfermo(self, inscripcion):
        #Creamos un cursor: Entrar
        cursor = self.connection.cursor()
        sql = "DELETE FROM ENFERMO WHERE INSCRIPCION = :insc"
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        self.connection.commit()
        #Ahora cerramos el cursor: Salir
        cursor.close()
        return registros
