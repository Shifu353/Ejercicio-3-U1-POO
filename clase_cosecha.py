class Cosecha:
    __lista=[]
    def __init__(self):
        for i in range(45):
            self.__lista.append([])
            for j in range(20):
                self.__lista[i].append(None)
    def registrarviaje(self,id=1,dia=1,kg=0.0):
        if type (id)==int and type(dia)==int and type(kg)==float and (dia<46 and dia>0):  
            if self.__lista[dia-1][id-1] is not None:
                self.__lista[dia-1][id-1]+=kg
            else:
                self.__lista[dia-1][id-1]=kg
        else:
            print("Tipo de dato erroneo o rango de dia incorrecto dias:1-45 ")
    def mostrarTotalKg(self,id):
        if id>20 or id<1:
            return -1
        else:
            acumulador=0
            id-=1
            for elemento in self.__lista:
                if elemento[id] is not None:
                    acumulador+=elemento[id]
            return acumulador
    def informedelDia(self,dia=1,listacamiones=[]):
        if type(dia)==int and type(listacamiones)==list and (dia<46 and dia>0):
            dia-=1
            print("{}       {}       {}".format("PATENTE" ,"CONDUCTOR", "CANTIDAD DE KILOS"))
            for camion in listacamiones:
                id=camion.retornaId()
                if self.__lista[dia][id-1] is not None:
                    print("{}       {}         {:.2f}".format(camion.retornaPatente(),camion.retornaNombre(),self.__lista[dia][id-1]))
                else:
                    print("{}       {}          {}".format(camion.retornaPatente(),camion.retornaNombre(),0))
        else:
            print("dia erroneo el rango de dias varia entre 1-45")
    def test(self,lista):
        self.registrarviaje(1,90,3000.4)
        self.registrarviaje(5,45,23)
        self.registrarviaje(5,45,900.5)
        self.registrarviaje(1,45,800.0)
        self.registrarviaje(10,45,1000.1)
        print("test id 1 kg:",self.mostrarTotalKg(1))
        print("test dia 45:")
        self.informedelDia(45,lista)
