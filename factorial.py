#Nombre: Factorial.py
#objetivo: scrip para calcular el factorial de un numero
#Autor: Marcos Oswaldo Gil Naranjo
#Fecha: 1 de julio de 2019

import math

def calcula(dato):
    fac=dato
    while(dato>1):
        fac=(dato-1)*fac        
        dato=dato-1

    return fac    

def main():
    print("----Factoria----")
    num=int(input("Ingrese el un número entero:  "))
    print (calcula(num))
    

if __name__ == "__main__":
    main()