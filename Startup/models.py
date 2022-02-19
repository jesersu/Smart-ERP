""" bdProxy models"""

from django.db import models


class TipoDocumento2(models.Model):
    Id = models.AutoField(primary_key=True)
    Codigo = models.CharField(max_length=100, blank=True)
    Descripcion = models.CharField(max_length=100, blank=True)
    Tipo = models.CharField(max_length=100, blank=True)
    Abreviacion = models.CharField(max_length=100, blank=True)
    LogUsuariocrea = models.CharField(max_length=100, blank=True)
    LogFechacrea = models.DateTimeField(auto_now_add=True)
    LogUsuariomodif = models.CharField(max_length=100, blank=True)
    LogFechamodif = models.DateTimeField(auto_now=True)
    LogEstado = models.SmallIntegerField(blank=True)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'tipo_documento2'
