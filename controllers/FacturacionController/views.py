import js2py
import html
from pybars import Compiler
from django.shortcuts import render
import datetime
from os import renames
import requests
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.conf import settings
from entidades.models import GenerarDocumento, PdfToBase64, Items, PlantillaResponse
import json
from rest_framework.response import Response
from repositorio.ERPQueryEntities.views import *
from rest_framework.permissions import IsAuthenticated
from repositorio.ERPProxyEntities.contabilidad.models import *
from utils.constantes import ESTADO_ACTIVO
from utils.generar_pdf import generar_comprobante
from utils.extensionFunction import toBase64
from utils.rutas import URL_LOGISTICA_QRY, URL_MSFACTURACIONCMD, URL_PROXY

# Create your views here.
headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2MDM3MzJFMzIyN0MwN0JFOEQwQUJENDcyRjM4NTBBOEYzNDRFRkQiLCJ0eXAiOiJKV1QiLCJ4NWMiOlsibXNzZWd1cmlkYWQiLCJERU1PLVBWTEciXX0.eyJuYmYiOjE2MzMzNzA5NzQsImV4cCI6MTYzNTk2MjczNCwiaXNzIjoibXNzZWd1cmlkYWQiLCJhdWQiOiI5OGQ0OGU0MTE3YjY0ZWFiYmY1NmQ1OGU5YmIzYTMzOSIsInNjb3BlcyI6eyJJZFVzdWFyaW8iOjQwMjEyLCJVc3VhcmlvIjoiZGVtby1wdmxnIiwiVGlwb1Rva2VuIjoxLCJJZEVudGlkYWRQZXJzb25hIjoxLCJJZEVudGlkYWRFbXByZXNhIjo2MDAxNiwiRG9jdW1lbnRvRW1wcmVzYSI6IjAwMDAwMDAwMDAwIiwiRG9jdW1lbnRvUGVyc29uYSI6IjQzMDk0NTM2IiwiU3VjdXJzYWxlcyI6WzIwLDIxXSwiU2VydmljaW9zIjpbMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTksMjAsMjEsMjIsMjMsMjQsMjUsMjYsMjcsMjgsMjksMzAsMzEsMzIsMzMsMzQsMzUsMzYsMzcsMzgsMzksNDAsNDEsNDIsNDMsNDQsNDUsNDYsNDcsNDgsNDksNTAsNTEsNTIsNTMsNTQsNTUsNTYsNTcsNTgsNTksNjAsNjEsNjIsNjMsNjQsNjUsNjYsNjcsNjgsNjksNzAsNzEsNzIsNzMsNzQsNzUsNzYsNzcsNzgsNzksODAsODEsODIsODMsODUsODYsODcsODgsODksOTAsOTEsOTIsOTMsOTQsOTUsOTYsOTcsOTgsOTksMTAwLDEwMSwxMDIsMTAzLDEwNCwxMDUsMTA2LDEwNywxMDgsMTA5LDExMCwxMTEsMTEyLDExMywxMTQsMTE1LDExNiwxMTcsMTE4LDExOSwxMjAsMTIxLDEyMiwxMjMsMTI0LDEyNSwxMjYsMTI3LDEyOCwxMjksMTMwLDEzMSwxMzIsMTMzLDEzNCwxMzUsMTM2LDEzNywxMzgsMTM5LDE0MCwxNDEsMTQyLDE0MywxNDQsMTQ1LDE0NiwxNDcsMTQ4LDE0OSwxNTAsMTUxLDE1MiwxNTMsMTU0LDE1NSwxNTYsMTU3LDE1OCwxNjAsMTY1LDE3NywxNzgsMTc5LDE4MSwyMTcsMjE4LDIxOSwyMjIsMjIzLDIzMiwyNzQsMjgxLDI4OCwyODksMzYyLDM3MiwzODEsMzg1LDM4NiwzODcsMzg4LDM4OSwzOTAsMzkxLDM5MiwzOTMsMzk0LDM5NSw0NTEsNDY3LDQ2OCw0NjksNDcwLDUwMCw1MDEsNTAyLDUwMyw1MDQsNTA1LDUwNiw1MDcsNTA4LDUwOSw1MTAsNTExLDUxMiw1MTMsNTE0LDUxNSw1MTYsNTE3LDE3NiwxODAsMTg1LDE2MSwxOTEsMTkyLDIzMywyMzQsMTY2LDE2NywxNjgsMTY5LDE3MCwxNzEsMTcyLDE3MywxNzQsMTc1LDE4MywyMDksMTU5LDE2MiwxNjMsMTY0LDE4NCwyMjcsMjc1LDI3NiwzNTksMzYwLDM2MSwzNzUsMzc2LDg0LDE4MiwxODYsMTg3LDE4OCwxODksMTkwLDE5MywxOTQsMTk1LDE5NiwxOTcsMTk4LDE5OSwyMDAsMjAxLDIwMiwyMDMsMjA0LDIwNSwyMDYsMjA3LDIwOCwyMTAsMjExLDIxMiwyMTMsMjE0LDIxNSwyMTYsMjIwLDIyMSwyMjQsMjI1LDIyNiwyMjgsMjI5LDIzMCwyMzEsMjM1LDIzNiwyMzcsMjM4LDIzOSwyNDAsMjQxLDI0MiwyNDMsMjQ0LDI0NSwyNDYsMjQ3LDI0OCwyNDksMjUwLDI1MSwyNTIsMjUzLDI1NCwyNTUsMjU2LDI1NywyNTgsMjU5LDI2MCwyNjEsMjYyLDI2MywzMjcsMzI4LDI2NCwyNjUsMjY2LDI2NywyNjgsMjY5LDI3MCwyNzEsMjcyLDM1NywzNTgsMjczLDI4NCwyODUsMjg2LDMxOSwzMjAsMzIxLDMyMiwzMjMsMzI0LDMyNSwzMjYsMzI5LDMzMCwzMTcsMzE4LDI3NywyOTAsMzEwLDMxMSwzMTIsMzE1LDMxNiwzMzksMzQzLDM0NCwzNDYsMzQ3LDM1MywzNzcsNDIzLDQyNCw0MjksNDMwLDQzMiw0MzMsNDM0LDQzNSw0MzYsNDQ2LDQ0Nyw0NDgsNDQ5LDQ1MCw0MTksNDIwLDQyMSw0MjIsNDI1LDQyNiw0MjcsNDI4LDQzMSw0MzcsNDM4LDQzOSw0NDAsNDQxLDQ0Miw0NDMsNDQ0LDQ0NSwzOTgsMzk5LDQ1Miw0NTMsNDU0LDQ1NSw0NTYsNDU3LDQ1OCw0NTksNDYwLDQ2MV19fQ.O_myVVBhcbMNwh-JLN-SeQ1hFym3e-ERZ6OFGynF6If80Ii_JOEuUeV1RxtFoDoQGhYvJ7EN_ZdzOJzDJy32SVLa8W6dWW-vvF8Jyfv8SAnCXWafPwseG2SO8TBkdlmMrl6WeAN3zYoaq_iYc6SfwMKak9ewweJE-sW91Qw2lck9_VPPBjfhuWeh1H9wioaXFC0RHpmNSX9CVt-rbvjjsBwlY_e1TYxtOMF9_3mBWfNGoST7-U38C1MrHdxPYhHDJIwwL2GEof-917Kx9qThOTtyNk0yMnzMD7TRVz-fhj2UORu60puyN27kUZq5mioJh_Rt4EVnLh-oxTmTsOGVdw', 'Content-type': 'application/json', 'Accept': 'text/plain'}


