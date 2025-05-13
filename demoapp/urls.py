# demoapp/urls.py

from django.urls import path
from . import views

app_name = 'demoapp' # Opcional, pero buena práctica para namespacing

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('request/', views.show_request_object, name='show_request_object'),
    path('request/app-attributes/', views.request_app_attributes, name='request_app_attributes'),
    path('request/middleware/', views.request_middleware_attribute, name='request_middleware_attribute'),
    path('request/querydict/', views.show_querydict, name='show_querydict'),
    path('request/is-secure/', views.check_is_secure, name='check_is_secure'),
    path('home/', views.home_get_post_view, name='home_get_post'),

    path('response/', views.basic_http_response, name='basic_http_response'),
    path('response/subclasses/', views.response_with_headers, name='response_with_headers'), # También demuestra subclases
    path('response/json/', views.json_response_view, name='json_response_view'),
    path('response/streaming/', views.streaming_response_view, name='streaming_response_view'),
    path('response/file/', views.file_response_view, name='file_response_view'),
    path('response/base/', views.response_base),
]