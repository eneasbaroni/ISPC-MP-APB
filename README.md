# ✈️ Agencia de Viajes SkyRoute - Aplicación en Consola

Este proyecto es una aplicación interactiva de consola que simula una agencia de viajes. Permite a los usuarios registrarse, iniciar sesión, ver destinos disponibles y comprar pasajes en cuotas.

## 👥 Integrantes

-   Baroni Eneas
-   Dalmau Vallejos Natalia
-   Ipolito Ignacio Nahuel
-   Medrano Facundo
-   Paez Jorge Maximiliano
-   Sáez Mauro

## 🚀 Características

-   Menú interactivo en consola
-   Registro, inicio de sesión de usuarios y cierre de sesión (LogOut)
-   Visualización de destinos con precios
-   Simulación de compra de pasajes:
    -   Elección de destino
    -   Cantidad de pasajeros
    -   Selección de cuotas con interés
    -   Resumen final de compra
    -   Confirmación y cancelación de compra
-   Visualización de los pasajes adquiridos por el usuario logueado
-   Opción para anular pasajes adquiridos (Botón de arrepentimiento)
-   Manejo de errores y validaciones básicas (campos no vacíos, formato numérico)
-   Mensajes informativos claros para el usuario

## 🔧 Funcionalidades futuras

-   Guardado de usuarios y compras en archivos
-   Validación de email con formato correcto
-   Historial de compras
-   Ver Perfil
-   Compra con selección de fechas
-   Menu administrador
    -   Cargar Destinos
    -   Ver Clientes
    -   Ver ventas

## ▶️ Cómo ejecutar

-   Clonar el repositorio:

```bash
git clone https://github.com/eneasbaroni/ISPC-MP-APB.git
cd ISPC-MP-APB
cd Programacion
```

-   Asegurate de tener Python 3 instalado. Para ejecutar la aplicación:

```bash
python3 main.py
```

## 🗺️ Mapa de Uso

A continuación, se describen los pasos para utilizar las funcionalidades implementadas en la aplicación SkyRoute:

1.  **Ejecutar la aplicación:**

    -   Sigue las instrucciones en la sección "▶️ Cómo ejecutar" para iniciar la aplicación en tu consola.
    -   Verás el **Menú Principal** con las opciones disponibles.

2.  **Crear un usuario:**

    -   En el **Menú Principal**, elige la opción `1. Perfil`.
    -   Dentro del submenú de Perfil, elige la opción `1. Crear usuario`.
    -   Se te pedirá que ingreses un **email** y una **contraseña** para crear tu cuenta. Sigue las instrucciones en pantalla.
    -   Volver al menú principal.

3.  **Iniciar sesión:**

    -   En el **Menú Principal**, elige la opción `1. Perfil`.
    -   Dentro del submenú de Perfil, elige la opción `2. Loguearse`.
    -   Se te pedirá que ingreses tu **email** y **contraseña** registrados.
    -   Si las credenciales son correctas, serás logueado y volverás al **Menú Principal**.

4.  **Ver los destinos disponibles:**

    -   En el **Menú Principal**, elige la opción `2. Destinos`.
    -   Dentro del submenú de Destinos, elige la opción `1. Ver destinos`.
    -   Se mostrará una lista de los destinos disponibles con sus respectivos precios.
    -   Desdea allí podrás **volver al menú principal** o **salir**.

5.  **Comprar pasajes (debes estar logueado):**

    -   En el **Menú Principal**, elige la opción `2. Destinos`.
    -   Dentro del submenú de Destinos, elige la opción `2. Comprar pasajes`.
    -   Se mostrará la lista de destinos. Ingresa el **número del destino** que deseas comprar.
    -   Ingresa la **cantidad de pasajeros**.
    -   Se mostrarán las opciones de **cuotas con interés**. Elige una opción ingresando su número.
    -   Se mostrará un **resumen de tu compra**.
    -   Se te preguntará si deseas **confirmar la compra** o **volver al menú principal**.

6.  **Ver tus pasajes adquiridos (debes estar logueado):**

    -   En el **Menú Principal**, elige la opción `1. Perfil`.
    -   Dentro del submenú de Perfil, elige la opción `4. Ver Pasajes`.
    -   Se mostrará una lista de los pasajes que has comprado.
    -   Luego, tendrás opciones para **volver al menú principal**, **salir**, o **arrepentirte de una compra**.

7.  **Arrepentirse de una compra (debes estar logueado y haber visto tus pasajes):**

    -   Sigue los pasos 6 para ver tus pasajes.
    -   En el menú de opciones de pasajes, elige la opción `3. Arrepentimiento de compra`.
    -   Se te pedirá que ingreses el **número del pasaje** que deseas anular. Sigue las instrucciones.

8.  **Cerrar sesión (LogOut):**

    -   En el **Menú Principal**, elige la opción `1. Perfil`.
    -   Dentro del submenú de Perfil, elige la opción `5. LogOut`.
    -   Se cerrará tu sesión y volverás al **Menú Principal**.

9.  **Salir de la aplicación:**
    -   En el **Menú Principal**, elige la opción `0. Salir`.
    -   La aplicación se cerrará.
