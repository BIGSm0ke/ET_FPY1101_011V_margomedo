import json
import csv
import statistics
import random


def leer_json(nombre):
    with open(nombre,"r",encoding="UTF-8")as archivo:
        archivo=json.load(archivo)
        return archivo.get("AFPS")
    
def rut():
    while True:
        rut=input("Ingrese un rut cond formato 00000000-0/k: ").upper()
        ruut=rut.split("-")
        if ruut[0].isdigit() and len(ruut[0])==8:
            if ruut[1].isdigit() or ruut[1]=="K" and len(ruut[1])==1:
                print("El rut es correcto")
                return rut
            else:
                print("Rut incorrrecto") 
        else:
            print("Rut incorrrecto") 

def menu(lista):
    while True:
        i=1
        for elemen in lista:
            print (i,".- ",elemen)
            i+=1
        print (f"{i} .- Salir")
        opc=input("Ingrese una opcion: ")  
        
        if opc.isdigit():
            opc=int(opc)
            if 1<=opc<=i:
                return opc
            else:
                print("Solo numeros dentro del menu")
        else:
            print("Opcion fuera del menu")


def menu2(lista):
    while True:
        i=1
        for elemen in lista:
            print (i,".- ",elemen)
            i+=1
        opc=input("Ingrese una opcion: ")  
        
        if opc.isdigit():
            opc=int(opc)
            if 1<=opc<=(i-1):
                return opc
            else:
                print("Solo numeros dentro del menu")
        else:
            print("Opcion fuera del menu")



def nombre(texto):
    while True:
        con=0
        nom=input(texto)
        nombres=nom.split(" ")
        if len(nombres)==2 or len(nombres)==1:
            for temp in nombres:
                if temp.isalpha():
                    con+=1
                else:
                    break
                if len(nombres)==con:
                    nom=nom.title()
                    return nom
        else:
            print("Solo 1 o 2 nombres")
def apellido(texto):
    while True:
        con=0
        nom=input(texto)
        nombres=nom.split(" ")
        if len(nombres)==2:
            for temp in nombres:
                if temp.isalpha():
                    con+=1
                else:
                    break
                if len(nombres)==con:
                    nom=nom.title()
                    return nom
        else:
            print("Solo dos apellidos")

def edad():
    while True:
        try:
            edad=int(input("ingrese su edad: "))
            if 21<edad<120:
                return edad
            else:
                print("Solo rango de 21 a 120")
        except:
            print("Ingrese solo numeros")

def nivel(opciones):
    while True:
        for x,y in opciones.items():
            print(f"{x} = {y} ",end="/")
        respuesta=input("Opcion: ").upper()
        x=list(opciones)
        
        if respuesta in x:
            return opciones.get(respuesta)
        else:
            print("Opcion fuera del menu")


def Afps(archivo):
    lista=[]
    while True:
        for temp in archivo:
            lista.append(temp.get("NOMBRE"))
        lista.append("Ninguna")
        return lista

def acu():
    while True:
        try:
            saldo=int(input("Ingrese su saldo disponible: "))
            if saldo>1000000:
                return saldo
            else:
                print("Debe ser superior a $1.000.000")
        except:
            print("Solo numeros enteros") 


def busca(rut,lista):
    while True:
        texto=""
        for temp in lista:
            if temp.get("Rut")==rut:
                for x,y in temp.items():
                    print(f"{x} = {y}")
                    texto=texto+str(x)+"="+str(y)+"\n"
                with open("CERTIFICADO AFILIADO.txt","w")as archivo:
                    archivo.write(texto)
                return 
        print ("Rut no encontrado")
        return
    

def sueldo(templista):
    empleados={}
    for x in templista:
        sueldo=random.randint(300000,2500000)
        empleados[x]=sueldo
    return empleados


def clas(templista):
    clas1={}
    clas2={}
    clas3={}
    total=0
    for x,y in templista.items():
        if y<800000:
            clas1[x]=y
        elif 800000<=y<=2000000:
            clas2[x]=y
        elif y>2000000:
            clas3[x]=y
    print("=================================")
    print("Menores a 800.000 = ",len(clas1))
    for x,y in clas1.items():
        print(f"{x} = {y}")
    print("=================================")
    print("Entre 800.000 y 2.000.000 = ",len(clas2))
    for x,y in clas2.items():
        print(f"{x} = {y}")
    print("=================================")
  
    print("Mayores a 2.000.000 = ",len(clas3))
    for x,y in clas3.items():
        print(f"{x} = {y}")
    print("=================================")
  
    for x,y in templista.items():
        total=total+y
    print("Total = ",total)
    print("=================================")

def alto(tempjsosn,sueldos):
    sueldo=max(sueldos)
    for x,y in tempjsosn.items():
        if y==sueldo:
            print("==================")
            print("Sueldo mas alto")
            print(f"{x} = {y}")
            print("==================\n")
    return sueldo
    
def bajo(tempjsosn,sueldos):
    sueldo=min(sueldos)
    for x,y in tempjsosn.items():
        if y==sueldo:
            print("==================")
            print("Sueldo mas bajo")
            print(f"{x} = {y}")
            print("==================\n")
    return sueldo
def prom(sueldos):
    prom=statistics.mean(sueldos)
    print("==================")
    print("Promedio de sueldos = ",prom)
    print("==================\n")
    return prom

def geo(sueldos):
    geo=statistics.geometric_mean(sueldos)
    print("==================")
    print("Promedio de sueldos = ",geo)
    print("==================\n")
    return geo

def reporte(tempjson):
    nombres=["Nombre Empleado","Sueldo Base","Descuentos Salud","Descuentos AFP","Sueldo Liquido"]
    listatotal=[]
    for x,y in tempjson.items():
        lista=[]
        lista.append(x)
        lista.append(y)
        salud=int(round(y*0.07,0))
        lista.append(salud)
        afp=int(round(y*0.12,0))
        lista.append(afp)
        liquido=y-salud-afp
        lista.append(liquido)
        listatotal.append(lista)

    for x in nombres:
        print(x,end="  |  ")
    print()
    for x in listatotal:
        for y in x:
            print(y,end="  |  ")
        print()

def crear_csv(tempjson):
    nombres=["Nombre Empleado","Sueldo Base","Descuentos Salud","Descuentos AFP","Sueldo Liquido"]
    listatotal=[]
    for x,y in tempjson.items():
        lista=[]
        lista.append(x)
        lista.append(y)
        salud=int(round(y*0.07,0))
        lista.append(salud)
        afp=int(round(y*0.12,0))
        lista.append(afp)
        liquido=y-salud-afp
        lista.append(liquido)
        listatotal.append(lista)
    try:
        with open("Reporte sueldos.csv","w",encoding="UTF-8")as archivo:
            escritura=csv.writer(archivo)
            escritura.writerow(nombres)
            escritura.writerows(listatotal)
        print("==================")
        print("Archivo Creao/actualizado")
        print("==================\n")
    except:
        print("==================")
        print("Cierre el archivo csv")
        print("==================\n")