@api_view(['GET'])
def getTiposDocumento(request, v):
    tipo = '*'
    if request.query_params['tipo']:
        tipo = request.query_params['tipo'][0]
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'tipoDocumento?redis=' + request.GET['redis'] + '&tipo=' + tipo, headers=headers)
    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def getCorrelativoContabilidadSerie(request, v, id):
    try:
        response = getCorrelativoContabilidad(id)
        return JsonResponse(response.correlativo, safe=False)
    except:
        return JsonResponse(-1, safe=False)


@api_view(['GET'])
def getCorrelativoFinanzasSerie(request, v, id):
    try:
        response = getCorrelativoFinanzas(id)
        return JsonResponse(response.Correlativo, safe=False)
    except:
        return JsonResponse(-1, safe=False)


@api_view(['GET'])
def getCorrelativoLogisticaSerie(request, v, id):
    try:
        response = getCorrelativoLogistica(id)
        return JsonResponse(response.Correlativo, safe=False)
    except:
        return JsonResponse(-1, safe=False)


@api_view(['POST'])
def generarDocumento(request, v):
    data = request.data
    generar = GenerarDocumento(**data)

    """ 
    Tipo Documento
    1003 -> Factura
    1004 -> Boleta venta
    1005 -> nota de credito
    1006 -> nota de debito
    1007 -> guia de remision
    Boleta
     """

    generar_comprobante(generar)

    response = requests.post(
        URL_MSFACTURACIONCMD+'documentoContable', data=json.dumps(data), headers=headers)
    print(response)
    return HttpResponse(response, content_type='application/json')


