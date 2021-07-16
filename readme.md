# Registros Biologicos

### Prerequisites

Se necesita tener instalado:

```
Python (preferiblemente la version 2.2)
```

### Instalacion

Para la instalacion utilizaremos pip

```
pip install -r requirements.txt
```

Realizamos las migraciones para crear las tablas en la base de datos 
```
python manage.py makemigrations
python manage.py migrate

```
Creamos el super Usuario de la plataforma
```
python manage.py createsuperuser

```
Corremos el servidor 
```
python manage.py runserver

```

## Construido con:

* [MySql](https://www.mysql.com/) - Base de Datos
* [Django](https://www.djangoproject.com/) - Framework de Desarrollo Web
* [Python](https://www.python.org/) - Lenguaje principal de Programacion

## Autor

* **Mayra Torres** - *Desarrolladora Principal  * - [mayra9821](https://github.com/mayra9821)