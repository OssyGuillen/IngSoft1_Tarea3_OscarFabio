'''
Created on 04/05/2015
@title Tarea 3: Test Billetera

@author: Fabio Castro 10-10132
@author: Oscar Guillen 11-11264

@Description
            Implementacion del archivo para los casos de prueba.
'''
import unittest
from BilleteraElectronica import Billetera

class testBilletera(unittest.TestCase):
############## Pruebas para la estrategia TDD. ##########

    # Prueba para crear la clase billetera.
    def test_InitBilletera(self):
        newPocket = Billetera("id","oscar","guillen",'V',21444449,5594)
        
    # Prueba para crear la clase consumo.
    def test_Consumo(self):
        newDebit = Consumo("id",1000,datetime.datetime(2015,5,23,18,25,0,0),"id_est")
        
    # Prueba para crear la clase recarga.
    def test_Recarga(self):
        newCredit = Recarga("id",1000,datetime.datetime(2015,5,23,18,25,0,0),"id_est")