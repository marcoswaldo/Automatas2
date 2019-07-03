#Nombre: circunferencia.py
#objetivo: scrip para calcular el area y diametro de una circunferncia
#math
#Autor: Marcos Oswaldo Gil Naranjo
#Fecha: 1 de julio de 2019

import math as mat
import os

#Funcion para calcular area
def calcularArea(r):
    area = mat.pi*(mat.pow(r,2))
    return area

#Funcion para calcular el diametro

def calculaDiametro(d):
    diam= d*2
    return diam

def main():
    ciclo = True

    while ciclo==True:
        print("--Script para calcular Área de circunferncia")
        radio = float (input("introduce el valor del radio: "))

        # invoncare el metodo
        print("El área es : ",calcularArea(radio))
        print("El diametro es: ",calculaDiametro(radio))

        resp= input("Desea hacer otro cálculo: s/n?")
        if (resp=="S" or resp=="s"):
            ciclo= True
        else :
            ciclo=False


if __name__=="__main__":
         main()