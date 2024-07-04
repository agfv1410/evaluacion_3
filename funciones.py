def añadir():
    from os import system
    from random import random
    system("cls")
    persona=[]
    id= random()
    nom=input("ingrese nombre:")
    while  True:
        if nom.isnumeric() or nom=="":
            nom=input("debe ser un nombre:")
        else:
            break

    ape=input("ingrese apellido:")
    while  True:
        if ape.isnumeric() or ape=="":
            ape=input("debe ser un apellido:")
        else:
            break

    comuna=input("ingrese comuna:")

    while  True:
        if comuna.isnumeric() or comuna=="":
            comuna=input("debe ser una comuna:")
        else:
            break

    direccion=input("ingrese direccion:")

    print("añada dispensadores:")
    disp_1=0
    disp_2=0
    disp_3=0
    total_disp=0
    while True:
        print("""
            1. 6 litros
            2. 10 litros
            3. 20 litros
            0. salir""")
        cant=int(input())
        
        match cant:
            case 1:
                disp_1= disp_1+1
                total_disp=total_disp+1
            case 2:
                disp_2=disp_2+1
                total_disp=total_disp+1
            case 3:
                disp_3=disp_3+1
                total_disp=total_disp+1
            case 0:
                break
            case _:
                print("debe ingresar una opcion valida")
    if total_disp==0:
        print("no ha añadido nada")
    else:
        print("ID pedido",id,"\nusuario: ",nom,ape,"\ndireccion: ",direccion,"\nsector: ",comuna,"\ndisp.6ltrs: ",disp_1,"\ndisp.10ltrs: ",disp_2,"\ndisp.20ltrs: ",disp_3)
        persona.append(id)
        persona.append(nom)
        persona.append(ape)
        persona.append(direccion)
        persona.append(comuna)
        persona.append(disp_1)
        persona.append(disp_2)
        persona.append(disp_3)
        personas=[]
        personas.append(persona)
    return personas
def listar():
    for i in añadir():
        print("ID pedido",añadir[i],"\nusuario: ",añadir[i],"\ndireccion: ",añadir[i],"\nsector: ",añadir[i],"\ndisp.6ltrs: ",añadir[i],"\ndisp.10ltrs: ",añadir[i],"\ndisp.20ltrs: ",añadir[i])
