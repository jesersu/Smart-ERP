import datetime
import requests
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Article, Tipo, TipoDocumento
from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.inspectors import CoreAPICompatInspector, FieldInspector, NotHandled, SwaggerAutoSchema
from drf_yasg.utils import no_body, swagger_auto_schema

from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse
from . import serializers


# Create your views here.
headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2MDM3MzJFMzIyN0MwN0JFOEQwQUJENDcyRjM4NTBBOEYzNDRFRkQiLCJ0eXAiOiJKV1QiLCJ4NWMiOlsibXNzZWd1cmlkYWQiLCJERU1PLVBWTEciXX0.eyJuYmYiOjE2MzMzNzA5NzQsImV4cCI6MTYzNTk2MjczNCwiaXNzIjoibXNzZWd1cmlkYWQiLCJhdWQiOiI5OGQ0OGU0MTE3YjY0ZWFiYmY1NmQ1OGU5YmIzYTMzOSIsInNjb3BlcyI6eyJJZFVzdWFyaW8iOjQwMjEyLCJVc3VhcmlvIjoiZGVtby1wdmxnIiwiVGlwb1Rva2VuIjoxLCJJZEVudGlkYWRQZXJzb25hIjoxLCJJZEVudGlkYWRFbXByZXNhIjo2MDAxNiwiRG9jdW1lbnRvRW1wcmVzYSI6IjAwMDAwMDAwMDAwIiwiRG9jdW1lbnRvUGVyc29uYSI6IjQzMDk0NTM2IiwiU3VjdXJzYWxlcyI6WzIwLDIxXSwiU2VydmljaW9zIjpbMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTksMjAsMjEsMjIsMjMsMjQsMjUsMjYsMjcsMjgsMjksMzAsMzEsMzIsMzMsMzQsMzUsMzYsMzcsMzgsMzksNDAsNDEsNDIsNDMsNDQsNDUsNDYsNDcsNDgsNDksNTAsNTEsNTIsNTMsNTQsNTUsNTYsNTcsNTgsNTksNjAsNjEsNjIsNjMsNjQsNjUsNjYsNjcsNjgsNjksNzAsNzEsNzIsNzMsNzQsNzUsNzYsNzcsNzgsNzksODAsODEsODIsODMsODUsODYsODcsODgsODksOTAsOTEsOTIsOTMsOTQsOTUsOTYsOTcsOTgsOTksMTAwLDEwMSwxMDIsMTAzLDEwNCwxMDUsMTA2LDEwNywxMDgsMTA5LDExMCwxMTEsMTEyLDExMywxMTQsMTE1LDExNiwxMTcsMTE4LDExOSwxMjAsMTIxLDEyMiwxMjMsMTI0LDEyNSwxMjYsMTI3LDEyOCwxMjksMTMwLDEzMSwxMzIsMTMzLDEzNCwxMzUsMTM2LDEzNywxMzgsMTM5LDE0MCwxNDEsMTQyLDE0MywxNDQsMTQ1LDE0NiwxNDcsMTQ4LDE0OSwxNTAsMTUxLDE1MiwxNTMsMTU0LDE1NSwxNTYsMTU3LDE1OCwxNjAsMTY1LDE3NywxNzgsMTc5LDE4MSwyMTcsMjE4LDIxOSwyMjIsMjIzLDIzMiwyNzQsMjgxLDI4OCwyODksMzYyLDM3MiwzODEsMzg1LDM4NiwzODcsMzg4LDM4OSwzOTAsMzkxLDM5MiwzOTMsMzk0LDM5NSw0NTEsNDY3LDQ2OCw0NjksNDcwLDUwMCw1MDEsNTAyLDUwMyw1MDQsNTA1LDUwNiw1MDcsNTA4LDUwOSw1MTAsNTExLDUxMiw1MTMsNTE0LDUxNSw1MTYsNTE3LDE3NiwxODAsMTg1LDE2MSwxOTEsMTkyLDIzMywyMzQsMTY2LDE2NywxNjgsMTY5LDE3MCwxNzEsMTcyLDE3MywxNzQsMTc1LDE4MywyMDksMTU5LDE2MiwxNjMsMTY0LDE4NCwyMjcsMjc1LDI3NiwzNTksMzYwLDM2MSwzNzUsMzc2LDg0LDE4MiwxODYsMTg3LDE4OCwxODksMTkwLDE5MywxOTQsMTk1LDE5NiwxOTcsMTk4LDE5OSwyMDAsMjAxLDIwMiwyMDMsMjA0LDIwNSwyMDYsMjA3LDIwOCwyMTAsMjExLDIxMiwyMTMsMjE0LDIxNSwyMTYsMjIwLDIyMSwyMjQsMjI1LDIyNiwyMjgsMjI5LDIzMCwyMzEsMjM1LDIzNiwyMzcsMjM4LDIzOSwyNDAsMjQxLDI0MiwyNDMsMjQ0LDI0NSwyNDYsMjQ3LDI0OCwyNDksMjUwLDI1MSwyNTIsMjUzLDI1NCwyNTUsMjU2LDI1NywyNTgsMjU5LDI2MCwyNjEsMjYyLDI2MywzMjcsMzI4LDI2NCwyNjUsMjY2LDI2NywyNjgsMjY5LDI3MCwyNzEsMjcyLDM1NywzNTgsMjczLDI4NCwyODUsMjg2LDMxOSwzMjAsMzIxLDMyMiwzMjMsMzI0LDMyNSwzMjYsMzI5LDMzMCwzMTcsMzE4LDI3NywyOTAsMzEwLDMxMSwzMTIsMzE1LDMxNiwzMzksMzQzLDM0NCwzNDYsMzQ3LDM1MywzNzcsNDIzLDQyNCw0MjksNDMwLDQzMiw0MzMsNDM0LDQzNSw0MzYsNDQ2LDQ0Nyw0NDgsNDQ5LDQ1MCw0MTksNDIwLDQyMSw0MjIsNDI1LDQyNiw0MjcsNDI4LDQzMSw0MzcsNDM4LDQzOSw0NDAsNDQxLDQ0Miw0NDMsNDQ0LDQ0NSwzOTgsMzk5LDQ1Miw0NTMsNDU0LDQ1NSw0NTYsNDU3LDQ1OCw0NTksNDYwLDQ2MV19fQ.O_myVVBhcbMNwh-JLN-SeQ1hFym3e-ERZ6OFGynF6If80Ii_JOEuUeV1RxtFoDoQGhYvJ7EN_ZdzOJzDJy32SVLa8W6dWW-vvF8Jyfv8SAnCXWafPwseG2SO8TBkdlmMrl6WeAN3zYoaq_iYc6SfwMKak9ewweJE-sW91Qw2lck9_VPPBjfhuWeh1H9wioaXFC0RHpmNSX9CVt-rbvjjsBwlY_e1TYxtOMF9_3mBWfNGoST7-U38C1MrHdxPYhHDJIwwL2GEof-917Kx9qThOTtyNk0yMnzMD7TRVz-fhj2UORu60puyN27kUZq5mioJh_Rt4EVnLh-oxTmTsOGVdw', 'Content-type': 'application/json', 'Accept': 'text/plain'}


class TipoViewSet(APIView):
    serializer_class = serializers.TipoSerializers
    throttle_scope = "tanto"

    def get_queryset(self):
        cars = Tipo.objects.all()
        return cars


class TipoDocumentoApiView(APIView):
    serializer_class = serializers.TipoDocumentoSerializers
    throttle_scope = "tanto"

    def get_queryset(self):
        cars = TipoDocumento.objects.all()
        return cars


class GatoConBotasMixin:
    def mi_listado(self, request, *args, **kwargs):
        if("tipo" in self.request.query_params):
            tipo = self.request.query_params['tipo']
            print(tipo)


@api_view(['GET'])
def gettipodocumento(request):
    tipo = '*'

    if request.query_params['tipo']:
        tipo = request.query_params['tipo'][0]
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'tipoDocumento?tipo=' + tipo, headers=headers)
    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def parametrosget(request):
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'parametros?idParametro=' + request.GET['idparametro'] + '&estado='+request.GET['estado'], headers=headers)

    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def getPagosSeries(request):
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'entidades/series?listaTiposDocumentos=' + request.GET['listaTiposDocumentos'] + '&tipoSerie=' + request.GET['tipoSerie'], headers=headers)

    return JsonResponse(response.json(), safe=False)
