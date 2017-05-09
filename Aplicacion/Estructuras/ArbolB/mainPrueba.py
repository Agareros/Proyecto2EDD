# -*- coding:utf-8 -*-
import Clave
import Btree
import random


clave=Clave.Clave(0)
arbol=Btree.Btree()

for i in range(1,22):
    clave=Clave.Clave(i)
    #arbol.Inserta(clave)

seguir=True

while (seguir):
    print "---------------"
    print("0.Ingresar")
    print("1.Eliminar")
    print("2.Imprimir")
    print("3.Salir")
    respuesta = raw_input()
    numero=int(respuesta)
    if(numero==0):
        print("Dato a ingresar")
        respuesta2=raw_input()
        clave=Clave.Clave(respuesta2)
        arbol.Inserta(clave)
        print("Insertado")
    if(numero==1):
        print("Dato a eliminar")
        respuesta2=raw_input()
        clave=Clave.Clave(respuesta2)
        arbol.Eliminar(clave)
        print("Eliminado")
    if(numero==2):
        print"----  ArbolB  -------"
        arbol.ImprimirDot()
    if(numero==3):
        seguir=False

"""
clave =Clave.Clave("arbol")
arbol.Inserta(clave)

clave =Clave.Clave("vaca")
arbol.Inserta(clave)

clave =Clave.Clave("pie")
arbol.Inserta(clave)
clave =Clave.Clave("dedo")
arbol.Inserta(clave)

clave =Clave.Clave("estructura")
arbol.Inserta(clave)
"""

#for i in range(5,7):
   # clavEliminar = Clave.Clave(i)
    #arbol.Eliminar(clavEliminar)
arbol.ImprimirDot()
"""
print "Raiz->|Cuentas->"+str(arbol.p.Cuentas)
for i in range(arbol.p.Cuentas):
    print "["+str(i)+"]->"+str(arbol.p.Claves[i].clave)

print "Rama 0 ->|Cuentas->"+str(arbol.p.Ramas[0].Cuentas)
for i in  range(arbol.p.Ramas[0].Cuentas):
    print "["+str(i)+"]->"+str(arbol.p.Ramas[0].Claves[i].clave)

print "Rama 1 ->|Cuentas->"+str(arbol.p.Ramas[1].Cuentas)
for i in range(arbol.p.Ramas[1].Cuentas):
    print "["+str(i)+"]->"+str(arbol.p.Ramas[1].Claves[i].clave)

"""