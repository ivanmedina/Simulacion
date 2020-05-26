import sys
sys.path.append('./../RandomFunctions')
import math
import functions as al

class cajero():


    Eventos=[]
#
    reloj=0
    fila=0
    limfila=8
    dinero=3000000
    limdinero=3000000
    cajero=False
    estatus=""
    llegadas=0
    eventos=0
    satisfechos=0
    instatisfechos=0
    tipo=""
    limeventos=21

    def __init__(self):
        pass


    def llegadaClientes(self):
        self.relof=self.reloj+1
        self.eventos=self.eventos+1
        self.tipo="llegadaClientes"
        self.agregarEvento()
        if self.cajero:
            if self.fila==0:
                atencionCliente()
            else:
                if fila>0:
                    if self.fila<self.limfila+1:
                        self.fila=self.fila
                    else:
                        self.salidaCliente()


    def salidaCliente(self):
        self.relof=self.reloj+1
        self.eventos=self.eventos+1
        self.agregarEvento()
        if self.dinero<=self.limdinero:
            abastecimientoCajero()
        if self.fila>0:
            self.fila=self.fila-1
            self.reloj=self.reloj+1
            self.eventos=eslf.eventos+1
            self.atencionCliente()
        else:
            pass



    def atencionCliente(self):
        catidad=0
        self.reloj=self.reloj+1
        self.eventos=self.eventos+1
        self.cajeros=False
        self.agregarEvento()
        self.cantidad=int(math.random()*3000)+100
        if self.dinero<self.cantidad:
            self.abastecimientoCajero()
        else:
            self.dinero=self.cantidad
            self.satisfechos=self.satisfechos+1
            self.salidaCliente()

        if(self.fila>0):
            self.fila=self.fila-1
            #self.atencionCliente()

    def abastecimientoCajero(self):
        self.reloj=self.reloj+1
        self.eventos=self.eventos+1
        self.cajero=False
        self.tipo='abastecimientoCajero'
        while(self.dinero<self.limdinero):
            self.dinero=self.dinero+1
        self.cajero=True
        if self.fila==0:
            self.atencionCliente()



    def agregarEvento(self):
        if self.eventos < self.limeventos:
            self.Eventos.add({'evento':self.eventos,'reloj':self.reloj,'operacion':self.tipo, 'dinero':self.dinero, 'filas':self.filas,'satisfechos':self.satisfechos, 'instatisfechos':self.instatisfechos})