@api_view(['POST'])
def generarDocumento2(request, v):
    data = request.data
    generar = GenerarDocumento(**data)

    correlativo_response = requests.get(
        URL_PROXY+'api/v1/correlativoContabilidad/1')

    print('correlativo')
    print(correlativo_response.content)

    response = requests.post(
        settings.URL_MSFACTURACIONQRY+'documentoContable', data, headers)

    if response.status_code != 200:
        return HttpResponse(response.content.json(), content_type='application/json')
    # verficar status de response

    generar_pdf = GenerarComprobante()

    #serializer = DocumentoContable(documentoContable)
    generar_pdf.fecha_emision = generar.FechaEmision
    generar_pdf.fecha_vencimiento = generar.FechaVencimiento
    generar_pdf.idcondicion_pago = generar.IdCondicionPago
    generar_pdf.idempresa = generar.IdEmpresa
    generar_pdf.identidad_emisor = generar.IdEntidadEmisor
    generar_pdf.identidad_receptora = generar.IdEntidadReceptora
    generar_pdf.idestado = generar.IdEstadoComprobante
    generar_pdf.idmoneda = generar.IdMoneda
    generar_pdf.id_serie = generar.IdSerie
    generar_pdf.idtipo_documento = generar.IdTipoDocumento
    generar_pdf.numero_documento = '000000000'
    generar_pdf.monto_igv = generar.MontoIGV
    generar_pdf.monto_isc = generar.MontoISC
    generar_pdf.monto_subtotal = generar.MontoSubTotal
    generar_pdf.monto_total = generar.MontoTotal
    generar_pdf.observacion = generar.Observaciones
    generar_pdf.tipo_operacion = generar.TipoOperacion
    generar_pdf.otros_cargos = generar.OtrosCargos
    generar_pdf.otros_tributos = generar.OtrosTributos
    generar_pdf.peso_bruto = generar.PesoBruto
    generar_pdf.peso_neto = generar.PesoNeto
    generar_pdf.total_precio_venta = generar.TotalPrecioVenta
    generar_pdf.valorigv = generar.ValorIGV
    generar_pdf.log_usuariocreacion = 'jess'
    generar_pdf.log_fechacreacion = str(datetime.datetime.now())
    generar_pdf.log_usuariomodif = 'jess'
    generar_pdf.log_fechamodif = str(datetime.datetime.now())
    generar_pdf.log_estado = ESTADO_ACTIVO\

    generar_pdf.montoAnticipo = generar.MontoAnticipo
    generar_pdf.montoDescuento = generar.MontoDescuento
    generar_pdf.monto_igv_gratuito = generar.MontoIGVGratuito
    generar_pdf.numero_contrato = generar.NumeroContrato
    generar_pdf.operaciones_exoneradas = generar.OperacionesExoneradas
    generar_pdf.operaciones_exportadas = generar.OperacionesExportadas
    generar_pdf.operaciones_gratuitas = generar.OperacionesGratuitas
    generar_pdf.operaciones_gravadas = generar.OperacionesGravadas
    generar_pdf.operaciones_inafectas = generar.OperacionesInafectas
    generar_pdf.otros_cargos_sumatoria = generar.OtrosCargosSumatoria
    generar_pdf.receptor_correo = generar.ReceptorCorreo
    generar_pdf.receptor_numero_documento = generar.ReceptorNumeroDocumento
    generar_pdf.receptor_razon_social = generar.ReceptorRazonSocial
    generar_pdf.receptor_tipo_documento = generar.ReceptorTipoDocumento
    generar_pdf.descripcion = generar.DescripcionEspecial1
    generar_pdf.suma_descuentos_no_afectan_base = generar.SumaDescuentosNoAfectanBase
    generar_pdf.sumatoriaIcbper = generar.SumatoriaIcbper

    for item in generar.ListaItems:
        item_obj = DetalleDocumento()
        item_obj.id_tipo_afectacion_igv = item.IdTipoAfectacionIGV
        item_obj.id_tipo_precio_venta_unitario = item.IdTipoPrecioVentaUnitario
        item_obj.precio_venta_item = item.PrecioVentaItem
        item_obj.id_lote = item.IdLote
        item_obj.peso_bruto = item.PesoBruto
        item_obj.peso_neto = item.PesoNeto
        #item_obj.es_de_stock = item.EsDeStock
        item_obj.cantidad = item.Cantidad
        item_obj.id_moneda = item.IdMoneda
        item_obj.codigo_barras = item.CodigoBarras
        item_obj.save()
        # codigos alternatios
        # codigos modelo
        # lista parametro

        for para in item.ListaParametros:
            detalle_parametro = DetalledocumentoParametro()
            detalle_parametro.idparametro = para.IdParametro
            detalle_parametro.iddominio = para.IdDominio
            detalle_parametro.tipo = para.Tipo
            detalle_parametro.auxiliar1 = para.Auxiliar1
            detalle_parametro.auxiliar2 = para.Auxiliar2
            detalle_parametro.auxiliar3 = para.Auxiliar3
            detalle_parametro.valor = para.Valor
            detalle_parametro.save()
        # lotes item

        item_obj.valorigv = item.ValorIGV
        item_obj.descripcion_item = item.ItemDescripcion
        item_obj.descuento = item.Descuento
        item_obj.otros_cargos_item = item.OtrosCargosItem
        item_obj.otros_tributos = item.OtrosTributos
        item_obj.descuento_porcentaje = item.DescuentoPorcentaje
        item_obj.descuento_precio = item.DescuentoPrecio
        item_obj.iddetalleorigen = item.IdDetalleOrigen
        item_obj.idmsorigen = item.IdMSOrigen
        item_obj.id_origen = item.IdOrigen
        item_obj.precio_unitario = item.PrecioUnitario
        item_obj.monto_isc = item.MontoISC
        item_obj.valor_venta = item.ValorVenta
        item_obj.valor_unitario = item.ValorUnitario
        item_obj.codigo_unidad = item.CodigoUnidad
        # itemunidad

        item_obj.id_referencia = item.IdReferencia
        item_obj.igv = item.IGV
        item_obj.item = item.Item
        item_obj.stock = item.Stock  # ?
        item_obj.icbper = item.ICBPER
        item_obj.nombre_marca = item.NombreMarca
        item_obj.id_inventario = item.IdInventario
        item_obj.tipo_item = item.TipoItem
        item_obj.codigo_item = item.CodigoItem
        item_obj.id_almacen = item.IdAlmacen
        item_obj.es_de_lista = int(item.EsDeLista)  # =?
        item_obj.precio_base = item.PrecioBase  # =?
        item_obj.url_imagen = item.UrlImagen  # =?
        item_obj.controlar_stock = item.ControlarStock  # =?
        item_obj.mostrar_detallado = item.MostrarDetallado  # =?
        item_obj.es_favorito = item.EsFavorito  # =?
        item_obj.control_lotes = item.ControlLotes
        item_obj.tiene_impuesto_bolsa = item.TieneImpuestoBolsa  # ?
        item_obj.subtotal = item.SubTotal
        item_obj.total = item.Total
        item_obj.precio_unitario_venta = item.PrecioUnitarioVenta
        item_obj.save()

    for parametro in generar.ListaParametro:
        docuemento_parametro = DocumentoParametro()
        docuemento_parametro.idparametro = parametro.IdParametro
        docuemento_parametro.iddominio = parametro.IdDominio
        docuemento_parametro.valor = parametro.Valor
        docuemento_parametro.tipo = parametro.Tipo
        docuemento_parametro.auxiliar1 = parametro.Auxiliar1
        docuemento_parametro.auxiliar2 = parametro.Auxiliar2
        docuemento_parametro.auxiliar3 = parametro.Auxiliar3
        docuemento_parametro.save()

    print("amoorsote")
    print(len(generar.ListaEntidades))
    for entidad in generar.ListaEntidades:
        entidad_obj = DocumentoEntidad()
        #entidad_obj.es_manual = entidad.EsManual
        entidad_obj.identidad = entidad.IdEntidad
        # ? tal vez esta con diferente nombre
        entidad_obj.tipo_entidad = entidad.TipoEntidad
        entidad_obj.numero_documento = entidad.NumeroDocumento
        entidad_obj.razon_social = entidad.RazonSocial
        entidad_obj.correo_electronico = entidad.CorreoEntidad
        entidad_obj.tipo_documento = entidad.TipoDocumentoDescripcion
        entidad_obj.direccion = entidad.Direccion
        entidad_obj.save()
    #documento_contable.r = generar.ReceptorCorreo

    #serie.descripcion = generar.SerieDescripcion
    """SumaDescuentosAfectanBase: 4.24
    SumaDescuentosNoAfectanBase: -0.0031578899999997745
    SumatoriaIcbper: 0"""

    generar_pdf.save()
    # serie.save()
    base64_response = generar_comprobante(generar)
    generar_pdf.correlativo = '1'
    return HttpResponse(base64_response, content_type='application/json')


