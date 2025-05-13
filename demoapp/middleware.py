# demoapp/middleware.py

class MyCustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configuración única e inicialización.

    def __call__(self, request):
        # Código a ejecutar para cada solicitud antes
        # de que la vista (y el middleware posterior) sea llamada.
        request.middleware_attribute = "Este atributo fue seteado por el Middleware"

        response = self.get_response(request)

        # Código a ejecutar para cada solicitud/respuesta después
        # de que la vista es llamada.

        return response