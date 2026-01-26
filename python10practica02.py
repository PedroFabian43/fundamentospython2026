print("-------------------------------------")

#VARIABLES
horas = float(input("INTRODUZCA HORAS SEMANALES: "))
precioh = float(input("INTRODUZCA IMPORTE HORA: "))
kilometro = int(input("INTRODUZCA KILOMETROS: "))


horanormal  = 0
horaex = 0

salarioex = 0
salariobase = horas * precioh
bruto = salariobase 
iva = 0
neto = 0

dieta = ""
reten = ""
#Hacemos los calculos de las horas extra si son necesarias
if(horas > 36 ):
    horanormal = 36
    horaex = horas - horanormal
    salariobase = horanormal * precioh
    salarioex = (precioh + 1.5) * horaex
    bruto = salariobase + salarioex

iva = bruto * 0.16
neto = bruto - iva

if(kilometro < 101):
    dieta = "PROVINCIAL"
elif(kilometro > 101 and kilometro < 900):
    dieta = "NACIONAL"
else:
    dieta = "INTERNACIONAL"

if(bruto < 250 or bruto == 250):
    reten = "0%"
elif(bruto > 250 and bruto < 500 or bruto == 500):
    reten = "20%"
else:
    reten = "50%"

print("-------------------------------------")
print("HORAS TRABAJADAS:", str(horas)+"h")
print("HORAS EXTRAS:", str(horaex)+"h")
print("IMPORTE DE LA HORA:", str(precioh)+"€")
print("DISTANCIA EN KM:", str(kilometro)+"km")
print("DESTINO:", dieta)
print("RETENCIÓN:", reten)
print("SALARIO BASE:", str(salariobase)+"€")
print("SALARIO HORAS EXTRA:", str(salarioex)+"€")
print("SALARIO BRUTO:", str(bruto)+"€")
print("IVA (16%):", str(iva)+"€")
print("-------------------------------------")
print("SALARIO TOTAL:", str(neto)+"€")
print("-------------------------------------")
print("FIN DEL PROGRAMA")

