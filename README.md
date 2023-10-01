# Proyecto Directorio Médico

 
Desarrollo de aplicación Web para un Directorio Médico basada en Django junto a Robot Framework.
  

## Pre-requisitos 📋

  

- Python 3

  

## Instalación ⚙️

  

- Clonar el repositorio 

- Crear  entorno virtual en la carpeta ProyectoDirectorioMedico

		python -m virtualenv venv

- Activar entorno virtual en la misma carpeta

		.\venv\Scripts\activate
-	Para Linux
	- `make activate`: Para activar el entorno virtual. (Lo crea si no existe)
	- `make run`: Para correr el server. Corre `makemigrations` y `migrate` antes de `runserver`.
- Ejecutar: 
	
		pip install -r requirements.txt

- Para correr el proyecto:

		python manage.py makemigrations

		python manage.py migrate

		python manage.py runserver

- Para ejecutar test:
		
		robot test.robot

## Detalles

Panel administrador

	localhost:8000/admin
## Licencia 🔓

  

MIT LICENCE
