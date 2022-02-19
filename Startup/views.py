from django.db.models.query import EmptyQuerySet
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from Startup import serializers
from repositorio.ERPProxyEntities.contabilidad.models import TipoDocumento
from django.conf import settings
from rest_framework.decorators import api_view


@api_view(['GET'])
def getEstadoInternet(request):
    estado = 1
    print("estado : ", estado)
    if estado > 0:
        headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2MDM3MzJFMzIyN0MwN0JFOEQwQUJENDcyRjM4NTBBOEYzNDRFRkQiLCJ0eXAiOiJKV1QiLCJ4NWMiOlsibXNzZWd1cmlkYWQiLCJhdmFyZ2FzLWdpdCJdfQ.eyJuYmYiOjE2MzEyOTk2ODksImV4cCI6MTYzMzg5MTQ0OSwiaXNzIjoibXNzZWd1cmlkYWQiLCJhdWQiOiIzNDUxNDNjZDNhOTk0YjQ3ODQ5MjMwMmYwOGIzNGNjMyIsInNjb3BlcyI6eyJJZFVzdWFyaW8iOjUwOTE0LCJVc3VhcmlvIjoiYXZhcmdhcy1naXQiLCJUaXBvVG9rZW4iOjAsIklkRW50aWRhZFBlcnNvbmEiOjcwMjY5LCJJZEVudGlkYWRFbXByZXNhIjoxMDAxNSwiRG9jdW1lbnRvRW1wcmVzYSI6IjIwNDU1MTE0NTYxIiwiRG9jdW1lbnRvUGVyc29uYSI6IjEwNzI1NjkwMjA0IiwiU3VjdXJzYWxlcyI6W10sIlNlcnZpY2lvcyI6WzEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzLDE0LDE1LDE2LDE3LDE4LDE5LDIwLDIxLDIyLDIzLDI0LDI1LDI2LDI3LDI4LDI5LDMwLDMxLDMyLDMzLDM0LDM1LDM2LDM3LDM4LDM5LDQwLDQxLDQyLDQzLDQ0LDQ1LDQ2LDQ3LDQ4LDQ5LDUwLDUxLDUyLDUzLDU0LDU1LDU2LDU3LDU4LDU5LDYwLDYxLDYyLDYzLDY0LDY1LDY2LDY3LDY4LDY5LDcwLDcxLDcyLDczLDc0LDc1LDc2LDc3LDc4LDc5LDgwLDgxLDgyLDgzLDg1LDg2LDg3LDg4LDg5LDkwLDkxLDkyLDkzLDk0LDk1LDk2LDk3LDk4LDk5LDEwMCwxMDEsMTAyLDEwMywxMDQsMTA1LDEwNiwxMDcsMTA4LDEwOSwxMTAsMTExLDExMiwxMTMsMTE0LDExNSwxMTYsMTE3LDExOCwxMTksMTIwLDEyMSwxMjIsMTIzLDEyNCwxMjUsMTI2LDEyNywxMjgsMTI5LDEzMCwxMzEsMTMyLDEzMywxMzQsMTM1LDEzNiwxMzcsMTM4LDEzOSwxNDAsMTQxLDE0MiwxNDMsMTQ0LDE0NSwxNDYsMTQ3LDE0OCwxNDksMTUwLDE1MSwxNTIsMTUzLDE1NCwxNTUsMTU2LDE1NywxNTgsMTYwLDE2NSwxNzcsMTc4LDE3OSwxODEsMjE3LDIxOCwyMTksMjIyLDIyMywyMzIsMjc0LDI4MSwyODgsMjg5LDM2MiwzNzIsMzgxLDM4NSwzODYsMzg3LDM4OCwzODksMzkwLDM5MSwzOTIsMzkzLDM5NCwzOTUsNDUxLDQ2Nyw0NjgsNDY5LDQ3MCw1MDAsNTAxLDUwMiw1MDMsNTA0LDUwNSw1MDYsNTA3LDUwOCw1MDksNTEwLDUxMSw1MTIsNTEzLDUxNCw1MTUsNTE2LDUxN119fQ.Wlhi3K-CDgNVM_6udENyccjmA1c0RyQhj3S8tEvGABOBZWRo0iR0_-o7DuAPY3GuHEjxIlFCWZ2_KJN8YM_JsX_CsIRbiRDCbMr8DI5zF6sELG42fkJ5Q5pwkteHLjfP_IkF46sh4tOZpSY1m1espV4Tfm3nAepGaANGHbB2JNXT2kL-sjlnUCMxKszMAMwIRGQpJGy6mpQRZkQLpcYGCy1Jqk3CETV4PmDqGF_EbdlSi4CHtzpK5V_GuqerSbN5kwuqKqzvs0TNp90BnvbFmYY_iRem86mUrXXkqTpZlE2mAH4M-e7u2SRUtwJ1I6owX6P0QKNbo6BNUH9OdV3fpA'}
        response = requests.get(
            settings.URL_MSFACTURACIONQRY + 'tipoDocumento?tipo=A', headers=headers)
        tiposDocumentos = json.loads(response.content)

        for documentos in tiposDocumentos:
            docu = TipoDocumento()
            serializer = TipoDocumento(documentos)
            docu.abreviacion = documentos['Abreviacion']
            docu.codigo = documentos['Codigo']
            docu.descripcion = documentos['Descripcion']
            docu.log_usuariocreacion = documentos['LogUsuariocrea']
            docu.idtipo_documento = documentos['Id']
            docu.log_fechacreacion = documentos['LogFechacrea']
            docu.log_usuariomodif = documentos['LogUsuariomodif']
            docu.log_fechamodif = documentos['LogFechamodif']

            docu.log_estado = documentos['LogEstado']
            docu.save()

        return Response(json.loads(response.content), status=status.HTTP_200_OK)
    else:
        documentos = TipoDocumento.objects.all()
        serializer = serializers.TipoDocumento2Serializer(
            documentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EstadoInternetViews(viewsets.ViewSet):
    def tipodocrepo():
        response = requests.get(
            settings.URL_MSFACTURACIONQRY + 'tipoDocumento?tipo=A')
        print(response.content)
        if response.status_code == 200:
            return response.json()

    def list(self, request, format=None):

        documentos = TipoDocumento.objects.all()
        serializer = serializers.TipoDocumento2Serializer(
            documentos, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TipoDocumento(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def getEstadoInternet(estado=None):

        print("estado : ", estado)
        if estado > 0:
            headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2MDM3MzJFMzIyN0MwN0JFOEQwQUJENDcyRjM4NTBBOEYzNDRFRkQiLCJ0eXAiOiJKV1QiLCJ4NWMiOlsibXNzZWd1cmlkYWQiLCJhdmFyZ2FzLWdpdCJdfQ.eyJuYmYiOjE2MzEyOTk2ODksImV4cCI6MTYzMzg5MTQ0OSwiaXNzIjoibXNzZWd1cmlkYWQiLCJhdWQiOiIzNDUxNDNjZDNhOTk0YjQ3ODQ5MjMwMmYwOGIzNGNjMyIsInNjb3BlcyI6eyJJZFVzdWFyaW8iOjUwOTE0LCJVc3VhcmlvIjoiYXZhcmdhcy1naXQiLCJUaXBvVG9rZW4iOjAsIklkRW50aWRhZFBlcnNvbmEiOjcwMjY5LCJJZEVudGlkYWRFbXByZXNhIjoxMDAxNSwiRG9jdW1lbnRvRW1wcmVzYSI6IjIwNDU1MTE0NTYxIiwiRG9jdW1lbnRvUGVyc29uYSI6IjEwNzI1NjkwMjA0IiwiU3VjdXJzYWxlcyI6W10sIlNlcnZpY2lvcyI6WzEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzLDE0LDE1LDE2LDE3LDE4LDE5LDIwLDIxLDIyLDIzLDI0LDI1LDI2LDI3LDI4LDI5LDMwLDMxLDMyLDMzLDM0LDM1LDM2LDM3LDM4LDM5LDQwLDQxLDQyLDQzLDQ0LDQ1LDQ2LDQ3LDQ4LDQ5LDUwLDUxLDUyLDUzLDU0LDU1LDU2LDU3LDU4LDU5LDYwLDYxLDYyLDYzLDY0LDY1LDY2LDY3LDY4LDY5LDcwLDcxLDcyLDczLDc0LDc1LDc2LDc3LDc4LDc5LDgwLDgxLDgyLDgzLDg1LDg2LDg3LDg4LDg5LDkwLDkxLDkyLDkzLDk0LDk1LDk2LDk3LDk4LDk5LDEwMCwxMDEsMTAyLDEwMywxMDQsMTA1LDEwNiwxMDcsMTA4LDEwOSwxMTAsMTExLDExMiwxMTMsMTE0LDExNSwxMTYsMTE3LDExOCwxMTksMTIwLDEyMSwxMjIsMTIzLDEyNCwxMjUsMTI2LDEyNywxMjgsMTI5LDEzMCwxMzEsMTMyLDEzMywxMzQsMTM1LDEzNiwxMzcsMTM4LDEzOSwxNDAsMTQxLDE0MiwxNDMsMTQ0LDE0NSwxNDYsMTQ3LDE0OCwxNDksMTUwLDE1MSwxNTIsMTUzLDE1NCwxNTUsMTU2LDE1NywxNTgsMTYwLDE2NSwxNzcsMTc4LDE3OSwxODEsMjE3LDIxOCwyMTksMjIyLDIyMywyMzIsMjc0LDI4MSwyODgsMjg5LDM2MiwzNzIsMzgxLDM4NSwzODYsMzg3LDM4OCwzODksMzkwLDM5MSwzOTIsMzkzLDM5NCwzOTUsNDUxLDQ2Nyw0NjgsNDY5LDQ3MCw1MDAsNTAxLDUwMiw1MDMsNTA0LDUwNSw1MDYsNTA3LDUwOCw1MDksNTEwLDUxMSw1MTIsNTEzLDUxNCw1MTUsNTE2LDUxN119fQ.Wlhi3K-CDgNVM_6udENyccjmA1c0RyQhj3S8tEvGABOBZWRo0iR0_-o7DuAPY3GuHEjxIlFCWZ2_KJN8YM_JsX_CsIRbiRDCbMr8DI5zF6sELG42fkJ5Q5pwkteHLjfP_IkF46sh4tOZpSY1m1espV4Tfm3nAepGaANGHbB2JNXT2kL-sjlnUCMxKszMAMwIRGQpJGy6mpQRZkQLpcYGCy1Jqk3CETV4PmDqGF_EbdlSi4CHtzpK5V_GuqerSbN5kwuqKqzvs0TNp90BnvbFmYY_iRem86mUrXXkqTpZlE2mAH4M-e7u2SRUtwJ1I6owX6P0QKNbo6BNUH9OdV3fpA'}
            response = requests.get(
                settings.URL_MSFACTURACIONQRY + 'tipoDocumento?tipo=A', headers=headers)
            tiposDocumentos = json.loads(response.content)

            for documentos in tiposDocumentos:
                docu = TipoDocumento()
                serializer = TipoDocumento(documentos)
                docu.abreviacion = documentos['Abreviacion']
                docu.codigo = documentos['Codigo']
                docu.descripcion = documentos['Descripcion']
                docu.log_usuariocreacion = documentos['LogUsuariocrea']
                docu.idtipo_documento = documentos['Id']
                docu.log_fechacreacion = documentos['LogFechacrea']
                docu.log_usuariomodif = documentos['LogUsuariomodif']
                docu.log_fechamodif = documentos['LogFechamodif']

                docu.log_estado = documentos['LogEstado']
                docu.save()

            return Response(json.loads(response.content), status=status.HTTP_200_OK)
        else:
            documentos = TipoDocumento.objects.all()
            serializer = serializers.TipoDocumento2Serializer(
                documentos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
