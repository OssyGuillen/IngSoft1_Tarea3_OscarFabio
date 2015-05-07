'''
Created on 04/05/2015
@title Tarea 3: Test Billetera

@author: Fabio Castro 10-10132
@author: Oscar Guillen 11-11264

@Description
            Implementacion del archivo para los casos de prueba.
'''
import unittest
import datetime
from BilleteraElectronica import *
from consumo import Consumo
from recarga import Recarga

class testBilletera(unittest.TestCase):
############## Pruebas para la estrategia TDD. ##########

    # Prueba para crear la clase billetera.
    def test_InitBilletera(self):
        nuevaBilletera = Billetera("id","oscar","guillen",'V',21444449,5594)
        
    # Prueba para crear la clase consumo.
    def test_Consumo(self):
        nuevoDebito = Consumo("id",1000,datetime.datetime(2015,5,23,18,25,0,0),"id_est")
        
    # Prueba para crear la clase recarga.
    def test_Recarga(self):
        nuevoCredito = Recarga("id",1000,datetime.datetime(2015,5,23,18,25,0,0),"id_est")
    
    # Prueba para crear la funcion Saldo.    
    def test_Saldo(self):
        nuevaBilletera = Billetera("id","oscar","guillen",'V',21444449,5594)
        self.assertEqual(nuevaBilletera.Saldo(), 0)
    # Prueba para crear la funcion consumir()
    def test_Consumir(self):
        nuevaBilletera = Billetera("id","oscar","guillen",'V',21444449,5594)
        Consumir(nuevaBilletera,"id",1000,datetime.datetime(2015,5,23,18,25,0,0),"id_est")
        
    # Prueba para crear la funcion recargar()    
    def test_Recargar(self):
        nuevaBilletera = Billetera("id","oscar","guillen",'V',21444449,5594)
        Recargar(nuevaBilletera, "id",1000,datetime.datetime(2015,5,23,18,25,0,0),"id_est")