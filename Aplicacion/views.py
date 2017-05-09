# -*- coding:utf-8 -*-
from django.shortcuts import render
from Estructuras import Lista
from Estructuras import Carpeta
from Estructuras.ArbolB import Btree
from django.contrib import messages   
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
# Create your views here.
lista= Lista.Lista()


def drive_home(request):
    return render(request,'login.html')

def login(request):
    return render(request, 'Login.html')

def registro(request):
    
    #lista.insertar("jhosef")
    #lista.imprimir()
    print "entro"
    #return render(request, 'Registro.html')
    if request.method=="POST":
        usuario=request.POST['usuario']
        password=request.POST['password']
        repassword=request.POST['repassword']
        archivo =request.POST['archivo']

        if password == repassword:
            print "son iguales"
        else:
            print "no mames"
        print usuario
        print password
        print repassword
        print archivo
        
        messages.add_message(request, 50, 'Hola Jhosef')
        return render(request, 'Registro.html')
    else:
        return render(request,'Registro.html')
#====================================================================================[Funciones]============================

def retornarNodoUsuario(request):
    retorno= None
    if 'nombre' in request.session:
        nombre =request.session['nombre']
        contra =  request.session['contra']
        retorno= lista.retornoNodo(nombre,contra)
    else:
        retorno=None
    return retorno 

def ruta(request,path):
    arbolOperaciones=Btree.Btree()
    #arbolOperaciones.p.iRamas()
    print "========[Path]========"
    nodoUsuario = retornarNodoUsuario(request)
    Clave=nodoUsuario.root #root es de la clase Carpeta
    for item in path.split('/'):
        if str(item)=="root":
            Clave=nodoUsuario.root
        else:
            Clave=arbolOperaciones.getCarpeta(Clave.carpetas.carpetasB.p,str(item))
    arbolOperaciones.getCarpetas(Clave)

def diccionarioCarpetas(request):
    arbolOperaciones=Btree.Btree()
    path=str(request.session['ruta'])
    #arbolOperaciones.p.iRamas()
    print "========[DiccionarioCarpetas]========"
    print path
    nodoUsuario = retornarNodoUsuario(request)
    Clave=nodoUsuario.root #root es de la clase Carpeta
    for item in path.split('/'):
        if str(item)=="root":
            Clave=nodoUsuario.root
        else:
            Clave=arbolOperaciones.getCarpeta(Clave.carpetas.carpetasB.p,str(item))
    return arbolOperaciones.getCarpetas(Clave)

def retornarClave(request):
    arbolOperaciones=Btree.Btree()
    path=str(request.session['ruta'])
    #arbolOperaciones.p.iRamas()
    print "========[DiccionarioCarpetas]========"
    print path
    nodoUsuario = retornarNodoUsuario(request)
    Clave=nodoUsuario.root #root es de la clase Carpeta
    for item in path.split('/'):
        if str(item)=="root":
            Clave=nodoUsuario.root
        else:
            Clave=arbolOperaciones.getCarpeta(Clave.carpetas.carpetasB.p,str(item))
    return Clave

#====================================================================================[Django]============================

def loginDjango(request):
    
    if request.method=="POST":
        usuario=request.POST['usuario']
        password=request.POST['contra']
        print "--------LoginDjango-----"
        print usuario
        print password
        if lista.login(usuario,password)=="True":
            request.session['nombre'] = usuario
            request.session['contra']= password
            request.session['ruta']="root"

            return render(request,'Drive_Carpetas.html')
        else:
            return render(request, 'Drive_Login.html')
    else:
        return render(request,'Drive_Login.html')


def logoutDjango(request):
    try:
        del request.session['nombre']
        del request.session['contra']
        del request.session['ruta']
    except KeyError:
        pass
    return render(request,'Drive_Login.html')

def verSesion(request):
    print "---Variables de sesion----"
    if 'nombre' in request.session:
        print request.session['nombre']
        print request.session['contra']

        nod = retornarNodoUsuario(request)
        print nod.usuario
        return render(request, 'Drive_Carpetas.html')
    else:
        print "No hay sesion iniciada"
        return render(request,'Drive_Login.html')
        
    
    #return HttpResponse("Sesiones")

