class Camion:
    __id=0
    __nombre=""
    __patente=""
    __marca=""
    __tara=0.0
    def __init__(self,id=None,nombre=None,patente=None,marca=None,tara=None):
        if type(id)==int and type(nombre)==str and type(patente)==str and type(marca)==str and type(tara)==float:      
            self.__id=id
            self.__nombre=nombre
            self.__patente=patente
            self.__marca=marca
            self.__tara=tara
        else:
            print("error en algun tipo de datos ingresado")
    def retornaId(self):
        return self.__id
    def retornaTara(self):
        return self.__tara
    def retornaPatente(self):
        return self.__patente
    def retornaNombre(self):
        return self.__nombre