@api_view(['GET'])
def getSeries(request, listaTiposDocumentos, tipoSerie):
    """listaTiposDocumentos = request.query_params['listaTiposDocumentos'][0]"""
    print(listaTiposDocumentos)
    print(tipoSerie)
    headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2MDM3MzJFMzIyN0MwN0JFOEQwQUJENDcyRjM4NTBBOEYzNDRFRkQiLCJ0eXAiOiJKV1QiLCJ4NWMiOlsibXNzZWd1cmlkYWQiLCJERU1PLVBWTEciXX0.eyJuYmYiOjE2MzI5Mzk4MzUsImV4cCI6MTYzNTUzMTU5NSwiaXNzIjoibXNzZWd1cmlkYWQiLCJhdWQiOiJiMjJjNDA3NmU3MWY0ZDBlYTYxODhhNjQ4Zjc3ZDAxZCIsInNjb3BlcyI6eyJJZFVzdWFyaW8iOjQwMjEyLCJVc3VhcmlvIjoiZGVtby1wdmxnIiwiVGlwb1Rva2VuIjoxLCJJZEVudGlkYWRQZXJzb25hIjoxLCJJZEVudGlkYWRFbXByZXNhIjo2MDAxNiwiRG9jdW1lbnRvRW1wcmVzYSI6IjAwMDAwMDAwMDAwIiwiRG9jdW1lbnRvUGVyc29uYSI6IjQzMDk0NTM2IiwiU3VjdXJzYWxlcyI6WzIwLDIxXSwiU2VydmljaW9zIjpbMSwyLDMsNCw1LDYsNyw4LDksMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTksMjAsMjEsMjIsMjMsMjQsMjUsMjYsMjcsMjgsMjksMzAsMzEsMzIsMzMsMzQsMzUsMzYsMzcsMzgsMzksNDAsNDEsNDIsNDMsNDQsNDUsNDYsNDcsNDgsNDksNTAsNTEsNTIsNTMsNTQsNTUsNTYsNTcsNTgsNTksNjAsNjEsNjIsNjMsNjQsNjUsNjYsNjcsNjgsNjksNzAsNzEsNzIsNzMsNzQsNzUsNzYsNzcsNzgsNzksODAsODEsODIsODMsODUsODYsODcsODgsODksOTAsOTEsOTIsOTMsOTQsOTUsOTYsOTcsOTgsOTksMTAwLDEwMSwxMDIsMTAzLDEwNCwxMDUsMTA2LDEwNywxMDgsMTA5LDExMCwxMTEsMTEyLDExMywxMTQsMTE1LDExNiwxMTcsMTE4LDExOSwxMjAsMTIxLDEyMiwxMjMsMTI0LDEyNSwxMjYsMTI3LDEyOCwxMjksMTMwLDEzMSwxMzIsMTMzLDEzNCwxMzUsMTM2LDEzNywxMzgsMTM5LDE0MCwxNDEsMTQyLDE0MywxNDQsMTQ1LDE0NiwxNDcsMTQ4LDE0OSwxNTAsMTUxLDE1MiwxNTMsMTU0LDE1NSwxNTYsMTU3LDE1OCwxNjAsMTY1LDE3NywxNzgsMTc5LDE4MSwyMTcsMjE4LDIxOSwyMjIsMjIzLDIzMiwyNzQsMjgxLDI4OCwyODksMzYyLDM3MiwzODEsMzg1LDM4NiwzODcsMzg4LDM4OSwzOTAsMzkxLDM5MiwzOTMsMzk0LDM5NSw0NTEsNDY3LDQ2OCw0NjksNDcwLDUwMCw1MDEsNTAyLDUwMyw1MDQsNTA1LDUwNiw1MDcsNTA4LDUwOSw1MTAsNTExLDUxMiw1MTMsNTE0LDUxNSw1MTYsNTE3LDE3NiwxODAsMTg1LDE2MSwxOTEsMTkyLDIzMywyMzQsMTY2LDE2NywxNjgsMTY5LDE3MCwxNzEsMTcyLDE3MywxNzQsMTc1LDE4MywyMDksMTU5LDE2MiwxNjMsMTY0LDE4NCwyMjcsMjc1LDI3NiwzNTksMzYwLDM2MSwzNzUsMzc2LDg0LDE4MiwxODYsMTg3LDE4OCwxODksMTkwLDE5MywxOTQsMTk1LDE5NiwxOTcsMTk4LDE5OSwyMDAsMjAxLDIwMiwyMDMsMjA0LDIwNSwyMDYsMjA3LDIwOCwyMTAsMjExLDIxMiwyMTMsMjE0LDIxNSwyMTYsMjIwLDIyMSwyMjQsMjI1LDIyNiwyMjgsMjI5LDIzMCwyMzEsMjM1LDIzNiwyMzcsMjM4LDIzOSwyNDAsMjQxLDI0MiwyNDMsMjQ0LDI0NSwyNDYsMjQ3LDI0OCwyNDksMjUwLDI1MSwyNTIsMjUzLDI1NCwyNTUsMjU2LDI1NywyNTgsMjU5LDI2MCwyNjEsMjYyLDI2MywzMjcsMzI4LDI2NCwyNjUsMjY2LDI2NywyNjgsMjY5LDI3MCwyNzEsMjcyLDM1NywzNTgsMjczLDI4NCwyODUsMjg2LDMxOSwzMjAsMzIxLDMyMiwzMjMsMzI0LDMyNSwzMjYsMzI5LDMzMCwzMTcsMzE4LDI3NywyOTAsMzEwLDMxMSwzMTIsMzE1LDMxNiwzMzksMzQzLDM0NCwzNDYsMzQ3LDM1MywzNzcsNDIzLDQyNCw0MjksNDMwLDQzMiw0MzMsNDM0LDQzNSw0MzYsNDQ2LDQ0Nyw0NDgsNDQ5LDQ1MCw0MTksNDIwLDQyMSw0MjIsNDI1LDQyNiw0MjcsNDI4LDQzMSw0MzcsNDM4LDQzOSw0NDAsNDQxLDQ0Miw0NDMsNDQ0LDQ0NSwzOTgsMzk5LDQ1Miw0NTMsNDU0LDQ1NSw0NTYsNDU3LDQ1OCw0NTksNDYwLDQ2MV19fQ.fhFnbff56O4DJLoGCV0F4LQGcOjouQnz_49dvZIkuSy6yl-ke6Zof9xKr6joSZpq5ASSLsE0wbrA1ZIe4KvFLj0JzsnOLuB1JYNuzgSR6o3sFPDWNBalg4IQfg_K_zGYndLRF7OpOdGfW-d4yVIEdwIKRAJvMttfirypwa9XpQ7JOjyZ__115OWxTkgl9NQiuCOI62VOGFx1z9cndxsVqusI6GayGk2JRn0iFkTfROWDh_WWhVYYPhmXRZZQtk_mlMRXx2I-WPmcz0vRdkp9rQCUIOJLyPDn2gH8PqlsOZGdB_H2Cd01pMBVMgpfN04Ed3_hu-L-Xz85hMJDdF_YgA'}
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'entidades/series?listaTiposDocumentos=' + listaTiposDocumentos + '&tipoSerie=' + tipoSerie, headers=headers)
    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def generarArchivo(request, id, tipo, v):
    pdftob64 = PdfToBase64(Nombre='00000000000/B003-00001296-633496-PDF.PDF',
                           NumeroDocumentoEmisor='000000000000',     Base64=toBase64())
    print("toJson")
    var = pdftob64.json()
    return HttpResponse(var, content_type='application/json')
    # return Response(json.loads(var),  status=status.HTTP_201_CREATED)


