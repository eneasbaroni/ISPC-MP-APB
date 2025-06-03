from mysql.connector import Error

def crear_tabla_ventas(conn):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para crear la tabla.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT NOT NULL,
                destino_id INT NOT NULL,
                fecha DATE NOT NULL,
                monto DECIMAL(10, 2) NOT NULL,
                estado VARCHAR(50) DEFAULT 'Activa',
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (destino_id) REFERENCES destinos(id)
            )
        """)
        conn.commit()
        print("Tabla 'ventas' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la tabla 'ventas': {e}")
    finally:
        cursor.close()

def insertar_venta(conn, cliente_id, destino_id, fecha, monto):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para insertar una venta.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO ventas (cliente_id, destino_id, fecha, monto)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, destino_id, fecha, monto))
        conn.commit()
        print(f"Venta registrada correctamente para el cliente ID {cliente_id}.")
    except Error as e:
        if e.errno == 1452:
            print(f"Error al insertar la venta: El ID de cliente ({cliente_id}) o el ID de destino ({destino_id}) no existen.")
            print("Por favor, verifique que los IDs de cliente y destino sean válidos.")
        else:
            print(f"Error al insertar la venta: {e}")
        conn.rollback()
    finally:
        cursor.close()

def listar_ventas(conn):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para listar las ventas.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT v.id, c.razon_social, d.ciudad, d.pais, v.fecha, v.monto, v.estado
            FROM ventas v
            JOIN clientes c ON v.cliente_id = c.id
            JOIN destinos d ON v.destino_id = d.id
        """)
        ventas = cursor.fetchall()
        if not ventas:
            print("No hay ventas registradas en la base de datos.")
        else:
            for venta in ventas:
                print(f"ID: {venta[0]}, Cliente: {venta[1]}, Destino: {venta[2]}, País: {venta[3]}, Fecha: {venta[4]}, Monto: ${venta[5]}, Estado: {venta[6]}")
    except Error as e:
        print(f"Error al listar las ventas: {e}")
    finally:
        cursor.close()

def ver_venta(conn, venta_id):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para ver una venta.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT v.id, c.razon_social, d.ciudad, d.pais, v.fecha, v.monto, v.estado
            FROM ventas v
            JOIN clientes c ON v.cliente_id = c.id
            JOIN destinos d ON v.destino_id = d.id
            WHERE v.id = %s
        """, (venta_id,))
        venta = cursor.fetchone()
        if venta:
            print(f"ID: {venta[0]}, Cliente: {venta[1]}, Destino: {venta[2]}, País: {venta[3]}, Fecha: {venta[4]}, Monto: ${venta[5]}, Estado: {venta[6]}")
        else:
            print(f"No se encontró la venta con ID {venta_id}.")
    except Error as e:
        print(f"Error al ver la venta: {e}")
    finally:
        cursor.close()

def anular_venta(conn, venta_id):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para anular la venta.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT estado FROM ventas WHERE id = %s", (venta_id,))
        venta_actual = cursor.fetchone()

        if venta_actual is None:
            print(f"No se encontró una venta con ID {venta_id}.")
            return
        
        current_status = venta_actual[0]
        if current_status == 'Anulada':
            print(f"La venta con ID {venta_id} ya está anulada.")
            return

        cursor.execute("""
            UPDATE ventas SET estado = 'Anulada' WHERE id = %s
        """, (venta_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Venta con ID {venta_id} anulada correctamente.")
        else:
            print(f"No se pudo anular la venta con ID {venta_id}. Posiblemente no existía o ya estaba anulada.")
    except Error as e:
        print(f"Error al anular la venta: {e}")
    finally:
        cursor.close()