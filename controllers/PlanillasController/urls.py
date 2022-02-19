from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^api/v(?P<v>[0-9]+)/entidades/relacionados/documentos',
        views.logistica_lista_favoritos),

]
