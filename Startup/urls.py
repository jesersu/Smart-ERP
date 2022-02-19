from django.conf.urls import url
from Startup import views as startup

urlpatterns = [
    url(r'^sincronizar$', startup.getEstadoInternet, name='sincronizar'),
]
