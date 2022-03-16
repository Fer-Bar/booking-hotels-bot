<h1 align="center">Selenium-Bot-Python ⚙️</h1>

> Este es un Bot hecho en Selenium con Python que permite realizar búsquedas automatizadas para la reserva de habitaciones en la página web de [Booking.com](https://booking.com/). <br>

![scraper_main](https://user-images.githubusercontent.com/90936639/154614011-c5a6be0a-7e74-4fce-b743-9d6cea865504.png)

>  El repositorio consta de:
> - El script [booking.py](booking.py) que contiene los métodos de montaje y desmontaje del bot. Además contiene las funciones que interactúan con la página web.
> - El script [booking_reports.py](booking_reports.py) se encarga de obtener los datos necesarios del raspado para realizar reportes muy detallados de las habitaciones disponibles que se encuentran en la página web.
> - El script [booking_filtration.py](booking_filtration.py) que filtra las habitaciones por su puntuación en estrellas y el precio más bajo disponible.
> - El script [run.py](run.py) que ejecuta el bot y sus acciones en base a los requerimientos del usuario.
> - Un archivo [constants.py](constants.py) que contiene las variables constantes como la URL del sitio.


## Pre-Requisitos
- Tener Python instalado con una versión superior a la 3.8.
- Tener instalado el Driver del navegador a usar, para lanzar esta automatización usare chromedriver.exe.

   - Asegurate que la versión del Driver coincida con la versión de tu navegador. Solo copia y pega esto `chrome://version/` en tu navegador para averiguar su versión.
   - [Descargar Drivers de Chrome](https://chromedriver.storage.googleapis.com/index.html)

## Como Usarlo
1. Ve al directorio donde quieras crear el proyecto y clona el repositorio

    ```
    git clone https://github.com/Fer-Bar/selenium-bot-python.git
    ```
2. Crea un entorno virtual:
    ```
    python3 -m venv venv
    ```
    Una vez creado puedes activarlo.
    <br>
    
    En Windows ejecutando:
    ```
    venv\Scripts\activate.bat
    ```
    En Unix o MacOS, ejecutando:
    ```
    source venv/bin/activate
    ```   
3. Instala las depedencias `pip install -r requirements.txt`
4. Reemplaza la variable `driver_path` del archivo [booking.py](booking.py) con la ruta donde se encuentra su driver instalado.
5. En caso de no necesitar todas las filtraciones de búsqueda puede revisar el código y comentar las lineas que crea necesarias (cada función tiene información detallada en el código)
6. Ejecutar [run.py](run.py) en consola y completar las preguntas propuestas.

![first_console](https://user-images.githubusercontent.com/90936639/154614720-5f06e3e7-7601-46ac-95a2-50ae097244fb.png)

7. Al final de la ejecución se nos mostrará el reporte en forma de tabla con todos los hoteles que cumplieron con los criterios de búsqueda.


## NOTAS
- Algunos sitios webs renovan o cambian la estructura de su código, si nota que ocurre un cambio en el sitio web que no permita que se ejecute el bot. Contactese por email: linofernando2703@gmail.com o por medio de un issue en Github
