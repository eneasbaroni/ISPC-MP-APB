# populate.py
import dbConnection
import gestionClientes
import gestionDestinos
import gestionVentas
from mysql.connector import Error 

def create_database_if_not_exists(conn, db_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Base de datos '{db_name}' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la base de datos '{db_name}': {e}")
        return False
    finally:
        cursor.close()
    return True


def populate_database():
    db_name = dbConnection.DB_CONFIG['database']

    conn_server = dbConnection.conectar_db()
    if conn_server is None:
        print("No se pudo conectar al servidor MySQL. Saliendo.")
        return

    if not create_database_if_not_exists(conn_server, db_name):
        dbConnection.cerrar_conexion(conn_server)
        print("No se pudo asegurar la existencia de la base de datos. Saliendo.")
        return

    dbConnection.cerrar_conexion(conn_server) 
    
    conn = dbConnection.conectar_db(database_name=db_name)

    if conn is None:
        print("No se pudo conectar a la base de datos para la población inicial.")
        return

    try:
        print("\n--- Creando tablas ---")
        gestionClientes.crear_tabla_clientes(conn)
        gestionDestinos.crear_tabla_destinos(conn)
        gestionVentas.crear_tabla_ventas(conn) 

        print("\n--- Insertando clientes de ejemplo ---")
        gestionClientes.insertar_cliente(conn, "Jorge Perez", "20-12345678-9", "jperez@gmail.com")
        gestionClientes.insertar_cliente(conn, "Juan Lopez", "27-87654321-3", "juan.lopex@gmail.com")
        gestionClientes.insertar_cliente(conn, "Raul Torres", "30-98765432-1", "rtorres@gmail.com")
        gestionClientes.insertar_cliente(conn, "María García", "23-11223344-5", "maria.g@gmail.com")

        print("\n--- Insertando destinos de ejemplo ---")
        gestionDestinos.insertar_destino(conn, "París", "Francia", 1200.50)
        gestionDestinos.insertar_destino(conn, "Tokio", "Japón", 1850.00)
        gestionDestinos.insertar_destino(conn, "Río de Janeiro", "Brasil", 750.25)
        gestionDestinos.insertar_destino(conn, "Nueva York", "Estados Unidos", 1500.75)
        gestionDestinos.insertar_destino(conn, "Buenos Aires", "Argentina", 400.00)

        print("\nBase de datos populada exitosamente.")

    except Exception as e:
        print(f"Ocurrió un error durante la población de la base de datos: {e}")
    finally:
        dbConnection.cerrar_conexion(conn)

if __name__ == "__main__":
    populate_database()