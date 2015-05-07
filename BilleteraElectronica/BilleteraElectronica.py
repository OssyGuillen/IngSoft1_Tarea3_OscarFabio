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
from recarga import Recarga
import datetime

class Billetera:
    
    __balance = 0 
    
    def __init__(self,id,nombre,apellido,cedulaTipo,cedula,pin):
        self.__id              = id
        self.__nombre          = nombre
        self.__apellido        = apellido
        self.__cedulaTipo     = cedulaTipo
        self.__cedula         = cedula
        self.__pin            = pin
        
    # Metodo Saldo: retorna el balance de la billetera.    
    def Saldo(self):
        return self.__balance
    
    # Metodo DebitarBalance: registra un debito en el balance.
    def DebitarBalance(self, monto):
        self.__balance -= monto
        
    # Metodo CreditarBalance: registra un credito en el balance.    
    def CreditarBalance(self,monto):
        self.__balance += monto
        
# Funcion consumir: Registra un deito en el balance de una billetera.
def Consumir(billet, id_trans, monto, fecha, id_est):
        nuevoDebito = Consumo(id_trans,monto,fecha,id_est) 
        billet.DebitarBalance(nuevoDebito.monto)
        
def Recargar(billet,id_trans, monto, fecha, id_est):
        nuevoCredito = Recarga(id_trans,monto,fecha,id_est)
        billet.CreditarBalance(nuevoCredito.monto)