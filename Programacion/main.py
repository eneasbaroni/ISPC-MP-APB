""" 
SkyRoute - Agencia de Viajes
Este programa permite a los usuarios registrarse, iniciar sesión, ver destinos disponibles y comprar pasajes.
Para ver los pasos de instalacion y uso, consulta el archivo README.md.
"""


from destinos import destinos
from menu import menu
from cuotas import cuotas
from usuarios import crear_usuario, loguearse, usuarios, ver_pasajes, anular_pasaje_usuario
from viajes import mostrar_destinos, comprar_pasajes


usuario_logueado = None

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

def menu_ver_pasajes():
    while True:
        print("\n=== Opciones de Pasajes ===")
        print("1. Volver al menú principal")
        print("2. Salir")
        print("3. Arrepentimiento de compra")
        opcion = input("Elegí una opción: ")
        return opcion

def navegar_menu(menu):
    global usuario_logueado
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

            if eleccion == "1" and subeleccion == "1":
                crear_usuario(usuarios)
            elif eleccion == "1" and subeleccion == "2":
                usuario = loguearse(usuarios)
                if usuario:
                    usuario_logueado = usuario['email']
            elif eleccion == "1" and subeleccion == "4":
                if usuario_logueado:
                    pasajes_vistos = ver_pasajes(usuario_logueado, mostrar_opciones=False)
                    if pasajes_vistos:
                        opcion_pasajes = menu_ver_pasajes()
                        if opcion_pasajes == "1":
                            continue # Volver al menú principal
                        elif opcion_pasajes == "2":
                            break # Salir del programa
                        elif opcion_pasajes == "3":
                            anular_pasaje_usuario(usuario_logueado, pasajes_vistos)
                else:
                    print("\n⚠️ Debes iniciar sesión para ver tus pasajes.\n")
                    if volver_o_salir():
                        continue # Volver al menú principal
                    else:
                        break # Salir del programa
            elif eleccion == "1" and subeleccion == "5":
                if usuario_logueado:
                    usuario_logueado = None
                    print("\n✅ Sesión cerrada.\n")
                else:
                    print("\n⚠️ No hay sesión activa para cerrar.\n")
            elif eleccion == "2" and subeleccion == "1":
                mostrar_destinos(destinos)
                if not volver_o_salir(): 
                    break
            elif eleccion == "2" and subeleccion == "2":
                if usuario_logueado is None:
                    print("\n⚠️ Debes iniciar sesión para comprar pasajes. \n")
                    if volver_o_salir():
                        continue # Volver al menú principal
                    else:
                        break # Salir del programa
                else:
                    comprar_pasajes(destinos, cuotas, usuario_logueado)
            else:
                print("\nFuncionalidad aún no implementada.\n")

navegar_menu(menu)