 # -*- coding:utf-8 -*-
import Clave
from array import array
import random

class Bnodo:
    Ramas = [None]*5
    Claves = [None]*4
    Cuentas = 0
    id = "0"
    idPadre="0"
    carpetaArbol=None
    carpetaNombre=None
    

    def __init__(self):
        self.Cuentas = 0
        self.Claves = [Clave.Clave(0)]*4
        self.id= "Nodo" + str(random.randrange(999999999999))
        
    def iRamas(self):
        self.Ramas = [Bnodo()]*5

    def iBnodo(self,clave):
        self.Claves[0] = clave
        self.Ramas = [Bnodo()]*5