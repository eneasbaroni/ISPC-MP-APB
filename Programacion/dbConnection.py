import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG

def conectar_db(database_name=None):
    """
    Establece una conexión con la base de datos MySQL.
    Si se proporciona un database_name, intenta conectarse a esa base de datos.
    De lo contrario, se conecta al servidor MySQL sin especificar una base de datos.
    """
    conn = None
    try:
        if database_name:
            conn = mysql.connector.connect(
                host=DB_CONFIG['host'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                database=database_name 
            )
        else:
            conn = mysql.connector.connect(
                host=DB_CONFIG['host'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password']
            )

        if conn.is_connected():
            if database_name:
                print(f"Conexión exitosa a la base de datos MySQL: {database_name}.")
            else:
                print("Conexión exitosa al servidor MySQL.")
    except Error as e:
        if e.errno == 1049 and database_name: 
            print(f"La base de datos '{database_name}' no existe.")
            return None
        else:
            print(f"Error al conectar a la base de datos MySQL: {e}")
    return conn

def cerrar_conexion(conn):
    if conn is not None and conn.is_connected():
        conn.close()
        print("Conexión a la base de datos cerrada.")
    else:
        print("No hay conexión a la base de datos para cerrar.")