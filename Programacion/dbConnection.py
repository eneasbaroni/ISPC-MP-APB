import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG


def conectar_db():
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("Conexión exitosa a la base de datos MySQL.")
    except Error as e:
        print(f"Error al conectar a la base de datos MySQL: {e}")
    return conn

def cerrar_conexion(conn):
    if conn is not None and conn.is_connected():
        conn.close()
        print("Conexión a la base de datos cerrada.")
    else:
        print("No hay conexión a la base de datos para cerrar.")