from clase_cosecha import Cosecha
from clase_camion import Camion
import csv
if __name__=='__main__':
    #funciones del menu de opciones
    def op1():
        camion=int(input("Ingresa el id del camion:"))
        resultado=cosecha.mostrarTotalKg(camion)
        if resultado!=-1:    
            print("{:.3f}".format(resultado))
        else:
            print("Id erronea, debe ser en el rango 1-20")
    def op2():
        dia=int(input("Ingresa el dia para recibir el informe:"))
        cosecha.informedelDia(dia,lista)
    def op3():
        cosecha.test(lista)
    def salir():
        print("salio del programa")
    bandera=0
    lista=[]
    archivo=open("camiones.csv")
    archivo2=open("datoscosecha.csv")
    reader=csv.reader(archivo,delimiter=";")
    for fila in reader:
        if(bandera==0):
            bandera=1
        else:
            lista.append(Camion(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4])))
    archivo.close()  
    reader=csv.reader(archivo2,delimiter=";")
    longitud=len(lista)
    cosecha=Cosecha()
    bandera=0
    for fila in reader:
        if(bandera==0):
            bandera=1
        else:
            i=0
            idc=int(fila[0])
            while((i<longitud)and(idc!=lista[i].retornaId())):
                i+=1
            if(i<longitud):
                kgcamion=float(fila[2])-lista[i].retornaTara()
                cosecha.registrarviaje(idc,int(fila[1]),kgcamion)
            else:
                print("No se encontro el id del camión, no se añadio la carga del mismo, id:",fila[0])
    archivo2.close()
    diccdeopciones={1:op1,2:op2,3:op3,4:salir}
    opcion=None
    while(opcion!=4):
        print("Menu de opciones:")
        print("Ingresa 1 para mostrar la cantidad de kilos descargados por un camión indicado")
        print("Ingresa 2 para mostrar el informe de un día ingresado ")
        print("Ingresa 3 para ejecutar un test")
        print("Ingresa 4 para salir")
        opcion=int(input("Ingresa opción:"))
        op=diccdeopciones.get(opcion,lambda:print("Opcion incorrecta, ingresar 3 para salir o las otras opciones 1 o 2"))
        op()
