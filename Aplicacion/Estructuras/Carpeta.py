# -*- coding:utf-8 -*-
from ArbolB import Btree
import avl

class Carpeta:
    carpetasB=None
    archivosA=None


    def __init__(self):
        self.carpetasB=Btree.Btree()
        self.archivosA=avl.avltree()
        #print "inicializando carpetas"
        #carpetas=arbolB
car=Carpeta()