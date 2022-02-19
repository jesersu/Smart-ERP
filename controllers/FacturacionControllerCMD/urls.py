from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v(?P<v>[0-9]+)/documentoContable/anulaciones$',
        views.getTiposDocumento),


]
