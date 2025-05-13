from django.shortcuts import render

# demoapp/views.py

from django.http import (
    HttpRequest, HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse, HttpResponseBase
)
from django.http.response import HttpResponseBase # Para la última solicitud
from django.shortcuts import render, redirect
from django.conf import settings
import time
import os
# --- Vistas para las solicitudes de HttpRequest ---

def landing_page(request: HttpRequest):
    return HttpResponse("<h1>Bienvenido a la Landing Page</h1><p>Explora las diferentes URLs.</p>")

def show_request_object(request: HttpRequest):
    # HttpRequest se muestra como una cadena con sus atributos principales
    return HttpResponse(f"<pre>Objeto HttpRequest:\n{request}\n\n"
                        f"Método: {request.method}\n"
                        f"Path: {request.path}\n"
                        f"User Agent: {request.headers.get('User-Agent', 'N/A')}\n"
                        f"GET params: {request.GET.dict()}\n"
                        f"POST params: {request.POST.dict()}</pre>")

def request_app_attributes(request: HttpRequest):
    request.my_custom_view_attribute = "Este atributo fue seteado en la vista."
    return HttpResponse(f"Atributo seteado en la vista: '{request.my_custom_view_attribute}'")

def request_middleware_attribute(request: HttpRequest):
    # El atributo 'middleware_attribute' es seteado por MyCustomMiddleware
    attr_value = getattr(request, 'middleware_attribute', 'Atributo del middleware no encontrado.')
    return HttpResponse(f"Atributo seteado por el middleware: '{attr_value}'")

def show_querydict(request: HttpRequest):
    # request.GET y request.POST son instancias de QueryDict
    # Ejemplo: http://127.0.0.1:8000/request/querydict/?nombre=Django&version=5
    response_html = f"<h2>Objetos QueryDict:</h2>"
    response_html += f"<p><b>request.GET:</b> {type(request.GET)}</p>"
    response_html += f"<pre>{request.GET.dict()}</pre>"
    response_html += f"<p>Para probar POST, usa una herramienta como Postman o un formulario.</p>"
    response_html += f"<p><b>request.POST:</b> {type(request.POST)}</p>"
    response_html += f"<pre>{request.POST.dict()}</pre>"
    return HttpResponse(response_html)

def check_is_secure(request: HttpRequest):
    is_secure = request.is_secure()
    # Nota: con `manage.py runserver` esto casi siempre será False
    # a menos que se configure un proxy inverso con HTTPS.
    return HttpResponse(f"¿La conexión es segura (HTTPS)? HttpRequest.is_secure(): {is_secure}")

def home_get_post_view(request: HttpRequest):
    context = {'message': None, 'method': request.method}
    if request.method == 'POST':
        name = request.POST.get('name_field', 'Anónimo')
        context['message'] = f"¡Hola, {name}! Recibimos tu POST."
        # En una app real, a menudo redirigirías después de un POST exitoso
        # return redirect('some_other_view_name')
    return render(request, 'demoapp/home.html', context)


# --- Vistas para las solicitudes de HttpResponse ---

def basic_http_response(request: HttpRequest):
    return HttpResponse("Este es un HttpResponse básico.")

def response_with_headers(request: HttpRequest):
    response = HttpResponse("Este es un HttpResponse con encabezados personalizados y un status code diferente.",
                            content_type="text/plain; charset=utf-8")
    response['X-Custom-Header'] = 'MiValorPersonalizado'
    response.status_code = 201 # Created
    # También se puede usar una subclase como HttpResponseForbidden, HttpResponseNotFound, etc.
    # from django.http import HttpResponseForbidden
    # return HttpResponseForbidden("Acceso denegado.")
    return response

def json_response_view(request: HttpRequest):
    data = {
        'nombre': 'Django App',
        'version': '1.0',
        'framework': 'Django',
        'features': ['URLs', 'Views', 'Responses']
    }
    return JsonResponse(data)

def stream_generator():
    """Un generador para StreamingHttpResponse."""
    yield "Inicio del stream...<br>"
    for i in range(5):
        time.sleep(0.5) # Simula una tarea que toma tiempo
        yield f"Línea {i+1} del stream.<br>"
    yield "Fin del stream."

def streaming_response_view(request: HttpRequest):
    return StreamingHttpResponse(stream_generator(), content_type="text/html") # Asegurar content_type para <br>

def file_response_view(request: HttpRequest):
    file_path = settings.DEMO_FILE_PATH
    try:
        # 'rb' es importante para FileResponse
        response = FileResponse(open(file_path, 'rb'), as_attachment=False, filename='custom_filename.txt')
        # as_attachment=True forzaría la descarga
        # filename='custom_filename.txt' sugiere un nombre al navegador si se descarga
        return response
    except FileNotFoundError:
        return HttpResponse("Archivo no encontrado en el servidor.", status=404)
    except Exception as e:
        return HttpResponse(f"Error al servir el archivo: {e}", status=500)


from django.http import HttpResponseBase

class MiRespuesta(HttpResponseBase):
    streaming = False  # Requerido por Django

    def __init__(self, contenido):
        super().__init__()
        self.content = contenido.encode('utf-8')  # ✅ Definimos .content
        self['Content-Type'] = 'text/plain'
        self['Content-Length'] = str(len(self.content))  # (opcional, pero recomendado)

    def __iter__(self):
        yield self.content

def response_base(request):
    return MiRespuesta("Respuesta usando HttpResponseBase, algunos errores pero se logro")
