print("Numeros narcisistas")

print("Dime un número")
num = input()

longitud = len(num)
resultado = 0
for i in range(longitud):
    numero = int(num[i])
    multi = numero ** longitud #** se usa para exponentes
    print(multi)
    resultado = resultado + multi
    print(resultado)
    if(resultado == num):
        print("narcisista")
    