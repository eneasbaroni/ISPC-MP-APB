usuarios = []

def crear_usuario(usuarios):
    print("\n=== Crear usuario ===")

    while True:
        email = input("Ingresá tu email: ").strip().lower()

        if not email:
            print("❌ El email no puede estar vacío.\n")
            continue

        if any(usuario["email"] == email for usuario in usuarios):
            print("❌ Ya existe un usuario registrado con ese email. Probá con otro.\n")
            continue

        break 

    while True:
        password = input("Ingresá una contraseña: ").strip()

        if not password:
            print("❌ La contraseña no puede estar vacía.\n")
            continue

        break

    # Registro exitoso
    usuarios.append({"email": email, "password": password,  "viajes": []})
    print("✅ Usuario creado exitosamente.\n")

def loguearse(usuarios):
    print("\n=== Iniciar sesión ===")

    while True:
        email = input("Email: ").strip().lower()
        password = input("Contraseña: ").strip()

        usuario_encontrado = next((u for u in usuarios if u["email"] == email), None)

        if not usuario_encontrado:
            print("❌ El usuario o contrseña no son correctos. Intentá de nuevo.\n")
        elif usuario_encontrado["password"] != password:
            print("❌ El usuario o contrseña no son correctos. Intentá de nuevo.\n")
        else:
            print(f"✅ Bienvenido/a, {email}.\n")
            return usuario_encontrado
        while True:
            opcion = input("1. Volver a intentar\n2. Volver al menú principal\nElegí una opción: ")
            if opcion == "1":
                break  # Volver al inicio del bucle de logueo
            elif opcion == "2":
                return None # Volver al menú principal sin loguearse
            else:
                print("Opción no válida. Intentá de nuevo.\n")
    

    
def registrar_compra_usuario(usuario_email, detalle_compra):
    for usuario in usuarios:
        if usuario["email"] == usuario_email:
            usuario["viajes"].append(detalle_compra)
            print(f"✈️ Viaje registrado para el usuario {usuario_email}.\n")
            return
    print(f"⚠️ No se encontró el usuario {usuario_email} para registrar la compra.\n")

def ver_pasajes(usuario_email, mostrar_opciones=True):
    print("\n=== Tus Pasajes Adquiridos ===")
    if not usuario_email:
        print("⚠️ Debes iniciar sesión para ver tus pasajes.\n")
        return

    usuario_encontrado = next((u for u in usuarios if u["email"] == usuario_email), None)

    if not usuario_encontrado:
        print(f"⚠️ No se encontró el usuario {usuario_email}.\n")
        return

    if not usuario_encontrado["viajes"]:
        print("No has adquirido ningún pasaje aún.\n")
        return

    for indice, viaje in enumerate(usuario_encontrado["viajes"]):
        print(f"{indice + 1}. ID: {viaje.get('id', 'N/A')}")
        print(f"   Fecha de Compra: {viaje.get('fecha_compra', 'N/A')}")
        print(f"   Destino: {viaje.get('destino', 'N/A')}")
        print(f"   Cantidad de Pasajeros: {viaje.get('cantidad_pasajeros', 'N/A')}")
        print(f"   Total: ${viaje.get('total', 'N/A'):,.2f}")
        print(f"   Cuotas: {viaje.get('cuotas', 'N/A')}")
        print(f"   Valor por Cuota: ${viaje.get('valor_por_cuota', 'N/A'):,.2f}")
        print(f"   Estado: {viaje.get('estado', 'N/A')}\n")

    return usuario_encontrado["viajes"]

def anular_pasaje_usuario(usuario_email, lista_pasajes):
    if not lista_pasajes:
        print("No hay pasajes para anular.\n")
        return

    while True:
        try:
            indice_arrepentimiento_str = input("Ingrese el número del pasaje que desea anular (0 para volver): ")
            indice_arrepentimiento = int(indice_arrepentimiento_str)
            if indice_arrepentimiento == 0:
                return
            elif 1 <= indice_arrepentimiento <= len(lista_pasajes):
                indice_seleccionado = indice_arrepentimiento - 1
                usuario_encontrado = next((u for u in usuarios if u["email"] == usuario_email), None)
                if usuario_encontrado:
                    if 0 <= indice_seleccionado < len(usuario_encontrado["viajes"]):
                        usuario_encontrado["viajes"][indice_seleccionado]["estado"] = "Anulado"
                        print(f"✅ El pasaje con ID {usuario_encontrado['viajes'][indice_seleccionado].get('id', 'N/A')} ha sido anulado.\n")
                        return # Volvemos al menú de ver pasajes
                    else:
                        print("Número de pasaje inválido.\n")
                else:
                    print("Usuario no encontrado.\n")
            else:
                print("Número de pasaje inválido.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")