print("--------------------------------")

#variables
horas = int(input("INTRODUZCA HORAS SEMANALES: "))
precioh = int(input("INTRODUZCA IMPORTE HORA: "))
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
    salarioex = (precioh + 1.5) * horaex
    bruto = (horanormal * precioh) + salarioex

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

print("------------------------------")
print("HORAS TRABAJADAS :" )
