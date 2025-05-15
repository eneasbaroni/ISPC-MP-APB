from destinos import destinos
from menu import menu
from cuotas import cuotas
from usuarios import crear_usuario, loguearse, usuarios
from viajes import mostrar_destinos, comprar_pasajes




def mostrar_menu_principal(menu):
    print("=== Menú Principal ===")
    for opcion, datos in menu.items():
        print(f"{opcion}. {datos['nombre']}")
    print("0. Salir")

def volver_o_salir():
    while True:
        print("1. Volver al menú principal")
        print("0. Salir")
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            return True  # Volver al menú
        elif opcion == "0":
            print("¡Hasta luego!")
            return False  # Salir del programa
        else:
            print("Opción no válida. Intentá de nuevo.\n")



def navegar_menu(menu):
    print("Bienvenido a la agencia de viajes SkyRoute 🛩️")
    while True:
        mostrar_menu_principal(menu)
        eleccion = input("Elegí una opción: ")

        if eleccion == "0":
            print("¡Hasta luego!")
            break

        if eleccion in menu:
            submenu = menu[eleccion]["submenu"]
            print(f"--- {menu[eleccion]['nombre']} ---")
            for subopcion, texto in submenu.items():
                print(f"{subopcion}. {texto}")
            
            subeleccion = input("Elegí una opción del submenú: ")

            if eleccion == "2" and subeleccion == "1":
                mostrar_destinos(destinos)
            elif eleccion == "2" and subeleccion == "2":
                comprar_pasajes(destinos, cuotas)
            elif eleccion == "1" and subeleccion == "1":
                crear_usuario(usuarios)
            elif eleccion == "1" and subeleccion == "2":
                loguearse(usuarios)
            else:
                print("Funcionalidad aún no implementada.\n")

            if not volver_o_salir():
                break
        else:
            print("Opción no válida. Por favor intentá de nuevo.\n")

navegar_menu(menu)