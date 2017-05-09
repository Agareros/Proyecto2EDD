# -*- coding:utf-8 -*-


class persona:
    nombre=""
    edad=""
    def __init__(self):
        self.nombre=""
    def insertar(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad


dict1 = {None:None}
dict2 = {'Uno':"Dos"}
dict1.update(dict2)
print dict1

"""pepol=persona()
pepol.insertar("Jhosef ","12")
dict = {'Age':pepol}
dict2 = {'dos':pepol}
dict.update(dict2)
#print "Value : %s" %  dict.items()
print dict['Age'].nombre
print dict['dos'].nombre
"""