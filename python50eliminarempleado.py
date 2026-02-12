from oracle50empleados import OracleEmpleados
#Importamos la clase del script aunque podemos importarla directamente
print("----Eliminación de Empleados----")
#Creamos el objeto. que llevará la clase y luego con el nombre.loquesea pues se cambian sus parámetros o ejecutan funciones
oracle = OracleEmpleados()
#Pedimos el dato al usuario
dato = int(input("Introduce el código del empleado: "))
#Registro aquí se convierte en el resultado de nuestro cursor, aquello que ha devuelto la funcion eliminarEmpleado(aquí va el dato)
registro = oracle.eliminarEmpleado(dato)
#Imprimimos y terminamos
print(f"Empleados eliminados: {registro}")
print("Fin de programa")