def registrarDjango(request):
    arbolOperaciones=Btree.Btree()
    if request.method=="POST":
        usuario=request.POST['usuario']
        password=request.POST['contra']
        repetir=request.POST['repetir']
       
        print "--------RegistrarDjango-----"
        
        
        print usuario
        print password
        print repetir
        if repetir==password:#se registra el usuario
            lista.registrarUsuario(usuario,password)

            request.session['nombre'] = usuario
            request.session['contra']=password
            request.session['ruta'] ="root"

            nod = retornarNodoUsuario(request)
            nod.root.carpetas.carpetasB.nuevaCarpeta("Archivos",Carpeta.Carpeta())
            nod.root.carpetas.carpetasB.nuevaCarpeta("Estructuras",Carpeta.Carpeta())
            nod.root.carpetas.carpetasB.nuevaCarpeta("Fotos",Carpeta.Carpeta())
            nod.root.carpetas.carpetasB.nuevaCarpeta("Recuerdos",Carpeta.Carpeta())
            """
            nod.root.carpetasB.nuevaCarpeta("Imagenes",Carpeta.Carpeta())
            nod.root.carpetasB.nuevaCarpeta("Juegos",Carpeta.Carpeta())
            nod.root.carpetasB.nuevaCarpeta("Fotos",Carpeta.Carpeta())
            nod.root.carpetasB.nuevaCarpeta("Recuerdos",Carpeta.Carpeta())
            nod.root.carpetasB.nuevaCarpeta("Computadoras",Carpeta.Carpeta())
            nod.root.carpetasB.nuevaCarpeta("Utensilios",Carpeta.Carpeta())
            nod.root.carpetasB.nuevaCarpeta("PlayBoy",Carpeta.Carpeta())
            """
            #ruta(request,"root")
            #ruta(request,"root/")
            #ruta(request,"root/home")
            #ruta(request,"root/home/")
            
            print "-----cadenaDot-----"
            nod.root.carpetas.carpetasB.ImprimirDot()
            nod.root.carpetas.carpetasB.recorrerEnAnchura()

            nuevaCar=arbolOperaciones.getCarpeta(nod.root.carpetas.carpetasB.p,"Archivos")
            nuevaCar.carpetas.carpetasB.nuevaCarpeta("Hijo",Carpeta.Carpeta())
            nuevaCar.carpetas.carpetasB.nuevaCarpeta("Hijo1",Carpeta.Carpeta())
            nuevaCar.carpetas.carpetasB.nuevaCarpeta("Hijo2",Carpeta.Carpeta())
            nuevaCar.carpetas.carpetasB.recorrerEnAnchura()

            hijo=arbolOperaciones.getCarpeta(nuevaCar.carpetas.carpetasB.p,"Hijo")
            hijo.carpetas.carpetasB.nuevaCarpeta("Subhijo",Carpeta.Carpeta())
            hijo.carpetas.carpetasB.nuevaCarpeta("Subhijo1",Carpeta.Carpeta())
            hijo.carpetas.carpetasB.nuevaCarpeta("Subhijo2",Carpeta.Carpeta())
            hijo.carpetas.carpetasB.recorrerEnAnchura()
            #ruta(request,"root/Archivos/Hijo")
            print diccionarioCarpetas(request)
            #print "-----getCarpetas---"
            #ca=nod.root.carpetas.getCarpeta("Archivos")#este es 
            #print ca
            return render(request,'Drive_Carpetas.html',{'carpetas':diccionarioCarpetas(request)})
        else:
            return render(request, 'Drive_Registrar.html')
    else:
        return render(request,'Drive_Registrar.html')

def carpetasDjango(request):
    
    if request.method=="POST":
        print "--------CarpetasDjango-----"
        accion = request.POST.get('sCheck',False)
        carpetas=request.POST.get('iCheck',False)
        archivos=request.POST.get('aCheck',False)
        textBox=request.POST.get('textBox',False)


        if accion=="Atras":

            print "atras"

        #---Carpetas
        elif accion=="C_Ir":
            request.session['ruta']=str(request.session['ruta'])+"/"+carpetas
        elif accion=="C_Nuevo":
            clav=retornarClave(request)
            clav.carpetas.carpetasB.nuevaCarpeta(textBox,Carpeta.Carpeta())
            print "C_Nuevo"
        elif accion=="C_Modificar":
            print "C_Modificar"

        elif accion=="C_Eliminar":
            print "C_Eliminar"

        elif accion=="C_Compartir":
            print "C_Compartir"
        
        #---Carpetas
        elif accion=="A_Nuevo":
            print "A_Nuevo"

        elif accion=="A_Modificar":
            print "A_Modificar"

        elif accion=="A_Eliminar":
            print "A_Eliminar"

        elif accion=="A_Compartir":
            print "A_Compartir"

        elif accion=="A_Descargar":
            print "A_Descargar"

        elif accion=="A_Subir":
            print "A_Subir"
            
        


        #dict = {'Name':pepol, 'Age':pepol}
        
        #print carpetas
        #print archivos
        #print accion
        #print textBox
    diccionario2={'Name':"Perez", 'Age':"Lugi",'Apellido':"Juanes"}
    return render(request, 'Drive_Carpetas.html',{'carpetas': diccionarioCarpetas(request),'diccionario2': diccionario2})

def masterDjango(request):
    return render(request,'Drive_Carpetas.html')



#====================================================================================[Android]============================
@csrf_exempt
def registroAndroid(request):
    
    #lista.insertar("jhosef")
    #lista.imprimir()
    print "entro android"
    #return render(request, 'Registro.html')
    if request.method=="POST":
        usuario=request.POST['nombre']
        password=request.POST['password']
        lista.registrarUsuario(usuario,password)
        print usuario
        print password
        return HttpResponse("Se registro:Bienvenido "+usuario)
    else:
        return HttpResponse("Diano")


@csrf_exempt
def loginAndroid(request):
    
    #lista.insertar("jhosef")
    #lista.imprimir()
    print "entro android"
    #return render(request, 'Registro.html')
    if request.method=="POST":
        usuario=request.POST['nombre']
        password=request.POST['password']
        print usuario
        print password
        return HttpResponse(lista.login(usuario,password))
    else:
        return HttpResponse("No me has enviado nada")


@csrf_exempt
def android(request):
    
    #lista.insertar("jhosef")
    #lista.imprimir()
    print "entro android"
    #return render(request, 'Registro.html')
    if request.method=="POST":
        usuario=request.POST['nombre']
        password=request.POST['password']

        print usuario
        print password
        return HttpResponse("Navarro")
    else:
        return HttpResponse("Diano")