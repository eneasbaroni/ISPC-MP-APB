# ✈️ Agencia de Viajes SkyRoute - Aplicación en Consola

Este proyecto es una aplicación interactiva de consola que simula una herramienta interna para una agencia de viajes. Permite a los usuarios gestionar clientes, destinos y ventas.
En la Carpeta Proyectos se encuentra lo solicitado para la meteria Introducción a la Programación.
En la Base de Datos se encuentra lo solicitado para la meteria Base de Datos.
En la Carpeta Ética se encuentra lo solicitado para la meteria Ética y deontología.

Link del video: https://drive.google.com/drive/folders/19i1BIkdJMxlvVkTSMpjWf_U1QocCUKs3?usp=sharing

## 👥 Integrantes

-   Baroni Eneas
-   Dalmau Vallejos Natalia
-   Ipolito Ignacio Nahuel
-   Medrano Facundo
-   Paez Jorge Maximiliano
-   Sáez Mauro

## 🚀 Características

-   Menú interactivo en consola
-   Gestión de Clientes (CRUD): Permite listar, ver detalles, crear, editar y eliminar información de clientes.
-   Gestión de Destinos (CRUD): Permite listar, ver detalles, crear, editar y eliminar información de destinos de viaje.
-   Gestión de Ventas:
    -   Registro de nuevas ventas asociadas a clientes y destinos existentes.
    -   Visualización de todas las ventas registradas.
    -   Consulta de detalles de una venta específica.
    -   Anulación de ventas: Con una ventana de "arrepentimiento" de 60 días (2 minutos) desde el momento de la venta

## 🔧 Funcionalidades futuras

-   Ver Perfil
-   Compra con selección de fechas

## ▶️ Cómo preparar y ejecutar la Aplicación

1.  **Requisitos Previos:**
    -   Python 3: Es necesario tener Python 3 instalado en el sistema.
    -   MySQL Server: Es necesario tener un servidor MySQL en ejecución.
    -   Librerías de Python: Es necesario tener instalado el conector de MySQL para Python:

```bash
pip install mysql-connector-python
```

2.  **Clonar el repositorio:**

```bash
git clone https://github.com/eneasbaroni/ISPC-MP-APB.git
cd ISPC-MP-APB
cd Programacion
```

3.  **Configuración de la Base de Datos:**
    -   El proyecto espera una base de datos MySQL con la configuración definida en config.py. Por defecto, está configurado para:

```bash
# config.py
DB_CONFIG = {
    'host': 'localhost',
    'database': 'prog_apb',
    'user': 'root',
    'password': 'root'
}
```

    -   Es necesario asegurarse de que los valores de user y password coincidan con las credenciales locales de MySQL.

4.  **Inicializar la Base de Datos (Crear DB y Tablas):**

-   La primera vez que se ejecuta la aplicación, o si es necesario resetear la base de datos, se debe ejecutar el script populate.py. Este script se encarga de:

    -   Crear la base de datos (prog_apb por defecto) si no existe.
    -   Crear las tablas clientes, destinos y ventas.
    -   Insertar algunos datos de ejemplo (clientes y destinos) para poder probar la aplicación inmediatamente.
    -   Verás mensajes en la consola indicando la creación de la base de datos, las tablas y la inserción de los datos.

```bash
# Desde la raíz del proyecto, donde se encuentra populate.py
python populate.py
```

5.  **Ejecutar la Aplicación Principal:**

-   Una vez que la base de datos esté preparada, se puede iniciar la aplicación principal:

```bash
# Desde la raíz del proyecto, donde se encuentra main.py
python main.py
```

## 🗺️ Mapa de Uso

A continuación, se describen los pasos para utilizar las funcionalidades implementadas en la aplicación SkyRoute:

-   Seguir las instrucciones en la sección "▶️ Cómo preparar y ejecutar la Aplicación" para iniciar la aplicación en consola.
-   Se verá el **Menú Principal** con las opciones disponibles.

```bash
=== MENÚ PRINCIPAL ===
1. Gestión de Clientes
2. Gestión de Destinos
3. Gestión de Ventas
0. Salir
```

1.  **Gestión de Clientes:**

-   Este menú permite administrar la información de los clientes:

```bash
=== MENÚ PRINCIPAL ===
1. Gestión de Clientes
2. Gestión de Destinos
3. Gestión de Ventas
0. Salir
```

-   Crear nuevo cliente: Se solicitará la Razón Social, CUIT y Email. Ambos CUIT y Email deben ser únicos.
-   Editar cliente existente: Se solicitará el ID del cliente y luego se podrá dejar en blanco los campos que no deseas modificar.
-   Eliminar cliente: Se solicitará el ID del cliente. Un cliente no puede ser eliminado si tiene ventas asociadas. Se Deberán anular o eliminar las ventas relacionadas primero.

2.  **Gestión de Destinos:**

-   Este menú te permite administrar los destinos de viaje disponibles:

```bash
--- Gestión de Destinos ---
1. Ver todos los destinos
2. Ver un destino específico
3. Crear nuevo destino
4. Editar destino existente
5. Eliminar destino
0. Volver al menú principal
```

-   Ver todos los destinos: Mostrará el listado de destinos disponibles en la BD.
-   Ver un destino específico: Mostrara la informacion de un destino en particular segun el id ingresado.
-   Crear nuevo destino: Se pedirá Ciudad, País y Costo Base.
-   Editar destino existente: Se pedirá el ID del destino y luego se podrá dejar en blanco los campos que no deseas modificar. El Costo Base puede ser un número decimal.
-   Eliminar destino: Se pedirá el ID del destino. Un destino no puede ser eliminado si tiene ventas asociadas. Se Deberásdeberá anular o eliminar las ventas relacionadas primero.

3.  **Gestión de Ventas:**

-   Este menú permite gestionar las ventas de pasajes:

```bash
--- Gestión de Ventas ---
1. Ver todas las ventas
2. Ver una venta específica
3. Crear nueva venta
4. Anular venta
0. Volver al menú principal
```

-   Ver todos las ventas: Mostrará el listado de ventas disponibles en la BD.
-   Ver una venta específica: Mostrara la informacion de una venta en particular segun el id ingresado.
-   Crear nueva venta:
    -   Se pedirá el ID del cliente y el ID del destino, es necesario que existan en la base de datos.
    -   La fecha y hora de la venta se registran automáticamente al momento de la creación.
    -   Se Deberá ingresar el monto de la venta.
-   Anular venta:
    -   Se pedirá el ID de la venta a anular.
    -   Importante: Solo se puede anular una venta si no han transcurrido más de 2 minutos desde su registro. Si se excede este tiempo, la anulación será denegada.
    -   Si la venta ya está anulada, se informará.
