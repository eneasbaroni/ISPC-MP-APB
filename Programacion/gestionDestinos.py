from mysql.connector import Error

def crear_tabla_destinos(conn):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para crear la tabla.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS destinos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ciudad VARCHAR(100) NOT NULL,
                pais VARCHAR(255) NOT NULL,
                costo_base DECIMAL(10, 2) NOT NULL
            )
        """)
        conn.commit()
        print("Tabla 'destinos' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la tabla 'destinos': {e}")
    finally:
        cursor.close()

def insertar_destino(conn, ciudad, pais, costo_base):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para insertar un destino.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO destinos (ciudad, pais, costo_base)
            VALUES (%s, %s, %s)
        """, (ciudad, pais, costo_base))
        conn.commit()
        print(f"Destino {ciudad}, {pais} insertado correctamente.")
    except Error as e:
        print(f"Error al insertar el destino: {e}")
    finally:
        cursor.close()

def eliminar_destino(conn, destino_id):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para eliminar un destino.")
        return False 

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM ventas WHERE destino_id = %s", (destino_id,))
        if cursor.fetchone()[0] > 0:
            print(f"Error: No se puede eliminar el destino con ID {destino_id} porque tiene ventas asociadas.")
            print("Por favor, anule o elimine las ventas relacionadas primero.")
            return False 


        cursor.execute("""
            DELETE FROM destinos WHERE id = %s
        """, (destino_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Destino con ID {destino_id} eliminado correctamente.")
            return True 
        else:
            print(f"No se encontró un destino con ID {destino_id} para eliminar.")
            return False 
    except Error as e:
        print(f"Error al eliminar el destino: {e}")
        conn.rollback() 
        return False 
    finally:
        cursor.close()

def editar_destino(conn, destino_id, ciudad=None, pais=None, costo_base=None):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para editar un destino.")
        return False
    cursor = conn.cursor()
    try:
        updates = []
        params = []
        if ciudad:
            updates.append("ciudad = %s")
            params.append(ciudad)
        if pais:
            updates.append("pais = %s")
            params.append(pais)
        if costo_base is not None:
            updates.append("costo_base = %s")
            params.append(costo_base)

        if updates:
            params.append(destino_id)
            cursor.execute(f"""
                UPDATE destinos SET {', '.join(updates)} WHERE id = %s
            """, tuple(params))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Destino con ID {destino_id} actualizado correctamente.")
                return True 
            else:
                print(f"No se encontró un destino con ID {destino_id} para actualizar.")
                return False 
        else:
            print("No se proporcionaron datos para actualizar.")
            return False 
    except Error as e:
        print(f"Error al editar el destino: {e}")
        conn.rollback()
        return False 
    finally:
        cursor.close()

def listar_destinos(conn):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para listar los destinos.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM destinos")
        destinos = cursor.fetchall()
        if not destinos:
            print("No hay destinos registrados en la base de datos.")
        else:
            for destino in destinos:
                print(f"ID: {destino[0]}, Ciudad: {destino[1]}, País: {destino[2]}, Costo Base: ${destino[3]}")
    except Error as e:
        print(f"Error al listar los destinos: {e}")
    finally:
        cursor.close()

def ver_destino(conn, destino_id):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para ver un destino.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM destinos WHERE id = %s", (destino_id,))
        destino = cursor.fetchone()
        if destino:
            print(f"ID: {destino[0]}, Ciudad: {destino[1]}, País: {destino[2]}, Costo Base: ${destino[3]}")
        else:
            print(f"No se encontró el destino con ID {destino_id}.")
    except Error as e:
        print(f"Error al ver el destino: {e}")
    finally:
        cursor.close()