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
        
    def VerificarPIN(self,pin):
        return self.__pin == pin
        
# Funcion consumir: Registra un debito en el balance de una billetera.
def Consumir(billet, id_trans, monto, fecha, id_est, pin):
        if (monto < 0):
            raise Exception("No se permiten montos negativos")
        if (billet.Saldo() < monto):
            raise Exception("No tiene suficientes fondos en su billetera.")
        if (not(billet.VerificarPIN(pin))):
            raise Exception("El PIN es erroneo.")
        nuevoDebito = Consumo(id_trans,monto,fecha,id_est) 
        billet.DebitarBalance(nuevoDebito.monto)
 
# Funcion recargar: Registra un credito en el balance de una billetera.     
def Recargar(billet,id_trans, monto, fecha, id_est):
        if (monto < 0):
            raise Exception("No se permiten montos negativos")
        nuevoCredito = Recarga(id_trans,monto,fecha,id_est)
        billet.CreditarBalance(nuevoCredito.monto)