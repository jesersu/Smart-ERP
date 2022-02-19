from django.shortcuts import render
from . import models
from entidades import models as dtos
import threading
# Declraing a lock
lock = threading.Lock()
# Create your views here.


def getTiposDocumento():
    res = []
    models.Serie.objects.using('erpquery').update()
    for td in models.TipoDocumento.objects.using('erpquery').all():
        dto = dtos.TipoDocumentoDto()
        dto.Id = td.idtipo_documento
        dto.Codigo = td.codigo
        dto.Tipo = td.tipo
        dto.Descripcion = td.descripcion
        dto.Abreviacion = td.abreviacion
        dto.LogUserCrea = td.log_usuariocreacion
        dto.LogDateCrea = td.log_fechacreacion
        dto.LogUserModif = td.log_usuariomodif
        dto.LogDateModif = td.log_fechamodif
        dto.LogEstado = td.log_estado
        res.append(dto)
    return res


def getCorrelativoContabilidad(id):
    lock.acquire()
    myserie = models.SerieContabilidad.objects.using(
        'srcontabilidad').get(idserie=id)
    models.SerieContabilidad.objects.using('srcontabilidad').filter(
        idserie=id).update(correlativo=myserie.correlativo + 1)
    lock.release()
    return myserie


def getCorrelativoFinanzas(id):
    lock.acquire()
    myserie = models.SerieFinanzas.objects.using(
        'srfinanzas').get(IdSerie=id)
    models.SerieFinanzas.objects.using('srfinanzas').filter(
        IdSerie=id).update(Correlativo=myserie.Correlativo + 1)
    lock.release()
    return myserie


def getCorrelativoLogistica(id):
    lock.acquire()
    myserie = models.SerieLogistica.objects.using(
        'srlogistica').get(IdSerie=id)
    models.SerieLogistica.objects.using('srlogistica').filter(
        IdSerie=id).update(Correlativo=myserie.Correlativo + 1)
    lock.release()
    return myserie
