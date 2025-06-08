from mysql.connector import Error

def crear_tabla_clientes(conn):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para crear la tabla.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                razon_social VARCHAR(100) NOT NULL,
                CUIT VARCHAR(100) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE
            )
        """)
        conn.commit()
        print("Tabla 'clientes' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la tabla 'clientes': {e}")
    finally:
        cursor.close()

def insertar_cliente(conn, razon_social, CUIT, email):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para insertar un cliente.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clientes (razon_social, CUIT, email)
            VALUES (%s, %s, %s)
        """, (razon_social, CUIT, email))
        conn.commit()
        print(f"Cliente {razon_social} insertado correctamente.")
    except Error as e:
        print(f"Error al insertar el cliente: {e}")
    finally:
        cursor.close()

def eliminar_cliente(conn, cliente_id):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para eliminar un cliente.")
        return False 
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM ventas WHERE cliente_id = %s", (cliente_id,))
        if cursor.fetchone()[0] > 0:
            print(f"Error: No se puede eliminar el cliente con ID {cliente_id} porque tiene ventas asociadas.")
            print("Por favor, anule o elimine las ventas relacionadas primero.")
            return False 

        cursor.execute("""
            DELETE FROM clientes WHERE id = %s
        """, (cliente_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Cliente con ID {cliente_id} eliminado correctamente.")
            return True 
        else:
            print(f"No se encontró un cliente con ID {cliente_id} para eliminar.")
            return False 
    except Error as e:
        print(f"Error al eliminar el cliente: {e}")
        conn.rollback()
        return False 
    finally:
        cursor.close()

def listar_clientes(conn):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para listar los clientes.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        if not clientes:
            print("No hay clientes registrados en la base de datos.")
        else:
            for cliente in clientes:
                print(cliente)
    except Error as e:
        print(f"Error al listar los clientes: {e}")
    finally:
        cursor.close()

def ver_cliente(conn, cliente_id):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para ver un cliente.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
        cliente = cursor.fetchone()
        if cliente:
            print(cliente)
        else:
            print(f"No se encontró el cliente con ID {cliente_id}.")
    except Error as e:
        print(f"Error al ver el cliente: {e}")
    finally:
        cursor.close()

def editar_cliente(conn, cliente_id, razon_social=None, CUIT=None, email=None):
    if conn is None or not conn.is_connected():
        print("No hay conexión a la base de datos para editar un cliente.")
        return False 
    cursor = conn.cursor()
    try:
        updates = []
        params = []
        if razon_social:
            updates.append("razon_social = %s")
            params.append(razon_social)
        if CUIT:
            updates.append("CUIT = %s")
            params.append(CUIT)
        if email:
            updates.append("email = %s")
            params.append(email)

        if updates:
            params.append(cliente_id)
            cursor.execute(f"""
                UPDATE clientes SET {', '.join(updates)} WHERE id = %s
            """, tuple(params))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Cliente con ID {cliente_id} actualizado correctamente.")
                return True 
            else:
                print(f"No se encontró un cliente con ID {cliente_id} para actualizar.")
                return False 
        else:
            print("No se proporcionaron datos para actualizar.")
            return False 
    except Error as e:
        print(f"Error al editar el cliente: {e}")
        conn.rollback() 
        return False 
    finally:
        cursor.close()