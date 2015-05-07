'''
Created on 04/05/2015
@title Tarea 3: Billetera Electronica

@author: Fabio Castro 10-10132
@author: Oscar Guillen 11-11264

@Description
            Implementacion de la clase billetera electronica.
            Estructura creada como servicio de pago...
'''
from consumo import Consumo

class Billetera:
    
    __balance = 0 
    
    def __init__(self,id,nombre,apellido,cedulaTipo,cedula,pin):
        self.__id              = id
        self.__nombre          = nombre
        self.__apellido        = apellido
        self.__cedulaTipo     = cedulaTipo
        self.__cedula         = cedula
        self.__pin            = pin
        
    def Saldo(self):
        return self.__balance
    
    def DebitBalance(self, monto):
        self.__balance -= monto
        

def Consumir(self, wallet, id_trans, monto, fecha, id_est):
        newDebit = Consumo(id_trans,monto,fecha,id_est) 
        wallet.DebitBalance(newDebit.monto)