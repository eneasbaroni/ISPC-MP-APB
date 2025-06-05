""" 
SkyRoute - Agencia de Viajes
Este programa permite a los usuarios registrarse, iniciar sesión, ver destinos disponibles y comprar pasajes.
Para ver los pasos de instalacion y uso, consulta el archivo README.md.
"""
import config
import dbConnection
import gestionClientes
import gestionDestinos
import gestionVentas
import datetime

# --- Funciones de Menú ---

def menu_gestion_clientes(conn):
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Ver todos los clientes")
        print("2. Ver un cliente específico")
        print("3. Crear nuevo cliente")
        print("4. Editar cliente existente")
        print("5. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionClientes.listar_clientes(conn)
        elif opcion == '2':
            try:
                cliente_id = int(input("Ingrese el ID del cliente a ver: "))
                gestionClientes.ver_cliente(conn, cliente_id)
            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '3':
            razon_social = input("Ingrese la razón social: ")
            cuit = input("Ingrese el CUIT: ")
            email = input("Ingrese el email: ")
            gestionClientes.insertar_cliente(conn, razon_social, cuit, email)
        elif opcion == '4':
            try:
                cliente_id = int(input("Ingrese el ID del cliente a editar: "))
                razon_social = input("Nueva razón social (dejar vacío para no cambiar): ")
                cuit = input("Nuevo CUIT (dejar vacío para no cambiar): ")
                email = input("Nuevo email (dejar vacío para no cambiar): ")

                exito_edicion = gestionClientes.editar_cliente(conn, cliente_id,
                                                            razon_social if razon_social else None,
                                                            cuit if cuit else None,
                                                            email if email else None)

                if exito_edicion:
                    print(f"Operación de edición para el cliente ID {cliente_id} completada.")
                else:
                    pass 

            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '5':
            try:
                cliente_id = int(input("Ingrese el ID del cliente a eliminar: "))
                gestionClientes.eliminar_cliente(conn, cliente_id)
            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_destinos(conn):
    while True:
        print("\n--- Gestión de Destinos ---")
        print("1. Ver todos los destinos")
        print("2. Ver un destino específico")
        print("3. Crear nuevo destino")
        print("4. Editar destino existente")
        print("5. Eliminar destino")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionDestinos.listar_destinos(conn)
        elif opcion == '2':
            try:
                destino_id = int(input("Ingrese el ID del destino a ver: "))
                gestionDestinos.ver_destino(conn, destino_id)
            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '3':
            ciudad = input("Ingrese la ciudad: ")
            pais = input("Ingrese el país: ")
            try:
                costo_base = float(input("Ingrese el costo base: "))
                gestionDestinos.insertar_destino(conn, ciudad, pais, costo_base)
            except ValueError:
                print("Costo base inválido. Por favor, ingrese un número.")
        elif opcion == '4':
            try:
                destino_id = int(input("Ingrese el ID del destino a editar: "))
                ciudad = input("Nueva ciudad (dejar vacío para no cambiar): ")
                pais = input("Nuevo país (dejar vacío para no cambiar): ")
                costo_base_str = input("Nuevo costo base (dejar vacío para no cambiar): ")

                costo_base = float(costo_base_str) if costo_base_str else None

                exito_edicion = gestionDestinos.editar_destino(conn, destino_id,
                                                            ciudad if ciudad else None,
                                                            pais if pais else None,
                                                            costo_base)

                if exito_edicion:
                    print(f"Operación de edición para el destino ID {destino_id} completada.")
                else:
                    pass

            except ValueError:
                print("ID o costo base inválido. Por favor, ingrese un número.")
        elif opcion == '5': 
            try:
                destino_id = int(input("Ingrese el ID del destino a eliminar: "))
                gestionDestinos.eliminar_destino(conn, destino_id)
            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_gestion_ventas(conn):
    while True:
        print("\n--- Gestión de Ventas ---")
        print("1. Ver todas las ventas")
        print("2. Ver una venta específica")
        print("3. Crear nueva venta")
        print("4. Anular venta")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionVentas.listar_ventas(conn)
        elif opcion == '2':
            try:
                venta_id = int(input("Ingrese el ID de la venta a ver: "))
                gestionVentas.ver_venta(conn, venta_id)
            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '3':
            try:
                cliente_id = int(input("Ingrese el ID del cliente para la venta: "))
                destino_id = int(input("Ingrese el ID del destino para la venta: "))
                fecha = datetime.datetime.now()
                monto = float(input("Ingrese el monto de la venta: "))

                gestionVentas.insertar_venta(conn, cliente_id, destino_id, fecha, monto)
                
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para IDs y monto.")
        elif opcion == '4': 
            try:
                venta_id = int(input("Ingrese el ID de la venta a anular: "))
                gestionVentas.anular_venta(conn, venta_id)
            except ValueError:
                print("ID inválido. Por favor, ingrese un número.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# --- Función Principal de la Aplicación ---

def main():
    conn = dbConnection.conectar_db('prog_apb')
    if conn is None:
        print("No se pudo establecer conexión con la base de datos. Saliendo del programa.")
        return

    gestionClientes.crear_tabla_clientes(conn)
    gestionDestinos.crear_tabla_destinos(conn)
    gestionVentas.crear_tabla_ventas(conn)

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Clientes")
        print("2. Gestión de Destinos")
        print("3. Gestión de Ventas")
        print("0. Salir")

        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == '1':
            menu_gestion_clientes(conn)
        elif opcion_principal == '2':
            menu_gestion_destinos(conn)
        elif opcion_principal == '3':
            menu_gestion_ventas(conn)
        elif opcion_principal == '0':
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
    dbConnection.cerrar_conexion(conn)

if __name__ == "__main__":
    main()