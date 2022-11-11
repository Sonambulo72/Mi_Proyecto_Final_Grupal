# mi-proyecto-final-Grupal (Comisión 44065)

Este es el proyecto final de Python para CODERHOUSE
Autores:
  - Jorge Bouza
  - Joshua Roig
  - José Luis Esperón

Tabla de contenido
1- Descripción
2- Requerimientos & Funcionamiento
3- Roadmap


1- Descripción
El proyecto radica en el armado de un blog cuyo contenido se realiza mediante un acceso de usuario y password
Por otro lado, el programa utiliza un ABM de personas.

2- Requerimientos
    Instalación
    Para la instalación se requiere:

Revisar la versión de python
Este proyecto se realizo usando la versión python 3.10.8,por ende ser recomienda usar dicha versión o superior.

Para revisar la compatibilidad usar:

c:\> py --version
c:\> Python 3.8.0

instalación de las dependencias
Para instalar las dependencias precisas ejecutar pip install, asegurándote que estas en la carpeta raiz. Por favor revisar la carpeta raíz requirements.txt para más información.

> pip install -r requirements.txt
> pip install Pillow
> pip install whitenoise
> pip install django-crispy-forms

En algunos SO se requiere ejecutar con pip3 en lugar de pip.

Configuración de la aplicación DJANGO
Una vez instaladas las dependencias, se debe ejecutar algunos comandos en DJANGO.

Migraciones

En windows:

c:\> py mananage.py migrate

Ejecutar en modo de prueba el servidor ( en el archivo setting.py /linea 26/ esta por defecto DEBUG = True)
> python mananage.py runserver
En windows:

c:\> py mananage.py runserver

Para acceder en el navegador agregar

localhost:8000/Blog

Si todo esta correcto se podrá acceder a la aplicación desde el navegador.

3- //Roadmap en definición aun///

Se continua trabajando en este punto. 
