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
    
    __balance = 0.0 
    
    # Constructor 
    def __init__(self,id,nombre,apellido,cedulaTipo,cedula,pin):
        
        if ((not isinstance(id, int)) or (id < 0)):
            raise Exception("El ID debe ser entero positivo.")
        
        if ((not isinstance(nombre, str)) or (nombre == "")):
            raise Exception("El nombre debe ser un String no vacio.")
        
        if ((not isinstance(apellido, str)) or (apellido == "")):
            raise Exception("El apellido debe ser un String no vacio.")
        
        if ((not isinstance(cedulaTipo, str)) or (cedulaTipo == "")):
            raise Exception("EL tipo de CI debe ser un String no vacio (V o E).")
        
        if (not isinstance(cedula, int) or (cedula <= 0)):
            raise Exception("La cedula debe ser un Entero positivo")
        
        if (not isinstance(pin, int) or (pin <= 0)):
            raise Exception("El PIN debe ser un Entero positivo")
        
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
    
    def VerificarCuenta(self,cuenta):
        return self.__id == cuenta 
        
# Funcion consumir: Registra un debito en el balance de una billetera.
def Consumir(billet, id_trans, monto, fecha, id_est, pin):
        if (not isinstance(billet, Billetera)):
            raise Exception("billet debe ser instancia de billetera.")
        
        if (not isinstance(monto, float)):
            raise Exception("El monto debe ser numerico.")
        
        if ((not isinstance(id_trans, int)) or (id_trans < 0)):
            raise Exception("El ID_trans debe ser entero positivo.")
        
        if (not isinstance(id_est, int)):
            raise Exception("El id_est debe ser int")

        if (not isinstance(pin, int)):
            raise Exception("El pin debe ser int")
        
        if (monto <= 0.0):
            raise Exception("No se permiten montos negativos")
        if (billet.Saldo() < monto):
            raise Exception("No tiene suficientes fondos en su billetera.")
        if (not(billet.VerificarPIN(pin))):
            raise Exception("El PIN es erroneo.")
        if (not(billet.VerificarPIN(pin))):
            raise Exception("El PIN es erroneo.")
        nuevoDebito = Consumo(id_trans,monto,fecha,id_est) 
        billet.DebitarBalance(nuevoDebito.monto)
 
# Funcion recargar: Registra un credito en el balance de una billetera.     
def Recargar(billet,id_trans, monto, fecha, id_est):

        if not isinstance(billet, Billetera):
            raise Exception("billet debe ser instancia de billetera.")
        
        if not isinstance(monto, float):
            raise Exception("El monto debe ser numerico.")
        
        if not isinstance(id_est, int):
            raise Exception("El id_est debe ser int")
    
        if ((not isinstance(id_trans, int)) or (id_trans < 0)):
            raise Exception("El ID_trans debe ser entero positivo.")
        
        if not isinstance(monto, float):
            raise Exception("El monto debe ser numerico.")
        
        if (not isinstance(id_est, int)):
            raise Exception("El id_est debe ser int")        
    
        if (monto <= 0):
            raise Exception("No se permiten montos negativos")
        nuevoCredito = Recarga(id_trans,monto,fecha,id_est)
        billet.CreditarBalance(nuevoCredito.monto)