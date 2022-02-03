#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NATALIA
#
# Created:     17/01/2022
# Copyright:   (c) NATALIA 2022
# Licence:     <your licence>



def fibonacci(n):
    a=0
    b=1
    c=0
    while c<=n:
        if c == 0:
            print(a,", ",end=""),
        else:
            print(c,", ", end=""),
        c= a+b
        b = a
        a = c
    return(n)


try:
    numero = int(input("Ingrese el número hasta el cual desea que le sea mostrada la serie Fibonacci: "))
    fibonacci(numero)
except (ValueError, TypeError, IndexError):
    print("El caracter ingresado no es válido.")
print("")
print("Proceso finalizado")

