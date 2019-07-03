#Nombre: Serie de Fibonacci.py
#objetivo: scrip para calcular la serie de fibonacci
#Autor: Marcos Oswaldo Gil Naranjo
#Fecha: 1 de julio de 2019

import math

def calcula(dato):
    ant=0
    act=1
    print(ant)
    print(act)
    for i in range (dato-2):
        serie=ant+act
        ant=act
        act=serie
        print(serie)

       

def main():
    print("----serie de fibonacci----")
    num=int(input("Ingrese el un número de iteraciones:  "))
    calcula(num)
    

if __name__ == "__main__":
    main()