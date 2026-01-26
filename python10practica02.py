print("-------------------------------------")

#VARIABLES
horas = float(input("INTRODUZCA HORAS SEMANALES: "))
precio_hora = float(input("INTRODUZCA IMPORTE HORA: "))
kilometro = int(input("INTRODUZCA KILOMETROS: "))


hora_normal  = 0
hora_extra = 0

salario_extra = 0
#salario_base = horas * precio_hora
#salario_bruto = salario_base 
iva = 0
neto = 0

dieta = ""
reten = ""
#Hacemos los calculos de las horas extra si son necesarias y si no que se quede con lo original
if(horas > 36 ):
    hora_normal = 36
    hora_extra = horas - hora_normal
    salario_base = hora_normal * precio_hora
    salario_extra = (precio_hora + 1.5) * hora_extra
    salario_bruto = salario_base + salario_extra
else:
    salario_base = horas * precio_hora
    salario_bruto = salario_base 

#Hacemos los calculos finales del IVA y el neto
iva = salario_bruto * 0.16
neto = salario_bruto - iva

#Añadimos en tipo de dieta según los kilometros
if(kilometro < 101):
    dieta = "PROVINCIAL"
elif(kilometro > 101 and kilometro < 900):
    dieta = "NACIONAL"
else:
    dieta = "INTERNACIONAL"

#Calculamos las retenciones segun el salario
if(salario_bruto < 250 or salario_bruto == 250):
    reten = "0%"
elif(salario_bruto > 250 and salario_bruto < 500 or salario_bruto == 500):
    reten = "20%"
else:
    reten = "50%"

#Mostramos los resultados en pantalla
print("-------------------------------------")
print("HORAS TRABAJADAS:", str(horas)+"h")
print("HORAS EXTRAS:", str(hora_extra)+"h")
print("IMPORTE DE LA HORA:", str(precio_hora)+"€")
print("DISTANCIA EN KM:", str(kilometro)+"km")
print("DESTINO:", dieta)
print("RETENCIÓN:", reten)
print("SALARIO BASE:", str(salario_base)+"€")
print("SALARIO HORAS EXTRA:", str(salario_extra)+"€")
print("SALARIO BRUTO:", str(salario_bruto)+"€")
print("IVA (16%):", str(iva)+"€")
print("-------------------------------------")
print("SALARIO TOTAL:", str(neto)+"€")
print("-------------------------------------")
print("FIN DE PROGRAMA")