'''
Created on 04/05/2015
@title Clase Consumo 

@author: Fabio Castro 10-10132
@author: Oscar Guillen 11-11264

@Description
            Implementacion de la estructura consumo.
'''

class Consumo:
    
    def __init__(self,id,monto,fecha,establecimiento):
        self.id = id
        self.monto = monto
        self.fecha = fecha
        self.id_establec = establecimiento