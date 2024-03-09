# ego-challenge

[Read in English](README_ES.md)



## Como lanzar el proyecto

### 1. Dependencias

Necesitas un entorno de Python con `Django 5.0.3`, `Django REST Framework 3.14` y `Pillow 10.2` instalados.
Yo utilizo `pipenv`, una herramienta que se encarga de esto.

Si tienes `pipenv` instalado (solo disponible en Linux) ejecuta los siguientes comando en la carpeta del repositorio:

> \$ `pipenv update`\
> \$ `pipenv shell`

Esto creará el entorno virtual e instalará las depencencias necesarias.

Si no quieres (o puedes) user `pipenv`, el archivo `requirements.txt` debería ayudarte a lanzar el proyecto utilizando otra herramienta.

### 2. Lanzar el proyecto

Una vez instaladas las depencencias lanza el proyecto usando:

> \$ `python ./project/manage.py runserver`

Luego abre tu navegador y ve a: http://localhost:8080/



## Información

### Modelo "vehicle"
![Database design](./doc/vehicleDB.png)

### Root / Admin
La url raíz redirije al panel de administración para realizar cambios en los datos<br>
http://localhost:8080/ -> http://localhost:8080/admin/

### API List View
http://localhost:8080/api/vehicle/

### API Vehicle Details
http://localhost:8080/api/vehicle/12/ <br>
(12 es el único vehiculo que tiene datos en el campo "vehiclesite")

### Detalles
"Autos" <br>
http://192.168.1.8:8080/api/vehicle/?filter=autos

"Pickups y comerciales" <br>
http://192.168.1.8:8080/api/vehicle/?filter=pickups,comerciales

"SUVs y Crossovers" <br>
http://192.168.1.8:8080/api/vehicle/?filter=suvs,crossovers

### Orden
De menor a mayor precio <br>
http://192.168.1.8:8080/api/vehicle/?order=price

De mayor a menor precio <br>
http://192.168.1.8:8080/api/vehicle/?order=price&reverse

Más nuevos primero <br>
http://192.168.1.8:8080/api/vehicle/?order=year

Más antiguos primero <br>
http://192.168.1.8:8080/api/vehicle/?order=year&reverse



## Mi entorno de desarrollo

- Python Virtual Env.: `pipenv`
- Python Dependencies: `pipenv`
- Editor: `Visual Studio Code`
- O.S.: `Manjaro Linux (arch)`



## Detalles

Para este desafío estructuré las cosas de una manera diferente a la que lo haría normalmente, ya que los objetivos son específicos y aislados, lo que quita la necesidad de tener en cuenta la seguridad y escalabilidad del proyecto. Sin embargo me parece interesante mencionar estas cosas:
- No hay una configuración estructurada, tampoco tuve en cuenta los detalles necesarios para trabajar en producción.
- El diseño de los modelos (la base de datos) es simple para cumplir con la consigna.
- No se escribió código de testeo, simplemente se testeó "a mano".
