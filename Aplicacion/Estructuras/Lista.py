# -*- coding:utf-8 -*-
from ArbolB import Btree
from ArbolB import Clave
import Carpeta
class Nodo:
    usuario=None
    contra=None
    root=None
    ruta=None

    def insertar(self,usuario,contra):
        self.usuario = str(usuario)
        self.contra = str(contra)
        self.root=Clave.Clave(0)
        self.root.carpetas=Carpeta.Carpeta()
        #self.root=Carpeta.Carpeta()

    def inicializar(self,tipo):
        self.anterior=tipo
        self.siguiente=tipo

class Lista:
    cabeza=None

    def vacio(self):
        if self.cabeza==None:
            return True
        else:
            return False
    
    def registrarUsuario(self, usuario, contra):
        nuevo=Nodo()
        nuevo.inicializar(Nodo())
        nuevo.insertar(usuario,contra)
        if self.vacio():
            self.cabeza=nuevo
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo
            self.cabeza=nuevo
    
    def login(self,usuario,contra):
        retorno="False"
        if self.vacio():
            retorno = "False"
        else:
            aux=self.cabeza
            ant=Nodo()
            while aux.usuario is not None:
                if (aux.usuario==usuario) and (aux.contra==contra):
                    retorno="True"
                aux=aux.siguiente
                    #break
        return retorno
    
    def retornoNodo(self,usuario,contra):
        retorno=None
        if self.vacio():
            retorno = "False"
        else:
            aux=self.cabeza
            ant=Nodo()
            while aux.usuario is not None:
                if (aux.usuario==usuario) and (aux.contra==contra):
                    retorno=aux
                    break
                aux=aux.siguiente
                    #break
        return retorno 
        
    def insertar(self,dato):
        nuevo=Nodo()
        nuevo.inicializar(Nodo())
        nuevo.insertar(dato)
        if self.vacio():
            self.cabeza=nuevo
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo
            self.cabeza=nuevo


    def imprimir(self):
        print "-----ImprimiendoLista-----"
        if self.vacio():
            print "Lista vacia"
        else:
            aux=self.cabeza
            while aux.usuario is not None:
                print "Usuario->"+aux.usuario+" | Contraseña->"+aux.contra
                aux=aux.siguiente
    
    def eliminar(self, usuario,contra):
        if self.vacio():
            print "Lista vacia"
        else:
            aux=self.cabeza
            ant=Nodo()
            while aux.usuario is not None:
                if (aux.usuario==usuario) and (aux.contra==contra):
                    if ant.usuario==None:                        
                        self.cabeza=self.cabeza.siguiente
                        aux.siguiente=None
                        aux=self.cabeza
                        break
                    else:
                        ant.siguiente=aux.siguiente
                        aux.siguiente=None
                        aux=ant.siguiente
                        break
                ant=aux
                aux=aux.siguiente




"""
dato=Lista()
for i in range(3):
    dato.insertar(i)
dato.imprimir()
dato.eliminar("2")
dato.eliminar("1")
dato.eliminar("0")
dato.imprimir()
dato.insertar("12")
dato.imprimir()
"""
"""
lis=Lista()
lis.registrarUsuario("jhosef","123")
lis.registrarUsuario("dato","dato")
lis.registrarUsuario("contra","user")

lis.imprimir()
print lis.login("jhosef","123")
print lis.login("jhosef","1234")
"""