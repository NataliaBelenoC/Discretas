#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NATALIA
#
# Created:     31/01/2022
# Copyright:   (c) NATALIA 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def reverseString(s):
  return s[::-1]

def de_base_10(numero,base):
    num=""
    while numero!=0:
        num = num+str(numero%base)
        #print(str(numero%base))
        #print(numero)
        numero = math.trunc(numero/base)
        #print(numero)
        #print(base)
        #print("")
    return(reverseString(num))


def a_base_10(numero, base):
	num = 0

	for i, digito in enumerate(reverseString(str(numero))):
		num = num + int(digito) * base ** i

	return(num)


print("Este programa permite convertir un número en base 6,7,8 o 9, en base 10, y de base 10, a las bases anteriormente mencionadas. ")
print("")
try:
    numero = int(input("Ingrese el número que desea convertir: "))
    base1 = int(input("Ingrese la base del número que desea convertir: "))
    base2 = int(input("Ingrese la base a la cual desea convertirlo: "))
    if (base1 == 6 or base1 == 7 or base1 == 8 or base1 == 9) and base2 == 10:
        print("")
        print(numero," en base ",base1, ", es ",a_base_10(numero,base1)," en base ",base2)
    elif base1 == 10 and (base2 == 6 or base2 == 7 or base2 == 8 or base2 == 9):
        print("")
        print(numero," en base ",base1, ", es ",de_base_10(numero,base2)," en base ",base2)
    else:
        print("La base ingresada no es válida")

except (ValueError, TypeError, IndexError):
    print("El caracter ingresado no es válido.")
print("")
print("Proceso finalizado")
