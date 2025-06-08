Proyecto SkyRoute - Base de Datos SQL
Descripción
Este proyecto contiene el script SQL para la creación y gestión de la base de datos prog_apb, diseñada para la agencia de viajes SkyRoute. Incluye las tablas clientes, destinos y ventas, además de ejemplos de consultas útiles para explorar y analizar la información registrada.

Instrucciones
Por favor, consultá el archivo PDF incluido para seguir paso a paso la creación de la base de datos, inserción de datos de prueba y ejecución de consultas SQL.
El documento explica conceptos clave como claves primarias y foráneas, y ofrece ejemplos prácticos comentados.

Archivos incluidos
prog_apb.sql — Script completo para crear la base de datos, insertar datos de prueba y ejecutar consultas.

SQL SkyRoute Creación de BD.pdf — Guía explicativa paso a paso con introducción, estructura y ejemplos comentados.

Estructura del proyecto
Tablas incluidas:
clientes: Información de los clientes (razón social, CUIT, email).

destinos: Ciudades disponibles para viajar, país y costo base del pasaje.

ventas: Registro de ventas con fechas, montos, estado y relaciones con clientes y destinos.

Consultas de ejemplo:
Listar todos los clientes.

Ventas realizadas en una fecha específica.

Última venta por cliente.

Destinos cuya ciudad comienza con “S”.

Cantidad de ventas por país.

Total recaudado por cliente (solo ventas activas).

Requisitos
Tener instalado un sistema de gestión de bases de datos compatible con SQL (como MySQL o MariaDB).

Capacidad para ejecutar scripts SQL desde terminal o interfaz gráfica (ej. MySQL Workbench).

Conocimientos básicos de SQL.


Contacto
Si tenés dudas o problemas con la implementación del sistema, no dudes en contactarme para ayudarte.

¡Gracias por usar SkyRoute y ser parte del viaje!
