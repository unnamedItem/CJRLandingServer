# Instalación del entorno virtual y ejecución de la app

Crear un entorno virtual con `Python 3.12.5`

```python -m venv venv```

Activar el entorno virtual e instalar los requerimientos

```venv/bin/activate```
```pip install -r requirements```

Correr la aplicación

```python run.py```

# Tools

Dentro de la carpeta tools guardamos varios scripts utiles

 - dashboard.py -> Genera un reporte sobre los juegos del club en formato JSON
 - games.py -> Genera la lista de juegos del club en formato JSON

# Endpoints utiles

 - /api/bgg/load -> Busca desde la API de la BGG los juegos del club que faltan agregar en la DB
 - /api/bgg/update -> Actualiza todos los juegos del club en la DB
