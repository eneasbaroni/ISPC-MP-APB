import uuid
from datetime import datetime
from usuarios import registrar_compra_usuario

def generar_id_unico():
    return str(uuid.uuid4())

def mostrar_destinos(destinos):
    print("=== Destinos disponibles ===")
    for codigo, datos in destinos.items():
        print(f"{codigo}. {datos['ciudad']}, {datos['pais']} - ${datos['precio']} por persona")
    print()

def mostrar_cuotas(cuotas):
    print("=== Opciones de cuotas ===")
    for codigo, datos in cuotas.items():
        print(f"{codigo}. {datos['nombre']} - Interés: {datos['interes']}%")
    print()

def comprar_pasajes(destinos, cuotas, usuario_logueado=None):
    while True:
        mostrar_destinos(destinos)
        destino_elegido = input("Elegí el número del destino: ")
        if destino_elegido in destinos:
            break
        print("❌ Opción de destino no válida. Ingrese un destino valido.\n")

    ciudad_destino = destinos[destino_elegido]["ciudad"]
    pais_destino = destinos[destino_elegido]["pais"]
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

    compra_id = generar_id_unico()
    fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    estado = "Activo"

    detalle_compra = {
        "id": compra_id,
        "fecha_compra": fecha_compra,
        "estado": estado,
        "destino": f"{ciudad_destino}, {pais_destino}",
        "cantidad_pasajeros": cantidad,
        "total": total_con_interes,
        "cuotas": cuotas[cuotas_elegidas]['nombre'],
        "valor_por_cuota": valor_por_cuota
    }

    print("\n=== 🧾 Resumen de compra ===")
    print(f"ID de compra: {detalle_compra['id']}")
    print(f"Fecha de compra: {detalle_compra['fecha_compra']}")
    print(f"Destino: {detalle_compra['destino']}")
    print(f"Cantidad de pasajeros: {detalle_compra['cantidad_pasajeros']}")
    print(f"Total: ${detalle_compra['total']:,.2f}")
    print(f"Cuotas: {detalle_compra['cuotas']} de ${detalle_compra['valor_por_cuota']:,.2f} cada una\n")

    while True:
        print("1. Confirmar compra")
        print("2. Volver al menú principal")
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            print("✅ ¡Compra confirmada! Gracias por viajar con nosotros.\n")
            registrar_compra_usuario(usuario_logueado, detalle_compra)
            return
        elif opcion == "2":
            return
        else:
            print("Opción no válida.\n")