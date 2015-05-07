'''
Created on 04/05/2015
@title Tarea 3: Billetera Electronica

@author: Fabio Castro 10-10132
@author: Oscar Guillen 11-11264

@Description
            Implementacion de la clase billetera electronica.
            Estructura creada como servicio de pago...
'''
from django.db import models

class Billetera(models.Model):
    
    balance = 0 
    
    def __init__(self,id,nombre,apellido,cedulaTipo,cedula,pin):
        self.id              = id
        self.nombre          = nombre
        self.apellido        = apellido
        self.cedulaTipo     = cedulaTipo
        self.cedula         = cedula
        self.pin            = pin