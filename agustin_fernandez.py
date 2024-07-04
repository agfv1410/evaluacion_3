from os import system
from funciones import añadir
from funciones import listar
system("cls")
while True:
    print("""1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa
    """)
    op=int(input("ingrese una opcion:"))

    match op:
        case 1:
            añadir()
            system("cls")
            pass
        case 2:
            listar()
            system("cls")
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("saliste del programa")
            break
        case _:
            print("debe ingresar una opcion valida")


