#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NATALIA
#
# Created:     30/01/2022
# Copyright:   (c) NATALIA 2022
# Licence:     <your licence>
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    print(num," es primo")
    return True

def primos_rango(num1, num2):
    for i in range(num1, (num2+1)):
        es_primo(i)


#primos_rango(1,10)


try:
    num1 = int(input("Ingrese el número desde el cual desea que le sean mostrados los primos: "))
    num2 = int(input("Ingrese el número hasta el cual desea que le sean mostrados los primos: "))
    primos_rango(num1, num2)
    
except (ValueError, TypeError, IndexError):
    print("Uno de los caracteres ingresado no es válido.")
print("")
print("Proceso finalizado")
