# ProyectoDirectorioMedico

## Para Windows
Crear  entorno virtual en la carpeta ProyectoDirectorioMedico
python -m virtualenv venv

Activar entorno virtual en la misma carpeta
.\venv\Scripts\activate

Ejecutar: pip install -r requirements.txt
Para que trabajemos con las mismas versiones
En caso de instalar una nueva librería, etc, ejecutar: pip freeze > requirements.txt y subir el archivo 
actualizado al repositorio

Para correr el proyecto:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Para Linux
- `make activate`: Para activar el entorno virtual. (Lo crea si no existe)
- `make run`: Para correr el server. Corre `makemigrations` y `migrate` antes de `runserver`.

## Detalles
en localhost:8000/admin se puede ver el panel de administrador

En caso de querer crear una nueva app en el proyecto:
python manage.py startapp nombre_app

La BD de pruebas queda subida para que frontend no tenga q crear nuevos datos desde cero



