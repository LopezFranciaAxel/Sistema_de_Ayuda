# Sistema de Ayuda con archivos HTML (Browser)

## Introducción

El proyecto **Sistema de Ayuda con Archivos HTML** es una aplicación de escritorio que actúa como un sistema de ayuda interactivo. Está diseñado para mostrar contenido HTML de diferentes secciones de ayuda en una interfaz de usuario, permitiendo a los usuarios navegar por distintas páginas y utilizar una barra de búsqueda para encontrar temas específicos. El proyecto se ha creado utilizando Python con el módulo PyQt5, que permite una interfaz gráfica moderna y funcional. Incluye funciones como navegación hacia adelante y atrás, y un icono de búsqueda en la barra de búsqueda.

Este README proporciona una guía paso a paso para la configuración del entorno de desarrollo, la instalación de dependencias, y la generación de un instalador ejecutable con la aplicacion Inno Setup.

---

## Guía de Pasos de Configuración y Ejecución del Proyecto

### Paso 1: Requisitos del Sistema

- **Sistema Operativo**: Windows 10 o superior.
- **Python**: Se recomienda la versión 3.10 para maximizar la compatibilidad con PyQt5 y otras dependencias.
- **Editor de Texto**: Visual Studio Code ( es el recomendado, aunque cualquier editor de texto será suficiente).

### Paso 2: Instalación de Python

1. Visita la [página oficial de Python](https://www.python.org/downloads/).
2. Descarga la versión 3.10 y sigue las instrucciones para instalarla.
3. Durante la instalación, asegúrate de seleccionar la opción **Add Python to PATH**.

### Paso 3: Instalación de Dependencias

Con Python instalado, abre una terminal o la línea de comandos y navega hasta la carpeta de tu proyecto. Despues, ejecuta los siguientes comandos para instalar las dependencias necesarias:

---bash
pip install pyqt5
pip install pyqtwebengine

Estos paquetes proporcionan los módulos PyQt5 y PyQtWebEngine, que se utilizan para la interfaz gráfica y para visualizar contenido HTML en el sistema de ayuda.

Paso 4: Estructura de Archivos del Proyecto
Dentro de la carpeta de tu proyecto, asegúrate de tener la siguiente estructura:

![Uploading image.png…]()



### Paso 5: Configuración de Opciones en config.ini
El archivo config.ini permite activar o desactivar ciertas funciones en la aplicación. Este archivo debe contener configuraciones como:

![image](https://github.com/user-attachments/assets/0ddcdc51-f609-4dc8-ac5d-8079286bd3e9)


### Paso 6: Creación del Ejecutable con PyInstaller
Para generar el ejecutable de main.py, ejecuta el siguiente comando en la terminal:

pyinstaller --onefile --windowed --add-data "html_files;html_files" --add-data "styles.css;." --add-data "config.ini;." --hidden-import=PyQt5.QtWebEngineWidgets main.py

Este comando genera una carpeta dist que contiene el archivo main.exe.

### Paso 7: Creación del Instalador con Inno Setup
1. Descarga e instala Inno Setup.
2. Abre Inno Setup y carga el archivo setup.iss que se encuentra en la carpeta del proyecto.
3. Configura la ruta del ejecutable generado (main.exe) y otros archivos necesarios (como html_files, config.ini, styles.css).
4. Compila el instalador presionando F9. Esto generará el archivo Sistema_de_Ayuda_Installer.exe, que puedes distribuir en otros dispositivos.

![image](https://github.com/user-attachments/assets/dd201f00-192a-4c87-9d40-f32dbad5cec0)


---

### En Conclusion
El proyecto puede ser ejecutado en cualquier dispositivo con Windows sin necesidad de instalar Python, ya que el instalador incluye todas las dependencias necesarias. La aplicación leerá el archivo config.ini cada vez que se ejecute, permitiendo que los usuarios puedan modificar las configuraciones sin necesidad de recompilar el programa.
