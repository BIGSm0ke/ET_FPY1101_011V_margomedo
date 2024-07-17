import json
import csv
import Funciones as f

opciones=["Ingresar","Buscar","Generacion de informe"]
ense={"B":"Basica",
      "M":"Media",
      "S":"Superior",
      "N":"Sin estudios"}
Todo=[]
A__f__p=f.leer_json("Afps.json")
Lista_afp=f.Afps(A__f__p)

while True:

    empleado={}
    opc=f.menu(opciones)
    aaffpp=[]
    if opc==1:
        
        rut=f.rut()
        nombre=f.nombre("Ingrese nombres: ")
        apellido=f.apellido("Ingrese apellidos: ")
        edad=f.edad()
        nivel=f.nivel(ense)
        while True:
            a_f_p=f.menu(Lista_afp)
            if a_f_p==24:
                 break
            if a_f_p==23:
                 afp="Ninguna"
            else:     
                afp=A__f__p[a_f_p-1]
                afp=afp.get("SOCIEDAD")
            if afp not in aaffpp: 
                aaffpp.append(afp)
        saldo=f.acu()
        
        empleado["Rut"]=rut
        empleado["Nombre"]=nombre
        empleado["Apellido"]=apellido
        empleado["Edad"]=edad
        empleado["Nivel de estudios"]=nivel
        empleado["Afp"]=aaffpp
        empleado["Saldo disponible"]=saldo

        Todo.append(empleado)
    elif opc==2:
        ruut=f.rut()
        f.busca(ruut,Todo)
        
    elif opc==3:
        with open("Informe.json","w")as archivo:
                json.dump(Todo,archivo)

    elif opc==4:
        for temp in Todo:
            nom=temp.get("Nombre")
            ap=temp.get("Apellido")
            saldo=temp.get("Saldo disponible")
            print(f"Saldo disponible de {nom} {ap} = {saldo}")
        print("Hasta la proxima, espero que vuelva a ocupar nuestro servicio")
        break