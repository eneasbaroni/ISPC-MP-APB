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
    usuarios.append({"email": email, "password": password})
    print("✅ Usuario creado exitosamente.\n")

def loguearse(usuarios):
    print("\n=== Iniciar sesión ===")

    if not usuarios:
        print("⚠️ No hay usuarios registrados. Creá una cuenta primero.\n")
        return

    while True:
        email = input("Email: ").strip().lower()
        password = input("Contraseña: ").strip()

        usuario_encontrado = next((u for u in usuarios if u["email"] == email), None)

        if not usuario_encontrado:
            print("❌ No se encontró un usuario con ese email. Intentá de nuevo.\n")
            continue

        if usuario_encontrado["password"] != password:
            print("❌ Contraseña incorrecta. Intentá de nuevo.\n")
            continue

        print(f"✅ Bienvenido/a, {email}.\n")
        break