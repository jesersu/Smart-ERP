from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^api/v(?P<v>[0-9]+)/listaprecios/ventas/items/(?P<id_lista>[0-9]+)$',
        views.logistica_lista_favoritos),
    url(r'^api/v(?P<v>[0-9]+)/listaprecios',
        views.logistica_lista_precios),
]
