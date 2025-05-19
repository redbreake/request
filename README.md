# Django Request/Response Cycle Demonstration

Este proyecto de Django es un ejercicio diseñado para demostrar varios aspectos del manejo de objetos `HttpRequest` y la construcción de objetos `HttpResponse`. Cubre conceptos fundamentales como el acceso a atributos de la solicitud, el trabajo con middleware, el manejo de GET/POST y el uso de diferentes tipos de respuestas HTTP (básica, JSON, streaming, archivos, etc.).

## Características Demostradas

La aplicación proporciona puntos finales (endpoints) para mostrar:

*   Una página de inicio (Landing Page) básica.
*   Inspección del objeto `HttpRequest`.
*   Acceso a atributos establecidos en las vistas.
*   Acceso a atributos establecidos por el middleware.
*   Trabajo con `QueryDict` (parámetros GET/POST).
*   Uso de `HttpRequest.is_secure()`.
*   Manejo de solicitudes GET y POST en una única vista con un formulario.
*   `HttpResponse` básica.
*   Subclases de `HttpResponse` y encabezados personalizados.
*   `JsonResponse` para enviar datos en formato JSON.
*   `StreamingHttpResponse` para enviar datos en streaming.
*   `FileResponse` para servir archivos desde el servidor.
*   Uso de `HttpResponseBase` como base para respuestas personalizadas.

## Requisitos Previos

*   Python (3.8+ recomendado)
*   pip (Instalador de paquetes de Python)
*   Git (para clonar si se comparte el repositorio)

## Configuración e Instalación

1.  **Clona el repositorio (si lo subes a GitHub y alguien más lo usa):**
    ```bash
    git clone https://github.com/redbreake/request.git
    cd myproject
    ```
    

2.  **Crea y activa un entorno virtual (recomendado):**
    ```bash
    python -m venv entorno
    # En Windows
    entorno\Scripts\activate
    # En macOS/Linux
    source entorno/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea el archivo `sample_file.txt` (si no existe):**
    Asegúrate de que el archivo `demoapp/sample_file.txt` exista con algún contenido de ejemplo. Por ejemplo:
    ```
    Este es un archivo de ejemplo para ser servido por FileResponse.
    ```

## Ejecutando la Aplicación

Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver

La aplicación estará accesible en http://127.0.0.1:8000/.
Endpoints para Probar
http://127.0.0.1:8000/ - Landing Page
http://127.0.0.1:8000/request/ - Muestra información básica de HttpRequest
http://127.0.0.1:8000/request/app-attributes/ - Muestra un atributo establecido en la vista
http://127.0.0.1:8000/request/middleware/ - Muestra un atributo establecido en el middleware
http://127.0.0.1:8000/request/querydict/?param1=valor1&otro=valor2 - Demuestra QueryDict (prueba añadiendo parámetros GET)
http://127.0.0.1:8000/request/is-secure/ - Verifica HttpRequest.is_secure()
http://127.0.0.1:8000/home/ - Demostración de manejo de GET/POST con un formulario
http://127.0.0.1:8000/response/ - HttpResponse básica
http://127.0.0.1:8000/response/subclasses/ - HttpResponse con encabezados personalizados y código de estado
http://127.0.0.1:8000/response/json/ - JsonResponse
http://127.0.0.1:8000/response/streaming/ - StreamingHttpResponse
http://127.0.0.1:8000/response/file/ - FileResponse (sirve sample_file.txt)
http://127.0.0.1:8000/response/base/ - Respuesta usando una subclase de HttpResponseBase

myproject/
├── demoapp/                 # Nuestra aplicación Django
│   ├── migrations/
│   ├── templates/
│   │   └── demoapp/
│   │       └── home.html    # Plantilla para la vista GET/POST
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── middleware.py        # Middleware personalizado
│   ├── models.py
│   ├── sample_file.txt      # Archivo para FileResponse
│   ├── tests.py
│   ├── urls.py              # URLs de la app
│   └── views.py             # Lógica de las vistas
├── myproject/               # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # URLs principales del proyecto
│   └── wsgi.py
├── manage.py                # Utilidad de línea de comandos de Django
├── db.sqlite3               # Base de datos (si se usa SQLite)
├── requirements.txt         # Dependencias del proyecto
└── README.md                
