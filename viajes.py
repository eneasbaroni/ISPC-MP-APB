def mostrar_destinos(destinos):
    print("=== Destinos disponibles ===")
    for codigo, datos in destinos.items():
        print(f"{codigo}. {datos['nombre']} - ${datos['precio']} por persona")
    print()

def mostrar_cuotas(cuotas):
    print("=== Opciones de cuotas ===")
    for codigo, datos in cuotas.items():
        print(f"{codigo}. {datos['nombre']} - Interés: {datos['interes']}%")
    print()

def comprar_pasajes(destinos, cuotas):
    while True:
        mostrar_destinos(destinos)
        destino_elegido = input("Elegí el número del destino: ")
        if destino_elegido in destinos:
            break
        print("❌ Opción de destino no válida. Ingrese un destino valido.\n")

    nombre_destino = destinos[destino_elegido]["nombre"]
    precio_unitario = destinos[destino_elegido]["precio"]

    while True:
        cantidad_input = input("¿Cuántos pasajeros? ")
        try:
            cantidad = int(cantidad_input)
            if cantidad > 0:
                break
            else:
                print("❌ La cantidad debe ser mayor a cero.\n")
        except ValueError:
            print("❌ Ingresá un número válido.\n")

    while True:
        mostrar_cuotas(cuotas)
        cuotas_elegidas = input("Elegí una opción de cuotas: ")
        if cuotas_elegidas in cuotas:
            break
        print("❌ Opción de cuotas no válida. Ingrese un valor valido (1, 2, 3, 6 o 12).\n")

    interes = cuotas[cuotas_elegidas]["interes"]
    cantidad_cuotas = int(cuotas_elegidas)
    total_base = precio_unitario * cantidad
    total_con_interes = total_base * (1 + interes / 100)
    valor_por_cuota = total_con_interes / cantidad_cuotas

    print("\n=== 🧾 Resumen de compra ===")
    print(f"Destino: {nombre_destino}")
    print(f"Cantidad de pasajeros: {cantidad}")
    print(f"Total: ${total_con_interes:,.2f}")
    print(f"Cuotas: {cuotas[cuotas_elegidas]['nombre']} de ${valor_por_cuota:,.2f} cada una\n")

    while True:
        print("1. Confirmar compra")
        print("2. Volver al menú principal")
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            print("✅ ¡Compra confirmada! Gracias por viajar con nosotros.\n")
            return
        elif opcion == "2":
            return
        else:
            print("Opción no válida.\n")