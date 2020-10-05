# webProgramas
Sitio web con django, monitor de proyectos  
¿Cómo se ejecuta?\
-Crear un entorno virtual dentro de la carpeta donde trabajarás (comando por consola)\
`python3 -m venv nombre_entorno_virtual`\
-Dentro de esa carpeta poner el código de este proyecto, hay 2 formas de obtenerlo.\
    1. Descargar como zip
    ![Debes dar clic donde dice Download ZIP o Descargar ZIP](https://docs.github.com/assets/images/help/repository/remotes-url.png) 
    2. Clonar en tu equipo con desktop

- Activar el entorno virtual
`source nombre_entorno_virtual/bin/activate`

- Instalar las siguientes dependencias:  
Django==3.1.1  
mysqlclient==2.0.1

Puedes hacerlo manualmente o ejecutar el siguiente comando:  
`pip install -r reqs.txt`

- Ejecutar migración
`python3 manage.py migrate`

-Ejecutar servidor
`python3 manage.py runserver`