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
    
def clasificar_sueldos(sueldos):
    clasificacion = {"Menores a $800000": [], "Entre $800000 y $2000000": [], "Superiores a $2000000": []}

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["Menores a $800000"].append((trabajador, sueldo))
        elif sueldo < 2000000:
            clasificacion["Entre $800000 y $2000000"].append((trabajador, sueldo))
        else:
            clasificacion["Superiores a $2000000"].append((trabajador, sueldo))

    print("Clasificación de sueldos:")
    for categoria, empleados in clasificacion.items():
        print(f"{categoria} - Total: {len(empleados)}")
        for trabajador, sueldo in empleados:
            print(f"{trabajador}: {sueldo}")
        print()

    print(f"Total sueldos: {sum(sueldos.values())}")

def reporte_sueldos(sueldos):
    with open('sueldos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=";")
        escritor_csv.writerow(['Nombre empleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])
        
        for trabajador, sueldo in sueldos.items():
            descuento_salud = round(sueldo * 0.07)
            descuento_afp = round(sueldo * 0.12)
            sueldo_liquido = round(sueldo - descuento_salud - descuento_afp)
            
            escritor_csv.writerow([trabajador, round(sueldo, 2), descuento_salud, descuento_afp, sueldo_liquido])
