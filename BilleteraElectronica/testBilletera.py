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
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,5594)

    # Prueba para crear la clase recarga.
    def test_Recarga(self):
        nuevoCredito = Recarga(10,1000,datetime.datetime.now(),0)
             
    # Prueba para crear la clase consumo.
    def test_Consumo(self):
        nuevoDebito = Consumo(10,1000,datetime.datetime.now(),0)
    
    # Prueba para crear la funcion Saldo.    
    def test_Saldo(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertEqual(nuevaBilletera.Saldo(), 0)
        
    # Prueba para crear la funcion recargar()    
    def test_Recargar(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        
    # Prueba para crear la funcion consumir()
    def test_Consumir(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        Consumir(nuevaBilletera,0,1000,datetime.datetime.now(),0,1234)
        
    # Prueba para agregar Validaciones a consumir().
    def test_DebitarSalgoNegativo(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,nuevaBilletera, 0, -1000, datetime.datetime.now(),1,1234)
    
    # Prueba para agregar Validaciones a recargar().
    def test_RecargarSalgoNegativo(self):
        nuevaBilletera = Billetera(2,"susa","rodriguez",'V',21444450,1234)
        Recargar(nuevaBilletera,2,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Recargar,nuevaBilletera, 2, -1000, datetime.datetime.now(),2)
        
    # Prueba para agregar Validaciones a consumir().
    def test_DebitarSinBalance(self):
        nuevaBilletera = Billetera(4,"patricia","reinoso",'V',21444452,1234)
        self.assertRaises(Exception,Consumir,nuevaBilletera, 4, 1000, datetime.datetime.now(),4,1234)
        
    # Prueba para agregar Validacion de Pin a consumir().
    # Para esto se tendra que agregar otro campo a la funcion consumir 
    # para la entrada del PIN.
    def test_VerificacionDePIN(self):
        nuevaBilletera = Billetera(1,"oscar","guillen",'V',21444449,5594)
        self.assertRaises(Exception,Consumir,nuevaBilletera, 1, 1000, datetime.datetime.now(),1,5595)
        
    # Prueba para valores incorrectos al crear una billetera.
    def test_BilleteraCorrecta(self): 
        self.assertRaises(Exception,Billetera,1,1,1,1,"21444449","5594")
        
    def test_RecargaMontoMaximoInvalido(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera, 0, datetime.datetime.now(),1)

    def test_RecargaMontoNegativo(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,-10,datetime.datetime.now(),1)

    def test_RecargaFechaPasada(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,10,datetime.datetime(2015,5,23,18,25,0,0),1)

    def test_RecargaFechaFutura(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,10,datetime.datetime(2016,5,23,18,25,0,0),1)
    
    def test_RecargaMuyGrande(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,10000000000000000000000000000000000000000,datetime.datetime.now(),1)

    def test_RecargaMinimaNoPermitida(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,1,datetime.datetime.now(),1)

    def test_RecargaMinimaPermitidaEntera(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        temp = nuevaBilletera.Saldo()
        Recargar(nuevaBilletera,0,1,datetime.datetime.now(),0)
        temp2= nuevaBilletera.Saldo()
        self.assertEqual(temp2,1+temp)

    def test_RecargaCuentaInvalida(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,10,datetime.datetime.now(),20000)
    
    def test_RecargaTexto(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,"RECARGA TEXTO",datetime.datetime.now(),20000)

    def test_RecargaDecimalNormal(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,0.57,datetime.datetime.now(),20000)

    def test_RecargaDecimalChico(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        self.assertRaises(Exception,Recargar,nuevaBilletera,0.0057,datetime.datetime.now(),20000)

    def test_DebitoMontoNegativo(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,1,0,datetime.datetime.now(),1,1234)

    def test_DebitoMontoNegativo(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,2,-1,datetime.datetime.now(),1,1234)
    
    def test_DebitoFechaPasada(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,3,10,datetime.datetime(2015,5,23,18,25,0,0),1,1234)
        
    def test_DebitoFechaFutura(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,4,10,datetime.datetime(2016,5,23,18,25,0,0),1,1234)
    
    def test_DebitoMuyGrande(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,5,10000000000000000000000000000000000000000,datetime.datetime.now(),1,1234)

    def test_DebitoMinimoNoPermitido(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,6,1,datetime.datetime.now(),1,1234)

    def test_DebitoMinimoPermitido(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        temp = nuevaBilletera.Saldo()
        Consumir(nuevaBilletera,7,10,datetime.datetime.now(),20000,1234)
        temp2= nuevaBilletera.Saldo()
        self.assertEqual(temp2,temp-10)
    
    def test_DebitoTexto(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        self.assertRaises(Exception,Consumir,6,"PRUEBAAA",datetime.datetime.now(),1,1234)

    def test_DebitoDecimalNormal(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        temp = nuevaBilletera.Saldo()
        Consumir(nuevaBilletera,7,127.23,datetime.datetime.now(),20000,1234)
        temp2= nuevaBilletera.Saldo()
        self.assertEqual(temp2,temp-127.23)
    
    def test_DebitoDecimalChico(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        temp = nuevaBilletera.Saldo()
        Consumir(nuevaBilletera,7,0.0057,datetime.datetime.now(),20000,1234)
        temp2= nuevaBilletera.Saldo()
        self.assertEqual(temp2,temp-0.0057)
    
    def test_DebitarCantidadExacta(self):
        nuevaBilletera = Billetera(0,"oscar","guillen",'V',21444449,1234)
        Recargar(nuevaBilletera,0,1000,datetime.datetime.now(),0)
        Consumir(nuevaBilletera,7,1000,datetime.datetime.now(),20000,1234)
        self.assertEqual(nuevaBilletera.Saldo(),0)