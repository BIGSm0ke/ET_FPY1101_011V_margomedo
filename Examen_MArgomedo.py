import Funciones as f
import random
import csv

menu=["Asignar sueldos aleatorios","Clasificar Sueldos","Ver estadisticas","Reporte de sueldos"]
empleado=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
listasueldos=[]
while True:
    opc=f.menu(menu)


    if opc==1:
        xd=f.sueldo(empleado)
        for x,y in xd.items():
            listasueldos.append(y)
        print("")
        print("==================")
        print("Sueldos generados")
        print("==================\n")

    elif opc==2:
        try:
            f.clas(xd)
        except:
            print("")
            print("==================")
            print("Primero genere sueldos")
            print("==================\n")

    elif opc==3:
        try:
            alto=f.alto(xd,listasueldos)
            bajo=f.bajo(xd,listasueldos)
            promedio=f.prom(listasueldos)
            geo=f.geo(listasueldos)
        except:
            print("")
            print("==================")
            print("Primero genere sueldos")
            print("==================\n")
    elif opc==4:
        try:
            f.reporte(xd)
            f.crear_csv(xd)
        except:
            print("")
            print("==================")
            print("Primero genere sueldos")
            print("==================\n")
    elif opc==5:
        print("Finalizando programa.........")
        print("Desarrollado por Mathias Argomedo")
        print("22.136.959-9")
        break
    