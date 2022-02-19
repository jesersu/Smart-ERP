# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class GenerarComprobante(models.Model):
    iddocumentocontable = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    idcentro_costos = models.IntegerField(blank=True, null=True)
    idtipo_documento = models.IntegerField(blank=True, null=True)
    idestado = models.IntegerField(blank=True, null=True)
    idestadosunat = models.IntegerField(blank=True, null=True)
    idmoneda = models.IntegerField(blank=True, null=True)
    idcondicion_pago = models.IntegerField(blank=True, null=True)
    id_serie = models.IntegerField(blank=True, null=True)
    serie_compras = models.CharField(max_length=100, blank=True, null=True)
    idempresa = models.IntegerField(blank=True, null=True)
    tipo_operacion = models.IntegerField(blank=True, null=True)
    numero_documento = models.BigIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    id_origen = models.CharField(max_length=100, blank=True, null=True)
    codigo_pedido = models.CharField(max_length=100, blank=True, null=True)
    serie_pedido = models.CharField(max_length=100, blank=True, null=True)
    id_modulo = models.BigIntegerField(blank=True, null=True)
    identidad_emisor = models.BigIntegerField(blank=True, null=True)
    identidad_receptora = models.BigIntegerField(blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_subtotal = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_igv = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_total = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    monto_total_desc = models.CharField(max_length=100, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    valorigv = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    fecha_emision = models.DateTimeField(blank=True, null=True)
    fecha_anulacion = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    otros_tributos = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    otros_cargos = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField(blank=True, null=True)
    log_usuariomodif = models.CharField(max_length=100, blank=True, null=True)
    log_fechamodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_isc = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total_precio_venta = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    peso_bruto = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    peso_neto = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    montoAnticipo = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    montoDescuento = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    monto_igv_gratuito = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    numero_contrato = models.IntegerField(blank=True, null=True)
    operaciones_exoneradas = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    operaciones_exportadas = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    operaciones_gratuitas = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    operaciones_gravadas = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    operaciones_inafectas = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    otros_cargos_sumatoria = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    receptor_correo = models.CharField(max_length=100, blank=True, null=True)
    receptor_numero_documento = models.CharField(
        max_length=100, blank=True, null=True)
    receptor_razon_social = models.CharField(
        max_length=100, blank=True, null=True)
    receptor_tipo_documento = models.CharField(
        max_length=100, blank=True, null=True)

    suma_descuentos_afectan_base = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    suma_descuentos_no_afectan_base = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    receptor_numero_documento = models.CharField(
        max_length=100, blank=True, null=True)
    receptor_razon_social = models.CharField(
        max_length=100, blank=True, null=True)
    receptor_tipo_documento = models.CharField(
        max_length=100, blank=True, null=True)

    descripcion = models.CharField(
        max_length=100, blank=True, null=True)

    suma_descuentos_afectan_base = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    suma_descuentos_no_afectan_base = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    sumatoriaIcbper = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    correlativo = models.CharField(
        max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'generar_comprobante'


class Asiento(models.Model):
    idasiento = models.AutoField(primary_key=True)
    idperiodo = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    idmoduloorigen = models.IntegerField()
    iddetalleorigen = models.BigIntegerField()
    iddocumentoorigen = models.BigIntegerField()
    codigo = models.CharField(max_length=100)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'asiento'


class AsientoTipo(models.Model):
    idasiento_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    identidad = models.BigIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'asiento_tipo'


class Concepto(models.Model):
    idconcepto = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacio = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'concepto'


class CondicionEntidad(models.Model):
    id = models.AutoField(primary_key=True)
    idcondicion_pago = models.IntegerField()
    identidad = models.BigIntegerField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'condicion_entidad'


class CondicionPago(models.Model):
    idcondicion_pago = models.AutoField(primary_key=True)
    condicion_pago = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipo = models.SmallIntegerField()
    tiempodias = models.IntegerField()
    nrocuotas = models.IntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'condicion_pago'


class CuentaContable(models.Model):
    idcuenta_contable = models.AutoField(primary_key=True)
    idplan_cuenta = models.IntegerField()
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    idpadre = models.IntegerField(blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    idtipocuenta = models.IntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'cuenta_contable'


class CuentaContableParametro(models.Model):
    idcuenta_contable_parametro = models.AutoField(primary_key=True)
    idparametro = models.IntegerField()
    idcuenta_contable = models.IntegerField()
    tipo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'cuenta_contable_parametro'


class Cuentaparticular(models.Model):
    idcuentaparticular = models.AutoField(primary_key=True)
    identidad = models.BigIntegerField()
    idcuentapadre = models.IntegerField()
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    idpadre = models.IntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'cuentaparticular'


class Cuentareporte(models.Model):
    idcuentaentidad = models.AutoField(primary_key=True)
    idplantillareporte = models.IntegerField()
    idparametro = models.IntegerField()
    idcuenta_contable = models.IntegerField()
    tipo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100, blank=True, null=True)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'cuentareporte'


class DetalleAdicional(models.Model):
    iddetalle_adicional = models.AutoField(primary_key=True)
    iddocumentocontable = models.BigIntegerField()
    tipo_adicional = models.IntegerField()
    # Field name made lowercase.
    descripcion = models.CharField(max_length=100, db_column='Descripcion')
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        max_length=100, db_column='Auxiliar1', blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        max_length=100, db_column='Auxiliar2', blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        max_length=100, db_column='Auxiliar3', blank=True, null=True)
    # Field name made lowercase.
    auxiliar4 = models.CharField(
        max_length=100, db_column='Auxiliar4', blank=True, null=True)
    # Field name made lowercase.
    auxiliar5 = models.CharField(
        max_length=100, db_column='Auxiliar5', blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'detalle_adicional'


class DetalleAsiento(models.Model):
    iddetalle_asiento = models.AutoField(primary_key=True)
    idasiento = models.IntegerField()
    idcuenta_contable = models.IntegerField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipo = models.SmallIntegerField()
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    valor = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'detalle_asiento'


class DetalleAsientoTipo(models.Model):
    iddetalle_asiento_tipo = models.AutoField(primary_key=True)
    idcuenta_contable = models.IntegerField()
    idasiento_tipo = models.IntegerField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipo = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'detalle_asiento_tipo'


class DetalleDocumento(models.Model):
    iddetalledocumento = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    iddocumentocontable = models.BigIntegerField(blank=True, null=True)
    item = models.IntegerField(blank=True, null=True)
    id_referencia = models.BigIntegerField(blank=True, null=True)
    descripcion_item = models.CharField(max_length=100)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    valor_unitario = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    precio_unitario_venta = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    precio_unitario = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    codigo_unidad = models.CharField(max_length=100, blank=True, null=True)
    descripcion_unidad = models.CharField(
        max_length=100, blank=True, null=True)
    id_almacen = models.BigIntegerField(blank=True, null=True)
    id_unidad = models.BigIntegerField(blank=True, null=True)
    id_inventario = models.BigIntegerField(blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    cantidad = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_isc = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_igv = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    descuento = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    valorigv = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    codigo_item = models.CharField(max_length=100, blank=True, null=True)
    codigo_sunat = models.CharField(max_length=100, blank=True, null=True)
    idmsorigen = models.BigIntegerField(blank=True, null=True)
    id_origen = models.CharField(max_length=100)
    iddetalleorigen = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField(auto_now_add=True)
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField(auto_now=True)
    log_estado = models.SmallIntegerField(default=1)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    precio_venta_item = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    peso_bruto = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    peso_neto = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    codigo_lote = models.CharField(max_length=100, blank=True, null=True)
    id_lote = models.BigIntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)

    id_tipo_afectacion_igv = models.SmallIntegerField(blank=True, null=True)
    id_tipo_precio_venta_unitario = models.SmallIntegerField(
        blank=True, null=True)
    id_moneda = models.SmallIntegerField(blank=True, null=True)
    codigo_barras = models.CharField(max_length=100, blank=True, null=True)
    igv_afectado = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    otros_cargos_item = models.CharField(max_length=100, blank=True, null=True)
    otros_tributos = models.CharField(max_length=100, blank=True, null=True)
    descuento_porcentaje = models.SmallIntegerField(blank=True, null=True)
    descuento_precio = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    valor_venta = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    igv = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    stock = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    icbper = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    nombre_marca = models.CharField(max_length=100, blank=True, null=True)
    tipo_item = models.SmallIntegerField(blank=True, null=True)
    es_de_lista = models.SmallIntegerField(blank=True, null=True)
    precio_base = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    url_imagen = models.CharField(max_length=100, blank=True, null=True)
    controlar_stock = models.SmallIntegerField(blank=True, null=True)
    mostrar_detallado = models.CharField(max_length=100, blank=True, null=True)
    es_favorito = models.SmallIntegerField(blank=True, null=True)
    control_lotes = models.SmallIntegerField(blank=True, null=True)
    tiene_impuesto_bolsa = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'detalle_documento'


class DetalleValidacion(models.Model):
    iddetalle_validacion = models.AutoField(primary_key=True)
    iddocumentoarchivo = models.BigIntegerField()
    registro_numero = models.IntegerField(blank=True, null=True)
    descripcion_documento = models.CharField(
        max_length=100, blank=True, null=True)
    nombre_campo = models.CharField(max_length=100)
    codigo_error = models.CharField(max_length=100)
    descripcion_validacion = models.CharField(
        max_length=100, blank=True, null=True)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipo = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'detalle_validacion'


class DetalledocumentoParametro(models.Model):
    iddetalledocumentoparametro = models.AutoField(primary_key=True)
    iddetalledocumento = models.BigIntegerField(blank=True, null=True)
    idparametro = models.IntegerField(blank=True, null=True)
    iddominio = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField(auto_now_add=True)
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField(auto_now=True)
    log_estado = models.SmallIntegerField(default=1)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'detalledocumento_parametro'


class DocumentoArchivo(models.Model):
    iddocumentoarchivo = models.AutoField(primary_key=True)
    iddocumentocontable = models.BigIntegerField()
    archivo = models.CharField(max_length=100)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    tipoarchivo = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_archivo'


class DocumentoConcepto(models.Model):
    iddocumentoconcepto = models.AutoField(primary_key=True)
    iddocumentocontable = models.BigIntegerField()
    idconcepto = models.IntegerField()
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    valor_concepto = models.DecimalField(max_digits=10, decimal_places=5)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_concepto'


class DocumentoContable(models.Model):
    iddocumentocontable = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    idcentro_costos = models.IntegerField(blank=True, null=True)
    idtipo_documento = models.IntegerField()
    idestado = models.IntegerField()
    idestadosunat = models.IntegerField(blank=True, null=True)
    idmoneda = models.IntegerField()
    idcondicion_pago = models.IntegerField()
    id_serie = models.IntegerField()
    serie_compras = models.CharField(max_length=100, blank=True, null=True)
    idempresa = models.IntegerField()
    tipo_operacion = models.IntegerField()
    numero_documento = models.BigIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    id_origen = models.CharField(max_length=100, blank=True, null=True)
    codigo_pedido = models.CharField(max_length=100, blank=True, null=True)
    serie_pedido = models.CharField(max_length=100, blank=True, null=True)
    id_modulo = models.BigIntegerField(blank=True, null=True)
    identidad_emisor = models.BigIntegerField()
    identidad_receptora = models.BigIntegerField(blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_subtotal = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_igv = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_total = models.DecimalField(max_digits=10, decimal_places=5)
    monto_total_desc = models.CharField(max_length=100, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    valorigv = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    fecha_emision = models.DateTimeField(blank=True, null=True)
    fecha_anulacion = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    otros_tributos = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    otros_cargos = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_isc = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total_precio_venta = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    peso_bruto = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    peso_neto = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_contable'


class DocumentoEntidad(models.Model):
    iddocumentoentidad = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    iddocumentocontable = models.BigIntegerField(blank=True, null=True)
    identidad = models.BigIntegerField(blank=True, null=True)
    idtipoentidad = models.IntegerField(blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField(auto_now_add=True)
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField(auto_now=True)
    log_estado = models.SmallIntegerField(default=1)
    numero_documento = models.CharField(max_length=100, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    tipo_documento = models.CharField(max_length=100, blank=True, null=True)
    idcliente = models.IntegerField(blank=True, null=True)
    idtipo_documento = models.IntegerField(blank=True, null=True)
    correo_electronico = models.CharField(
        max_length=100, blank=True, null=True)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    tipo_entidad = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_entidad'


class DocumentoEvento(models.Model):
    id_documento_evento = models.AutoField(primary_key=True)
    id_evento = models.SmallIntegerField()
    id_documentocontable = models.BigIntegerField()
    observacion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_evento'


class DocumentoParametro(models.Model):
    iddocumentoparametro = models.AutoField(primary_key=True)
    iddocumentocontable = models.BigIntegerField(blank=True, null=True)
    idparametro = models.IntegerField(blank=True, null=True)
    iddominio = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField(auto_now_add=True)
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField(auto_now=True)
    log_estado = models.SmallIntegerField(default=1)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_parametro'


class DocumentoReferencia(models.Model):
    iddocumentoreferencia = models.AutoField(primary_key=True)
    iddocumentoorigen = models.BigIntegerField()
    iddocumentodestino = models.BigIntegerField()
    idtipo_documento_origen = models.IntegerField()
    codigo_tipo_documento_origen = models.CharField(max_length=100)
    desc_tipo_documento_origen = models.CharField(max_length=100)
    id_serie_origen = models.IntegerField()
    serie_origen = models.CharField(max_length=100)
    correlativo_origen = models.BigIntegerField()
    idtipo_documento_destinmo = models.IntegerField()
    codigo_tipo_documento_destino = models.CharField(max_length=100)
    des_tipo_documento_destino = models.CharField(max_length=100)
    id_serie_destino = models.IntegerField()
    serie_destino = models.CharField(max_length=100)
    correlativo_destino = models.BigIntegerField()
    fecha_emision_destino = models.DateTimeField(blank=True, null=True)
    # This field type is a guess.
    es_anicipo = models.TextField(blank=True, null=True)
    moneda_destino = models.CharField(max_length=100, blank=True, null=True)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    monto_anticipo = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    auxiliar_1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar_2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar_3 = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'documento_referencia'


class Dominio(models.Model):
    iddominio = models.AutoField(primary_key=True)
    idparametro = models.IntegerField()
    codigo_sunat = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'dominio'


class Entidad(models.Model):
    identidad = models.AutoField(primary_key=True)
    idtipo_documento_identidad = models.IntegerField(blank=True, null=True)
    codigo_tipo_documento_sunat = models.CharField(
        max_length=100, blank=True, null=True)
    tipo_documento_descripcion = models.CharField(
        max_length=100, blank=True, null=True)
    numero_documento = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    correo_electronico = models.CharField(
        max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    codigo_ubigeo = models.CharField(max_length=100)
    descripcion_ubigeo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'entidad'


class EntidadParametro(models.Model):
    identidad_parametro = models.AutoField(primary_key=True)
    identidad = models.BigIntegerField()
    idparametro = models.IntegerField()
    iddominio = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    auxiliar1 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=100, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'entidad_parametro'


class EntidadTipodocumento(models.Model):
    entidad = models.AutoField(primary_key=True)
    idtipodocumento = models.IntegerField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'entidad_tipodocumento'


class Equivalenciacuenta(models.Model):
    idequivalenciacuenta = models.AutoField(primary_key=True)
    idcuentasrc = models.IntegerField()
    idcuentadst = models.IntegerField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'equivalenciacuenta'


class ErrorValidacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipo = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'error_validacion'


class Estado(models.Model):
    idestado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    idmodulo = models.IntegerField(blank=True, null=True)
    abreviacion = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'estado'


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'evento'


class Moneda(models.Model):
    idmoneda = models.AutoField(primary_key=True)
    codigo_moneda = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    abreviacion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'moneda'


class Parametro(models.Model):
    parametros = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'parametro'


class Periodo(models.Model):
    idperiodo = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    identidad = models.BigIntegerField()
    codigo = models.CharField(max_length=100)
    anho = models.IntegerField()
    mes = models.IntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'periodo'


class PlanCuenta(models.Model):
    idplan_cuenta = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'plan_cuenta'


class Plantillareporte(models.Model):
    idplantillareporte = models.AutoField(primary_key=True)
    identidad = models.BigIntegerField()
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'plantillareporte'


class Serie(models.Model):
    idserie = models.AutoField(primary_key=True)
    identidad = models.BigIntegerField()
    idtipo_documento = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    abreviacion = models.CharField(max_length=100, blank=True, null=True)
    correlativo = models.BigIntegerField(blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipo_serie = models.IntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'serie'


class SerieSucursal(models.Model):
    idseriesucursal = models.AutoField(primary_key=True)
    idserie = models.IntegerField()
    idsucursal = models.IntegerField()
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'serie_sucursal'


class Sincronizacion(models.Model):
    idsincronizacion = models.AutoField(primary_key=True)
    idmodulo = models.IntegerField()
    nombre_proc = models.CharField(max_length=100)

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'sincronizacion'


class Sucursal(models.Model):
    idsucursal = models.AutoField(primary_key=True)
    identidad = models.BigIntegerField()
    direccion = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=100, blank=True, null=True)
    codigosunat = models.CharField(max_length=100, blank=True, null=True)
    ubigeo = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodifi = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'sucursal'


class TipoDocumento(models.Model):
    idtipo_documento = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    abreviacion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'tipo_documento'


class TipoEntidad(models.Model):
    idtipoentidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'tipo_entidad'


class Tipocuenta(models.Model):
    idtipocuenta = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    log_usuariocreacion = models.CharField(max_length=100)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=100)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'contabilidad'
        managed = True
        db_table = 'tipocuenta'

