# -*- coding:utf-8 -*-
import Clave
import Bnodo
import Queue as queue

class Btree:
    p = Bnodo.Bnodo()
    Xder =Bnodo.Bnodo()
    Xizq = Bnodo.Bnodo()
    X=Clave.Clave(0)
    Xr=Bnodo.Bnodo()
    salida = " "
    imps= " "
    EmpA=False
    Esta=False

    ###############################
    #Constructor
    ###############################
    def __init__(self):
        self.Xr.iRamas()
        self.Xder.iRamas()
        self.Xizq.iRamas()
        self.p.iRamas()
        

    ###############################
    #Insertando un nodo en el arbolB
    ###############################


    def Inserta(self,Clave):
        self.Insertaa(Clave,self.p)
    
    def nuevaCarpeta(self,carpeta,Carpetas):
        clave=Clave.Clave(carpeta)
        clave.carpetas=Carpetas

        self.Insertaa(clave,self.p)
        
    def Insertaa(self,Clave,raiz):
        self.Empujar(Clave,raiz)
        if self.EmpA:
            self.p = Bnodo.Bnodo()
            self.p.iRamas()
            self.p.Cuentas=1
            self.p.Claves[0]=self.X
            self.p.Ramas[0]=raiz
            self.p.Ramas[1]=self.Xr
       # print "Insercion exitosa"


    def MeterHoja(self,Clave,raiz,k):
        i=raiz.Cuentas
        while i is not k:
            raiz.Claves[i]=raiz.Claves[i-1]
            raiz.Ramas[i+1]=raiz.Ramas[i]
            i=i-1
        raiz.Claves[k]=Clave
        raiz.Ramas[k+1]=self.Xr
        raiz.Cuentas=raiz.Cuentas+1
    
    def DividirN(self,Clave,Raiz,k):
        pos = 0
        Posmda = 0
        if k <= 2:
            Posmda = 2
        else:
            Posmda = 3
        Mder = Bnodo.Bnodo()
        Mder.iRamas()#inicializo las ramas
        pos = Posmda+1
        while pos is not 5:
            Mder.Claves[(pos-Posmda)-1] = Raiz.Claves[pos-1]
            Mder.Ramas[pos-Posmda] = Raiz.Ramas[pos]
            pos=pos+1
        Mder.Cuentas=4-Posmda
        Raiz.Cuentas=Posmda
        if k<= 2:
            self.MeterHoja(Clave,Raiz,k)
        else:
            self.MeterHoja(Clave,Mder,k-Posmda)
        self.X=Raiz.Claves[Raiz.Cuentas-1]
        Mder.Ramas[0]=Raiz.Ramas[Raiz.Cuentas]
        Raiz.Cuentas=Raiz.Cuentas-1
        self.Xr=Mder

    def Empujar(self,Clave,raiz):
        k=0
        self.Esta=False
        if self.Vacio(raiz):
            self.EmpA=True
            self.X=Clave
            self.Xr=Bnodo.Bnodo()#aquí era null
            self.Xr.iRamas()
        else:
            k=self.BuscarNodo(Clave,raiz)
            if self.Esta:
                print "No hay clases repetidas"
                self.EmpA=False
            else:
                self.Empujar(Clave,raiz.Ramas[k])
                if self.EmpA:
                    if raiz.Cuentas<4:
                        self.EmpA=False
                        self.MeterHoja(self.X, raiz, k);
                    else:
                        self.EmpA=True
                        self.DividirN(self.X, raiz, k);

    ###############################
    #Metodos generales
    ###############################


    def Vacio(self,raiz):
        if (raiz==None or raiz.Cuentas==0):
            return True
        else:
            return False
    
    def BuscarNodo(self,Clave,raiz):
        j=0
        if (Clave.clave < raiz.Claves[0].clave):
            self.Esta=False
            j=0
            return j
        else:
            j=raiz.Cuentas
            while (Clave.clave < raiz.Claves[j-1].clave and j>1):
                j=j-1
            self.Esta = (Clave.clave == raiz.Claves[j-1].clave)
            return j

    ###############################
    #Eliminar
    ###############################
    def MoverDer(self,raiz,pos):
        i=raiz.Ramas[pos].Cuentas
        while i is not 0:
            raiz.Ramas[pos].Claves[i]=raiz.Ramas[pos].Claves[i-1]
            raiz.Ramas[pos].Ramas[i+1]=raiz.Ramas[pos].Ramas[i]
            i=i-1
        raiz.Ramas[pos].Cuentas=raiz.Ramas[pos].Cuentas+1
        raiz.Ramas[pos].Ramas[1]=raiz.Ramas[pos].Ramas[0]
        raiz.Ramas[pos].Claves[0]=raiz.Claves[pos-1]
        raiz.Claves[pos-1]=raiz.Ramas[pos-1].Claves[raiz.Ramas[pos-1].Cuentas-1]
        raiz.Ramas[pos].Ramas[0]=raiz.Ramas[pos-1].Ramas[raiz.Ramas[pos-1].Cuentas]
        raiz.Ramas[pos-1].Cuentas=raiz.Ramas[pos-1].Cuentas-1
    
    def MoverIzq(self,raiz,pos):
        i=0
        raiz.Ramas[pos-1].Cuentas=raiz.Ramas[pos-1].Cuentas+1
        raiz.Ramas[pos-1].Claves[raiz.Ramas[pos-1].Cuentas-1]=raiz.Claves[pos-1]
        raiz.Ramas[pos-1].Ramas[raiz.Ramas[pos-1].Cuentas]=raiz.Ramas[pos].Ramas[0]
        raiz.Claves[pos-1]=raiz.Ramas[pos].Claves[0]
        raiz.Ramas[pos].Ramas[0]=raiz.Ramas[pos].Ramas[1]
        raiz.Ramas[pos].Cuentas=raiz.Ramas[pos].Cuentas-1
        i=1
        while i is not raiz.Ramas[pos].Cuentas+1:
            raiz.Ramas[pos].Claves[i-1]=raiz.Ramas[pos].Claves[i]
            raiz.Ramas[pos].Ramas[i]=raiz.Ramas[pos].Ramas[i+1]
            i=i+1
    
    def Quitar(self,raiz,pos):
        j=pos+1
        while j is not raiz.Cuentas+1:
            raiz.Claves[j-2]=raiz.Claves[j-1]
            raiz.Ramas[j-1]=raiz.Ramas[j]
            j=j+1
        raiz.Cuentas=raiz.Cuentas-1
    
    def Restablecer(self,raiz,pos):
        if pos>0:
            if raiz.Ramas[pos-1].Cuentas>2:
                self.MoverDer(raiz,pos)
            else:
                self.Combina(raiz,pos)
            return
        if raiz.Ramas[1].Cuentas>2:
            self.MoverIzq(raiz,1)
            return 
        else:
            self.Combina(raiz,1)
            return
    
    def Combina(self,raiz,pos):
        j=0
        self.Xder=raiz.Ramas[pos]
        self.Xizq=raiz.Ramas[pos-1]
        self.Xizq.Cuentas=self.Xizq.Cuentas+1
        self.Xizq.Claves[self.Xizq.Cuentas-1]=raiz.Claves[pos-1]
        self.Xizq.Ramas[self.Xizq.Cuentas]=self.Xder.Ramas[0]
        j=1
        while j is not self.Xder.Cuentas+1:
            self.Xizq.Cuentas=self.Xizq.Cuentas+1
            self.Xizq.Claves[self.Xizq.Cuentas-1]=self.Xder.Claves[j-1]
            self.Xizq.Ramas[self.Xizq.Cuentas]=self.Xder.Ramas[j]
            j=j+1
        self.Quitar(raiz,pos)
    
    def Restablecer(self,raiz,pos):
        if pos>0:
            if raiz.Ramas[pos-1].Cuentas>2:
                self.MoverDer(raiz,pos)
            else:
                self.Combina(raiz,pos)
            return
        if(raiz.Ramas[1].Cuentas>2):
            self.MoverIzq(raiz,1)
            return
        else:
            self.Combina(raiz,1)
            return

    def Sucesor(self,raiz,k):
        q=Bnodo.Bnodo()
        q.iRamas()
        q=raiz.Ramas[k]
        while not self.Vacio(q.Ramas[0]):
            q=q.Ramas[0]
        raiz.Claves[k-1]=q.Claves[0]
    
    def EliminarRegistro(self,raiz,c):
        pos=0

        if self.Vacio(raiz):
            self.Esta=False
        else:
            pos=self.BuscarNodo(c,raiz)
            if self.Esta:
                if self.Vacio(raiz.Ramas[pos-1]):
                    self.Quitar(raiz,pos)
                else:
                    self.Sucesor(raiz,pos)
                    self.EliminarRegistro(raiz.Ramas[pos],raiz.Claves[pos-1])
            else:
                self.EliminarRegistro(raiz.Ramas[pos],c)
                if (raiz.Ramas[pos] is not None) and (raiz.Ramas[pos].Cuentas<2):
                    self.Restablecer(raiz,pos)

    def Eliminara(self,Raiz, Clave):
        try:
            self.EliminarRegistro(Raiz,Clave) #aquí va el try catch
            self.Esta = True#esto lo agregue yo
        except:
            self.Esta = False

        if not self.Esta:
            print "Eliminacion fallida->No se econtró el dato"
        else:
            if Raiz.Cuentas==0:
                Raiz =Raiz.Ramas[0]
            self.p=Raiz
            print"Eliminacion completa :)"

    def Eliminar(self,Clave):
        if self.Vacio(self.p):
            print "No hay elementos maje "
        else:
            self.Eliminara(self.p,Clave)
                

    ###############################
    #Imprimir
    ###############################

    def ImprimirDot(self):
        aux = Bnodo.Bnodo()
        aux.iRamas()
        
        if  not self.Vacio(self.p):
            cola = queue.Queue(aux)
            cola.put(self.p)#insertado la raíz a la cola
            
            #print cola.get().Cuentas

            while (not cola.empty()):
                aux=cola.get()


                #print "-------"+str(aux.id)+"----" #imprimiendo
                i=0
                cadena=""
                for i in range(aux.Cuentas):
                    #print "["+str(i)+"]->"+str(aux.Claves[i].clave)
                    if i==0:
                        cadena="<P0>|"
                        cadena= cadena+str(aux.Claves[i].clave)+"|<P1>"
                    else:
                        cadena=cadena+"|"+str(aux.Claves[i].clave)+"|<P"+str(i+1)+">"
                print aux.id+"[label = \""+cadena+"\"];"
                #insertando a la cola
                for i in range(aux.Cuentas+1):
                    try:
                        if not (aux.Ramas[i].Cuentas <= 0): #arbol.p.Ramas[0].Cuentas
                            cola.put(aux.Ramas[i])
                            print aux.id+":P"+str(i)+"->"+aux.Ramas[i].id+";"               
                    except:
                        print "fallo imprimir"
    def recorrerEnAnchura(self):
        print "-------Recorriendo en anchura-----"
        aux = Bnodo.Bnodo()
        aux.iRamas()
        
        if  not self.Vacio(self.p):
            cola = queue.Queue(aux)
            cola.put(self.p)
            while (not cola.empty()):
                aux=cola.get()
                i=0
                cadena=""
                for i in range(aux.Cuentas):
                    print "["+str(i)+"]->"+str(aux.Claves[i].clave)
                #insertando a la cola
                for i in range(aux.Cuentas+1):
                    try:
                        if not (aux.Ramas[i].Cuentas <= 0): #arbol.p.Ramas[0].Cuentas
                            cola.put(aux.Ramas[i])              
                    except:
                        print "fallo imprimir"

    def getCarpetas(self,carpetaPadre):
        retorno = {None:None}
        #dict2 = {'Dos':"Dos"}
        #dict1.update(dict2)
        #la carpetaPadre es de tipo Clave
        print "-------CarpetasEn["+str(carpetaPadre.clave)+"]-----"
        arbolRaiz=carpetaPadre.carpetas.carpetasB.p
        aux = Bnodo.Bnodo()
        aux.iRamas()
        
        if  not self.Vacio(arbolRaiz):
            cola = queue.Queue(aux)
            cola.put(arbolRaiz)
            while (not cola.empty()):
                aux=cola.get()
                i=0
                cadena=""
                for i in range(aux.Cuentas):
                    #print "["+str(i)+"]->"+str(aux.Claves[i].clave)
                    tem={str(i): str(aux.Claves[i].clave)}
                    retorno.update(tem)
                #insertando a la cola
                for i in range(aux.Cuentas+1):
                    try:
                        if not (aux.Ramas[i].Cuentas <= 0): #arbol.p.Ramas[0].Cuentas
                            cola.put(aux.Ramas[i])              
                    except:
                        print "fallo imprimir"
        del retorno[None]
        return retorno

    
    def getCarpeta(self,arbol,nombreCarpeta):
        print "-------RetornandoCarpeta-----"
        aux = Bnodo.Bnodo()
        aux.iRamas()
        carpetaEncontrada=False
        if  not self.Vacio(arbol):
            cola = queue.Queue(aux)
            cola.put(arbol)
            while (not cola.empty()):
                aux=cola.get()
                i=0
                cadena=""
                for i in range(aux.Cuentas):
                    if nombreCarpeta==str(aux.Claves[i].clave):
                        carpetaEncontrada=True
                        print "encontrado"
                        return aux.Claves[i]#retorno una clase CLAVE

                #insertando a la cola
                for i in range(aux.Cuentas+1):
                    try:
                        if not (aux.Ramas[i].Cuentas <= 0): 
                            cola.put(aux.Ramas[i])              
                    except:
                        print "fallo imprimir"
        return None