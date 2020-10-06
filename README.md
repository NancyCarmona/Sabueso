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
pip3 install Django==3.1.1    

Para instalar mysqlconfig en caso de MAC OS(conector para MySQl)  

`brew install mysql-client`  
`echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile`  
`export PATH="/usr/local/opt/mysql-client/bin:$PATH"`  
`pip install mysqlclient`  

CONSULTA ESTE [LINK] (https://pypi.org/project/mysqlclient/) PARA OTRO SO


- Ejecutar migración
`python3 manage.py migrate`

-Ejecutar servidor
`python3 manage.py runserver`