@api_view(['POST'])
def emitir(request, v):
    data = request.data
    generar = GenerarDocumento(**data)
    """ 
    Tipo Documento
    1003 -> Factura
    1004 -> Boleta venta
    1005 -> nota de credito
    1006 -> nota de debito
    1007 -> guia de remision 
    Boleta
     """
    response = requests.post(
        URL_MSFACTURACIONCMD+'documentoContable', data=json.dumps(data), headers=headers)
    if response.status_code >= 500:
        return response

    if generar.IdTipoDocumento == 1004:
        generar_comprobante(generar)
    pdftob64 = PdfToBase64(Nombre='00000000000/B003-00001296-633496-PDF.PDF',
                           NumeroDocumentoEmisor='000000000000',     Base64=toBase64())

    var = pdftob64.json()
    return HttpResponse(var, content_type='application/json')


@api_view(['GET'])
def parametros(request, idParametro, tipo, estado):
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'parametros?idParametro=' + idParametro + '&tipo=' + tipo + '&estado='+estado, headers=headers)

    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def datosAdicionalesFE(request, listaTiposDocumentos, tipoSerie):
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'entidades/series?listaTiposDocumentos=' + listaTiposDocumentos + '&tipoSerie='+tipoSerie, headers=headers)
    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def parametrosget(request, v):

    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'parametros?idParametro=' + request.GET['idparametro'] + '&estado='+request.GET['estado'], headers=headers)
    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def getPagosSeries(request, v):
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'entidades/series?listaTiposDocumentos=' + request.GET['listaTiposDocumentos'] + '&tipoSerie=' + request.GET['tipoSerie'], headers=headers)
    return JsonResponse(response.json(), safe=False)


