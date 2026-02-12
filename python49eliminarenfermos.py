from oracle49enfermos import OracleEnfermos

print("----Eliminando enfermos----")
#Creamos el objeto que llevará la clase OracleEnfermo() y con eso nos referiremos a partir de ahora
oracle = OracleEnfermos()
print("Introduzca la inscripción")
dato = int(input())
registros = oracle.eliminarEnfermo(dato)
print(f"Enfermos eliminados: {registros}")
print("Fin de programa")