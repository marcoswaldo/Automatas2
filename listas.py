#-----------------------------------------
#Nombre: listas.py
#objetivo: Muestra el funcionamiento de las listas en python
#Autor: Marcos Oswaldo Gil Naranjo
#Fecha: 2 de julio de 2019

#------------
#Metodo para crear la lista
#---------------------
lista=[]

#------------------------
#Funcion para agregar items a la lista
#-----------------------------


def agregarItem(dato):
    lista.append(dato)

#Funcion para eliminar item
def eliminarItem(dato):
    if (dato in lista):
        lista.remove(dato)
        print("Dato eliminado")
    else:
        print("Item no existe en la lista")    

#Funcion para impromir lista

def imprimirlista():
    j=0
    for i in lista:
        print("item: ",j,",",i)    
        j=j+1

def main():
    ciclo = True

    while( ciclo==True):
        print("---------Script para trabajar con listas----------")
        print("1.- Agregar elementos a la lista")
        print("2.- Buscar un elemento en la lista")
        print("3.- Modificar un elemento en la lista")
        print("4.- Eliminar un elemento de la lista")
        print("5.- Imprimir los elementos de la lista")
        print("6.- Salir")

        opc = int (input("Elija una opcion entre 1 y 6: "))
        if(opc==1):
            item = input("Introduce el valor del elemento")
            agregarItem(item)
        elif(opc == 2):
            print(" ")
        elif(opc == 3):
            print(" ")
        elif(opc == 4):
            print(" ")
        elif(opc == 5):
            imprimirlista()
        elif(opc == 6):
            print("*** fin del programa")
            ciclo=False
        else:
            print("Selecciona un numero entre 1 y 6: ")

if __name__ == "__main__":
    main()
