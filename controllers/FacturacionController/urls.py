from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^api/v(?P<v>[0-9]+)/tipoDocumento$', views.getTiposDocumento),
    url(r'^api/v(?P<v>[0-9]+)/documentoContable/(?P<id>[0-9]+)/archivo/(?P<tipo>[0-9]+)$',
        views.generarArchivo, name='generarArchivo'),
    url(r'^api/v(?P<v>[0-9]+)/documentoContables$', views.generarDocumento),
    url(r'api/v(?P<v>[0-9]+)/entidades/series', views.getPagosSeries),
    url(r'api/v(?P<v>[0-9]+)/parametros', views.parametrosget),
    url(r'^api/v(?P<v>[0-9]+)/generarDocumento$', views.generarDocumento2),
    url(r'^api/v(?P<v>[0-9]+)/correlativoContabilidad/(?P<id>[0-9]+)$',
        views.getCorrelativoContabilidadSerie),
    url(r'^api/v(?P<v>[0-9]+)/correlativoFinanzas/(?P<id>[0-9]+)$',
        views.getCorrelativoFinanzasSerie),
    url(r'^api/v(?P<v>[0-9]+)/correlativoLogistica/(?P<id>[0-9]+)$',
        views.getCorrelativoLogisticaSerie),
    url(r'^api/v(?P<v>[0-9]+)/emitir$',
        views.emitir),
    url(r'api/v(?P<v>[0-9]+)/moneda', views.get_moneda),
    url(r'api/v(?P<v>[0-9]+)/documentoContable/buscar',
        views.buscar_documento_contable, name='buscar'),
    url(r'api/v(?P<v>[0-9]+)/documentoContable/plantilla/html$',
        views.plantilla_html, name='plantilla_html'),

]