@api_view(['GET'])
def get_moneda(request, v):
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'moneda?estados=' + request.GET['estados'], headers=headers)

    return JsonResponse(response.json(), safe=False)


@api_view(['POST'])
def buscar_documento_contable(request, v):
    data = request.data
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'buscar', data=json.dumps(data), headers=headers)

    return JsonResponse(response.json(), safe=False)


""" Contenidos """


@api_view(['GET'])
def plantilla_html(request, v):
    data = request.data
    response = requests.get(
        settings.URL_MSFACTURACIONQRY + 'documentoContable/plantilla/html?idEntidadEmisor='+request.GET['idEntidadEmisor']+'&tipoDocumentoCodigo='+request.GET['tipoDocumentoCodigo']+'&IdTipoNota='+request.GET['IdTipoNota'], data=json.dumps(data), headers=headers)
    html_pdf = str(response.content)
    remplazo = html_pdf.replace('\\n', '')

    Html_file = open("plan.html", "w")
    Html_file.write(html_pdf)
    Html_file.close()

    """ respuesta = render(request, "Home.html", {
                       'plantilla': remplazo}, content_type='application/xhtml+xml')

    print(html.unescape(str(respuesta.content))) """

    compiler = Compiler()

    # Compile the template
    source = u"{{{header}}}"
    template = compiler.compile(source)

    # Add any special helpers
    def _list(this, options, items):
        result = [u'<ul>']
        for thing in items:
            result.append(u'<li>')
            result.extend(options['fn'](thing))
            result.append(u'</li>')
        result.append(u'</ul>')
        return result
    helpers = {'list': _list}

    # Add partials
    header = compiler.compile(u'<h1>People</h1>')
    partials = {'header': header}

    # Render the template
    output = template({
        'people': [
            {'firstName': "Yehuda", 'lastName': "Katz"},
            {'firstName': "Carl", 'lastName': "Lerche"},
            {'firstName': "Alan", 'lastName': "Johnson"}
        ]}, helpers=helpers, partials=partials)

    print(output)
    return Response(str(output))
