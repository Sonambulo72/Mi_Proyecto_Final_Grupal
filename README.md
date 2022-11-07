# mi-proyecto-final-Grupal (Comisión 44065)

Este es el proyecto final de Python para CODERHOUSE

Autores:
  - Jorge Bouza
  - Joshua Roig
  - Jose Luis Esperon

Tabla de contenido
1- Descripción
2- Requerimientos & Funcionamiento
3- Roadmap


1- Descripción
El proyecto radica en el armado de un blog cuyo contenido se realiza mediante un acceso de usuario y password
Por otro lado, el programa utiliza un ABM de personas.

2-  Requerimientos
    Instalacion
    Para la instalacion se requiere:

Revisar la version de python
Este proyecto se realizo usando la version python 3.10.8,por ende ser recomienda usar dicha version o superior.

Para revisar la compatibilidad usar:

c:\> py --version
c:\> Python 3.8.0

Instalacion de las dependencias
Para instalar las dependencias precisas ejecutar pip install, asegurandote que estas en la carpeta raiz. Por favor revisar la carpeta raiz requirements.txt para mas informacion.

> pip install -r requirements.txt

En algunos SO se requiere ejecutar con pip3 en lugar de pip.

Configuracion de la aplicacion DJANGO
Una vez instaladas las dependencias, se debe ejecutar algunos comando en DJANGO.

Migraciones

En windows:

c:\> py mananage.py migrate

Ejecutar en modo de prueba el servidor ( en el archivo setting.py /linea 26/ esta por defecto DEBUG = True)
> python mananage.py runserver
En windows:

c:\> py mananage.py runserver

Para acceder en el navegador agregar

localhost:8000/Blog

Si todo esta correcto se podria acceder a la aplicacion desde el navegador.

3- //Roadmap en definición aun///



