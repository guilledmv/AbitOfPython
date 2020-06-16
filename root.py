#We need to use math library
import math
print("Program for calculating roots")
#We use an amount of intentos
intento = 0
numero=int(input("Enter a number, please : "))

while numero < 0 :
        print("Error: root is not posible for negative numbers")
        #If we use 3 or more intentos--> Final 
        if intento == 2 :
                print("Too many intentos")
                break;

        numero=int(input("Enter a number, please : "))
        if numero <0 :
                intento+=1
if intento < 2 and numero > 0:
        solucion= math.sqrt(numero)
        print("root of "+str(numero)+" is "+str(solucion))
