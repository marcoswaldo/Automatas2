#Nombre: circunferencia.py
#objetivo: scrip para calcular el area y diametro de una circunferncia
#math
#Autor: Marcos Oswaldo Gil Naranjo
#Fecha: 1 de julio de 2019

def identifica(l1,l2,l3):
    if(l1==l2 and l2==l3 ):
        print("El triangulo es equilatero : ",l1, ", ", l2,", ",l3)
    elif (l1==l2 and l3!=l1):
          print("El triangulo es isóceles : ",l1, ", ", l2,", ",l3)    
    elif(l1!=l2 and l1!=l3 and l2!=l3 ):
        print("El triangulo es escaleno : ",l1, ", ",l2,", ",l3)
    p=l1+l2+l3 

    print("Perimetro: ",p)        

    
    

def main():
    ciclo=True
    while ciclo==True:
            
        print  ( "----Scrip para identificar triangulos----")
        lado1=float(input("Introduce lado 1: "))

        lado2=float(input("Introduce lado 2: "))
        lado3=float(input("Introduce lado 3: "))

        #invocar
        identifica(lado1,lado2,lado3)
        
        resp= input("Desea hacer otro cálculo: s/n?")
        if (resp=="S" or resp=="s"):
            ciclo= True
        else :
            ciclo=False

if __name__=="__main__":
    main()