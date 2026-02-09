import oracledb

print("conectando a Oracle")
#tenemos un objeto connection que nos pedirá
#(user, password, server)

connection = oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")

print("estamos conectados!!!")

#las consultas select se ejecutan a partir de connection y se crea un objeto llamado curso

#cursor = connection.cursor()

#una vez tenemos el cursor se quejecuta el sql.

#cursor.execute(SQL)