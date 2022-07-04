# Proyecto_Final_Roldan

Mi nombre es Javier Roldan y este es mi proyecto final de Python y Django. 
El proyecto final lo hice solo desde cero.
Disculpen si los estilos de las paginas no son llamativos.

Link al video con la pagina funcionando:
-link-

Para utilizar los templates, crear o usar la carpeta en la ruta "C:\Proyecto_Final\-la carpeta del proyecto-"}

el superusuario es:
user: javier 
password: adminadmin

http://127.0.0.1:8000/home/ --> la ruta del menu de inicio del programa

* Desde el "home" se puede acceder al:
	- "about" donde se encuentra la información sobre mi
	- "register" donde se registran los usuarios
	- "login" donde se inicia sesion con el usuario creado

* Una vez iniciado sesion se redirecciona al inicio

* Desde "inicio" se puede acceder al:
	- "logout" donde se cierra sesion y te redirecciona al login
	- "blogs" donde se presenta una plantilla con los blogs
	- "editar profile" donde se puede editar el perfil del usuario

* Desde "blogs" se puede:
	- crear un blog nuevo con un formulario (pulsar "Agregar Blog")
	- borrar un blog (pulsar "BORRAR")
	- editar un blog con un formulario (pulsar "EDITAR")
	- "leer mas" se accede a un template en la ruta /pages/<id_blog>.
	- "logout" donde se cierra sesion y te redirecciona al login
