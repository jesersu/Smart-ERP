# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Detalleadicional(models.Model):
    # Field name made lowercase.
    iddetalleadicional = models.BigIntegerField(
        db_column='IdDetalleAdicional', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    # Field name made lowercase.
    tipoadicional = models.IntegerField(db_column='TipoAdicional')
    # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250)
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        db_column='Auxiliar1', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        db_column='Auxiliar2', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        db_column='Auxiliar3', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar4 = models.CharField(
        db_column='Auxiliar4', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar5 = models.CharField(
        db_column='Auxiliar5', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'DetalleAdicional'


class Detalledocumento(models.Model):
    # Field name made lowercase.
    iddetalledocumento = models.BigIntegerField(
        db_column='IdDetalleDocumento', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    item = models.IntegerField(db_column='Item')  # Field name made lowercase.
    # Field name made lowercase.
    idreferencia = models.BigIntegerField(
        db_column='IdReferencia', blank=True, null=True)
    # Field name made lowercase.
    descripcionitem = models.CharField(
        db_column='DescripcionItem', max_length=5000)
    # Field name made lowercase.
    preciounitarioventa = models.DecimalField(
        db_column='PrecioUnitarioVenta', max_digits=20, decimal_places=8, blank=True, null=True)
    # Field name made lowercase.
    preciounitario = models.DecimalField(
        db_column='PrecioUnitario', max_digits=20, decimal_places=8, blank=True, null=True)
    # Field name made lowercase.
    codigounidad = models.CharField(
        db_column='CodigoUnidad', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    descripcionunidad = models.CharField(
        db_column='DescripcionUnidad', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    idalmacen = models.BigIntegerField(
        db_column='IdAlmacen', blank=True, null=True)
    # Field name made lowercase.
    idunidad = models.BigIntegerField(
        db_column='IdUnidad', blank=True, null=True)
    # Field name made lowercase.
    idinventario = models.BigIntegerField(
        db_column='IdInventario', blank=True, null=True)
    # Field name made lowercase.
    cantidad = models.DecimalField(
        db_column='Cantidad', max_digits=20, decimal_places=8, blank=True, null=True)
    # Field name made lowercase.
    subtotal = models.DecimalField(
        db_column='SubTotal', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    montoisc = models.DecimalField(
        db_column='MontoIsc', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    montoigv = models.DecimalField(
        db_column='MontoIgv', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    descuento = models.DecimalField(
        db_column='Descuento', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    valorigv = models.DecimalField(
        db_column='ValorIgv', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    codigoitem = models.CharField(
        db_column='CodigoItem', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    idmsorigen = models.BigIntegerField(db_column='IdMsOrigen')
    # Field name made lowercase.
    idorigen = models.CharField(db_column='IdOrigen', max_length=50)
    # Field name made lowercase.
    iddetalleorigen = models.CharField(
        db_column='IdDetalleOrigen', max_length=50)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)
    # Field name made lowercase.
    valorunitario = models.DecimalField(
        db_column='ValorUnitario', max_digits=20, decimal_places=8, blank=True, null=True)
    # Field name made lowercase.
    total = models.DecimalField(
        db_column='Total', max_digits=20, decimal_places=8, blank=True, null=True)
    # Field name made lowercase.
    precioventaitem = models.DecimalField(
        db_column='PrecioVentaItem', max_digits=20, decimal_places=8, blank=True, null=True)
    # Field name made lowercase.
    codigosunat = models.CharField(
        db_column='CodigoSunat', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    pesobruto = models.DecimalField(
        db_column='PesoBruto', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    pesoneto = models.DecimalField(
        db_column='PesoNeto', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    codigolote = models.CharField(
        db_column='CodigoLote', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    idlote = models.BigIntegerField(db_column='IdLote', blank=True, null=True)
    # Field name made lowercase.
    fechavencimiento = models.DateTimeField(
        db_column='FechaVencimiento', blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'DetalleDocumento'


class Detalledocumentoparametro(models.Model):
    iddetalledocumentoparametro = models.BigIntegerField(
        db_column='IdDetalleDocumentoParametro', primary_key=True)  # Field name made lowercase.
    # Field name made lowercase.
    iddetalledocumento = models.BigIntegerField(db_column='IdDetalleDocumento')
    # Field name made lowercase.
    idparametro = models.IntegerField(db_column='Idparametro')
    # Field name made lowercase.
    iddominio = models.IntegerField(db_column='IdDominio')
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20)
    # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=20)
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        db_column='Auxiliar1', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        db_column='Auxiliar2', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        db_column='Auxiliar3', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleDocumentoParametro'


class Documentoarchivo(models.Model):
    # Field name made lowercase.
    iddocumentoarchivo = models.BigIntegerField(
        db_column='IdDocumentoArchivo', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=100)
    # Field name made lowercase.
    tipoarchivo = models.CharField(db_column='TipoArchivo', max_length=3)
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        db_column='Auxiliar1', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        db_column='Auxiliar2', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        db_column='Auxiliar3', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'DocumentoArchivo'


class Documentoconcepto(models.Model):
    # Field name made lowercase.
    iddocumentoconcepto = models.BigIntegerField(
        db_column='IdDocumentoConcepto', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    # Field name made lowercase.
    idconcepto = models.IntegerField(db_column='IdConcepto')
    # Field name made lowercase.
    valorconcepto = models.DecimalField(
        db_column='ValorConcepto', max_digits=12, decimal_places=2)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)
    # Field name made lowercase.
    auxiliardec1 = models.DecimalField(
        db_column='AuxiliarDec1', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    auxiliardec2 = models.DecimalField(
        db_column='AuxiliarDec2', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    auxiliarvar1 = models.CharField(
        db_column='AuxiliarVar1', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    auxiliarvar2 = models.CharField(
        db_column='AuxiliarVar2', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocumentoConcepto'


class Documentocontable(models.Model):
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable', primary_key=True)
    # Field name made lowercase.
    idtipodocumento = models.IntegerField(
        db_column='IdTipoDocumento', blank=True, null=True)
    # Field name made lowercase.
    idcentrocostos = models.IntegerField(
        db_column='IdCentroCostos', blank=True, null=True)
    # Field name made lowercase.
    idestado = models.IntegerField(db_column='IdEstado', blank=True, null=True)
    # Field name made lowercase.
    idestadosunat = models.IntegerField(
        db_column='IdEstadoSunat', blank=True, null=True)
    # Field name made lowercase.
    idmoneda = models.IntegerField(db_column='IdMoneda', blank=True, null=True)
    # Field name made lowercase.
    idcondicionpago = models.IntegerField(
        db_column='IdCondicionPago', blank=True, null=True)
    # Field name made lowercase.
    idserie = models.IntegerField(db_column='IdSerie', blank=True, null=True)
    # Field name made lowercase.
    idempresa = models.IntegerField(
        db_column='IdEmpresa', blank=True, null=True)
    # Field name made lowercase.
    tipooperacion = models.IntegerField(
        db_column='TipoOperacion', blank=True, null=True)
    # Field name made lowercase.
    numerodocumento = models.BigIntegerField(
        db_column='NumeroDocumento', blank=True, null=True)
    # Field name made lowercase.
    numerodocumentoformateado = models.CharField(
        db_column='NumeroDocumentoFormateado', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    idorigen = models.CharField(
        db_column='IdOrigen', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    codigopedido = models.CharField(
        db_column='CodigoPedido', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    seriepedido = models.CharField(
        db_column='SeriePedido', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    idmodulo = models.BigIntegerField(
        db_column='IdModulo', blank=True, null=True)
    # Field name made lowercase.
    identidademisor = models.BigIntegerField(
        db_column='IdEntidadEmisor', blank=True, null=True)
    # Field name made lowercase.
    identidadreceptora = models.BigIntegerField(
        db_column='IdEntidadReceptora', blank=True, null=True)
    # Field name made lowercase.
    montosubtotal = models.DecimalField(
        db_column='MontoSubTotal', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    montoigv = models.DecimalField(
        db_column='MontoIgv', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    montototal = models.DecimalField(
        db_column='MontoTotal', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    valorigv = models.DecimalField(
        db_column='ValorIgv', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    fechaemision = models.DateTimeField(
        db_column='FechaEmision', blank=True, null=True)
    # Field name made lowercase.
    fechaanulacion = models.DateTimeField(
        db_column='FechaAnulacion', blank=True, null=True)
    # Field name made lowercase.
    fechavencimiento = models.DateTimeField(
        db_column='FechaVencimiento', blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)
    # Field name made lowercase.
    montoisc = models.DecimalField(
        db_column='MontoIsc', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    monedadescripcion = models.CharField(
        db_column='MonedaDescripcion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    monedaabreviacion = models.CharField(
        db_column='MonedaAbreviacion', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    monedacodigo = models.CharField(
        db_column='MonedaCodigo', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    tipodocumentocodigo = models.CharField(
        db_column='TipoDocumentoCodigo', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    tipodocumentodescripcion = models.CharField(
        db_column='TipoDocumentoDescripcion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    tipodocumentoabreviacion = models.CharField(
        db_column='TipoDocumentoAbreviacion', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    condicionpagocondicionpago = models.CharField(
        db_column='CondicionPagoCondicionPago', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    condicionpagoabreviatura = models.CharField(
        db_column='CondicionPagoAbreviatura', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    condicionpagotipo = models.SmallIntegerField(
        db_column='CondicionPagoTipo', blank=True, null=True)
    # Field name made lowercase.
    condicionpagotiempodias = models.IntegerField(
        db_column='CondicionPagoTiempoDias', blank=True, null=True)
    # Field name made lowercase.
    condicionpagonrocuotas = models.IntegerField(
        db_column='CondicionPagoNroCuotas', blank=True, null=True)
    # Field name made lowercase.
    estadodescripcion = models.CharField(
        db_column='EstadoDescripcion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    estadoidmodulo = models.IntegerField(
        db_column='EstadoIdModulo', blank=True, null=True)
    # Field name made lowercase.
    estadoabreviacion = models.CharField(
        db_column='EstadoAbreviacion', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    seriedescripcion = models.CharField(
        db_column='SerieDescripcion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    serieidentidad = models.BigIntegerField(
        db_column='SerieIdentidad', blank=True, null=True)
    # Field name made lowercase.
    serieidtipodocumento = models.IntegerField(
        db_column='SerieIdTipoDocumento', blank=True, null=True)
    # Field name made lowercase.
    serieabreviacion = models.CharField(
        db_column='SerieAbreviacion', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    seriecorrelativo = models.BigIntegerField(
        db_column='SerieCorrelativo', blank=True, null=True)
    # Field name made lowercase.
    serietiposerie = models.IntegerField(
        db_column='SerieTipoSerie', blank=True, null=True)
    # Field name made lowercase.
    serieorden = models.SmallIntegerField(
        db_column='SerieOrden', blank=True, null=True)
    # Field name made lowercase.
    observacion = models.CharField(
        db_column='Observacion', max_length=5000, blank=True, null=True)
    # Field name made lowercase.
    montototaldesc = models.CharField(
        db_column='MontoTotalDesc', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    otrostributos = models.DecimalField(
        db_column='OtrosTributos', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    seriecompras = models.CharField(
        db_column='SerieCompras', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    direccion = models.CharField(
        db_column='Direccion', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    totalprecioventa = models.DecimalField(
        db_column='TotalPrecioVenta', max_digits=13, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    pesobruto = models.DecimalField(
        db_column='PesoBruto', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    pesoneto = models.DecimalField(
        db_column='PesoNeto', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    montoigvgratuito = models.DecimalField(
        db_column='MontoIgvGratuito', max_digits=18, decimal_places=5, blank=True, null=True)
    # Field name made lowercase.
    codigoordencompra = models.CharField(
        db_column='CodigoOrdenCompra', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    numerocontrato = models.CharField(
        db_column='NumeroContrato', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    numeroguiaremision = models.CharField(
        db_column='NumeroGuiaRemision', max_length=20, blank=True, null=True)
    emisoridtipodocumentoidentidad = models.IntegerField(
        db_column='EmisorIdTipoDocumentoIdentidad', blank=True, null=True)  # Field name made lowercase.
    emisorcodigotipodocumentosunat = models.CharField(
        db_column='EmisorCodigoTipoDocumentoSunat', max_length=2, blank=True, null=True)  # Field name made lowercase.
    emisortipodocumentodescripcion = models.CharField(
        db_column='EmisorTipoDocumentoDescripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    emisornumerodocumento = models.CharField(
        db_column='EmisorNumeroDocumento', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    emisorrazonsocial = models.CharField(
        db_column='EmisorRazonSocial', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    emisorcorreoelectrico = models.CharField(
        db_column='EmisorCorreoElectrico', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    emisordireccion = models.CharField(
        db_column='EmisorDireccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    emisorcodigoubigeo = models.CharField(
        db_column='EmisorCodigoUbigeo', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    emisordescripcionubigeo = models.CharField(
        db_column='EmisorDescripcionUbigeo', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    emisortelefono = models.CharField(
        db_column='EmisorTelefono', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    sucursalidsucursal = models.IntegerField(db_column='SucursalIdSucursal')
    # Field name made lowercase.
    sucursalidentidad = models.BigIntegerField(db_column='SucursalIdEntidad')
    # Field name made lowercase.
    sucursaldireccion = models.CharField(
        db_column='SucursalDireccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    sucursalabreviatura = models.CharField(
        db_column='SucursalAbreviatura', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    sucursalcodigosunat = models.CharField(
        db_column='SucursalCodigoSunat', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    sucursalubigeo = models.CharField(
        db_column='SucursalUbigeo', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    sucursalimagen = models.CharField(
        db_column='SucursalImagen', max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'DocumentoContable'


class Documentoentidad(models.Model):
    # Field name made lowercase.
    iddocumentoentidad = models.BigIntegerField(
        db_column='IdDocumentoEntidad', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    # Field name made lowercase.
    identidad = models.BigIntegerField(db_column='IdEntidad')
    # Field name made lowercase.
    idtipoentidad = models.IntegerField(db_column='IdTipoEntidad')
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)
    # Field name made lowercase.
    numerodocumento = models.CharField(
        db_column='NumeroDocumento', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    razonsocial = models.CharField(
        db_column='RazonSocial', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    direccion = models.CharField(
        db_column='Direccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    tipodocumento = models.CharField(
        db_column='TipoDocumento', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    idcliente = models.IntegerField(
        db_column='IdCliente', blank=True, null=True)
    # Field name made lowercase.
    idtipodocumento = models.IntegerField(
        db_column='IdTipoDocumento', blank=True, null=True)
    # Field name made lowercase.
    correoelectronico = models.CharField(
        db_column='CorreoElectronico', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        db_column='Auxiliar1', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        db_column='Auxiliar2', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        db_column='Auxiliar3', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    entidadidtipodocumento = models.IntegerField(
        db_column='EntidadIdTipoDocumento', blank=True, null=True)
    entidadcodigotipodocumentosunat = models.CharField(
        db_column='EntidadCodigoTipoDocumentoSunat', max_length=2, blank=True, null=True)  # Field name made lowercase.
    entidadtipodocumentodescripcion = models.CharField(
        db_column='EntidadTipoDocumentoDescripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    entidadnumerodocumento = models.CharField(
        db_column='EntidadNumeroDocumento', max_length=20)
    # Field name made lowercase.
    entidadrazonsocial = models.CharField(
        db_column='EntidadRazonSocial', max_length=200)
    # Field name made lowercase.
    entidadcorreoelectronico = models.CharField(
        db_column='EntidadCorreoElectronico', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    entidaddireccion = models.CharField(
        db_column='EntidadDireccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    entidadcodigoubigeo = models.CharField(
        db_column='EntidadCodigoUbigeo', max_length=6)
    # Field name made lowercase.
    entidaddescripcionubigeo = models.CharField(
        db_column='EntidadDescripcionUbigeo', max_length=250)
    # Field name made lowercase.
    entidadtelefono = models.CharField(
        db_column='EntidadTelefono', max_length=30)

    class Meta:
        managed = False
        db_table = 'DocumentoEntidad'


class Documentoparametro(models.Model):
    # Field name made lowercase.
    iddocumentoparametro = models.BigIntegerField(
        db_column='IdDocumentoParametro', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    # Field name made lowercase.
    idparametro = models.IntegerField(db_column='IdParametro')
    # Field name made lowercase.
    iddominio = models.IntegerField(
        db_column='IdDominio', blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20)
    # Field name made lowercase.
    valor = models.CharField(
        db_column='Valor', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        db_column='Auxiliar1', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        db_column='Auxiliar2', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        db_column='Auxiliar3', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)
    # Field name made lowercase.
    dominioidparametro = models.IntegerField(
        db_column='DominioIdParametro', blank=True, null=True)
    # Field name made lowercase.
    dominiocodigosunat = models.CharField(
        db_column='DominioCodigoSunat', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    dominiodescripcion = models.CharField(
        db_column='DominioDescripcion', max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'DocumentoParametro'


class Documentoreferencia(models.Model):
    # Field name made lowercase.
    iddocumentoreferencia = models.BigIntegerField(
        db_column='IdDocumentoReferencia', primary_key=True)
    # Field name made lowercase.
    iddocumentoorigen = models.BigIntegerField(db_column='IdDocumentoOrigen')
    # Field name made lowercase.
    iddocumentodestino = models.BigIntegerField(db_column='IdDocumentoDestino')
    # Field name made lowercase.
    idtipodocumentoorigen = models.IntegerField(
        db_column='IdTipoDocumentoOrigen')
    # Field name made lowercase.
    codigotipodocumentoorigen = models.CharField(
        db_column='CodigoTipoDocumentoOrigen', max_length=10)
    # Field name made lowercase.
    desctipodocumentoorigen = models.CharField(
        db_column='DescTipoDocumentoOrigen', max_length=20)
    # Field name made lowercase.
    idserieorigen = models.IntegerField(db_column='IdSerieOrigen')
    # Field name made lowercase.
    serieorigen = models.CharField(db_column='SerieOrigen', max_length=4)
    # Field name made lowercase.
    correlativoorigen = models.BigIntegerField(db_column='CorrelativoOrigen')
    # Field name made lowercase.
    idtipodocumentodestino = models.IntegerField(
        db_column='IdTipoDocumentoDestino')
    # Field name made lowercase.
    codigotipodocumentodestino = models.CharField(
        db_column='CodigoTipoDocumentoDestino', max_length=10)
    # Field name made lowercase.
    destipodocumentodestino = models.CharField(
        db_column='DesTipoDocumentoDestino', max_length=20)
    # Field name made lowercase.
    idseriedestino = models.IntegerField(db_column='IdSerieDestino')
    # Field name made lowercase.
    seriedestino = models.CharField(db_column='SerieDestino', max_length=4)
    # Field name made lowercase.
    correlativodestino = models.BigIntegerField(db_column='CorrelativoDestino')
    # Field name made lowercase.
    fechaemisiondestino = models.DateTimeField(
        db_column='FechaEmisionDestino', blank=True, null=True)
    # Field name made lowercase.
    esanicipo = models.BooleanField(
        db_column='EsAnicipo', blank=True, null=True)
    # Field name made lowercase.
    monedadestino = models.CharField(
        db_column='MonedaDestino', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    montoanticipo = models.DecimalField(
        db_column='MontoAnticipo', max_digits=12, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    auxiliar1 = models.CharField(
        db_column='Auxiliar1', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar2 = models.CharField(
        db_column='Auxiliar2', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    auxiliar3 = models.CharField(
        db_column='Auxiliar3', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)
    documentocontabledestinofechaemision = models.DateTimeField(
        db_column='DocumentoContableDestinoFechaEmision', blank=True, null=True)  # Field name made lowercase.
    documentocontabledestinomontototal = models.DecimalField(
        db_column='DocumentoContableDestinoMontoTotal', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocumentoReferencia'


class Entidad(models.Model):
    # Field name made lowercase.
    identidad = models.BigIntegerField(db_column='IdEntidad', primary_key=True)
    # Field name made lowercase.
    idtipodocumentoidentidad = models.IntegerField(
        db_column='IdTipoDocumentoIdentidad', blank=True, null=True)
    # Field name made lowercase.
    codigotipodocumentosunat = models.CharField(
        db_column='CodigoTipoDocumentoSunat', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    tipodocumentodescripcion = models.CharField(
        db_column='TipoDocumentoDescripcion', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    numerodocumento = models.CharField(
        db_column='NumeroDocumento', max_length=20)
    # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=200)
    # Field name made lowercase.
    correoelectronico = models.CharField(
        db_column='CorreoElectronico', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    direccion = models.CharField(
        db_column='Direccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    codigoubigeo = models.CharField(db_column='CodigoUbigeo', max_length=6)
    # Field name made lowercase.
    descripcionubigeo = models.CharField(
        db_column='DescripcionUbigeo', max_length=250)
    # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=30)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(db_column='LogFechaCreacion')
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(db_column='LogFechaModif')
    # Field name made lowercase.
    logestado = models.SmallIntegerField(db_column='logEstado')

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'Entidad'


class Mensajes(models.Model):
    # Field name made lowercase.
    idtarea = models.IntegerField(db_column='IdTarea')

    class Meta:
        managed = False
        db_table = 'MENSAJES'


class Recibopago(models.Model):
    # Field name made lowercase.
    idrecibopago = models.BigIntegerField(
        db_column='IdReciboPago', primary_key=True)
    # Field name made lowercase.
    iddocumentocontable = models.BigIntegerField(
        db_column='IdDocumentoContable')
    # Field name made lowercase.
    numerocuota = models.IntegerField(db_column='NumeroCuota')
    # Field name made lowercase.
    monto = models.DecimalField(
        db_column='Monto', max_digits=18, decimal_places=4)
    # Field name made lowercase.
    fechavencimiento = models.DateTimeField(db_column='FechaVencimiento')
    # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')
    # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='Estado')
    # Field name made lowercase.
    idrecibofinanciero = models.BigIntegerField(db_column='IdReciboFinanciero')
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'ReciboPago'


class Seriesucursal2(models.Model):
    # Field name made lowercase.
    idseriesucursal = models.BigIntegerField(
        db_column='IdSerieSucursal', primary_key=True)
    # Field name made lowercase.
    idserie = models.IntegerField(db_column='IdSerie', blank=True, null=True)
    # Field name made lowercase.
    idsucursal = models.IntegerField(
        db_column='IdSucursal', blank=True, null=True)
    # Field name made lowercase.
    seriecorrelativo = models.BigIntegerField(
        db_column='SerieCorrelativo', blank=True, null=True)
    # Field name made lowercase.
    seriedescripcion = models.CharField(
        db_column='SerieDescripcion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    serieidentidad = models.BigIntegerField(
        db_column='SerieIdEntidad', blank=True, null=True)
    # Field name made lowercase.
    serieidtipodocumento = models.IntegerField(
        db_column='SerieIdTipoDocumento', blank=True, null=True)
    # Field name made lowercase.
    serietiposerie = models.IntegerField(
        db_column='SerieTipoSerie', blank=True, null=True)
    serietipodocumentodescripcion = models.CharField(
        db_column='SerieTipoDocumentoDescripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    serietipodocumentocodigo = models.CharField(
        db_column='SerieTipoDocumentoCodigo', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    serieorden = models.SmallIntegerField(
        db_column='SerieOrden', blank=True, null=True)
    # Field name made lowercase.
    sucursalidentidad = models.BigIntegerField(db_column='SucursalIdEntidad')
    # Field name made lowercase.
    sucursaldireccion = models.CharField(
        db_column='SucursalDireccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    sucursalabreviatura = models.CharField(
        db_column='SucursalAbreviatura', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    sucursalcodigosunat = models.CharField(
        db_column='SucursalCodigoSunat', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    sucursalubigeo = models.CharField(
        db_column='SucursalUbigeo', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    sucursalimagen = models.CharField(
        db_column='SucursalImagen', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(
        db_column='LogFechaCreacion', blank=True, null=True)
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(
        db_column='LogFechaModif', blank=True, null=True)
    # Field name made lowercase.
    logestado = models.SmallIntegerField(
        db_column='LogEstado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SerieSucursal'


class Sucursal(models.Model):
    # Field name made lowercase.
    idsucursal = models.IntegerField(db_column='IdSucursal', primary_key=True)
    # Field name made lowercase.
    identidad = models.BigIntegerField(db_column='IdEntidad')
    # Field name made lowercase.
    direccion = models.CharField(
        db_column='Direccion', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    abreviatura = models.CharField(
        db_column='Abreviatura', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    codigosunat = models.CharField(
        db_column='CodigoSunat', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    ubigeo = models.CharField(
        db_column='Ubigeo', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    logusuariocreacion = models.CharField(
        db_column='LogUsuarioCreacion', max_length=50)
    # Field name made lowercase.
    logfechacreacion = models.DateTimeField(db_column='LogFechaCreacion')
    # Field name made lowercase.
    logusuariomodif = models.CharField(
        db_column='LogUsuarioModif', max_length=50)
    # Field name made lowercase.
    logfechamodif = models.DateTimeField(db_column='LogFechaModif')
    # Field name made lowercase.
    logestado = models.SmallIntegerField(db_column='logEstado')
    # Field name made lowercase.
    imagen = models.CharField(
        db_column='Imagen', max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'Sucursal'


# class Catalogocodigos(models.Model):
#     id = models.AutoField(unique=True,primary_key=True)
#     tabla = models.CharField(max_length=100)
#     campo = models.CharField(max_length=100)
#     valor = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=500)
#
#     class Meta:
#         app_label = 'ERPQueryEntities'
#         managed = False
#         db_table = 'catalogocodigos'


class Cuadremoneda(models.Model):
    idcuadremoneda = models.BigIntegerField(primary_key=True)
    idcuadrecaja = models.IntegerField()
    idmoneda = models.IntegerField()
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.SmallIntegerField()
    montoapertura = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True)
    montocierre = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True)
    montorealcierre = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50, blank=True, null=True)
    log_datecrea = models.DateTimeField(blank=True, null=True)
    log_usermodif = models.CharField(max_length=50, blank=True, null=True)
    log_datemodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'cuadremoneda'


class Listaprecios(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    idlistaprecios = models.BigIntegerField(
        db_column='IdListaPrecios', blank=True, null=True)
    # Field name made lowercase.
    iditem = models.BigIntegerField(db_column='IdItem', blank=True, null=True)
    # Field name made lowercase.
    idsucursal = models.BigIntegerField(
        db_column='IdSucursal', blank=True, null=True)
    # Field name made lowercase.
    idmarca = models.BigIntegerField(
        db_column='IdMarca', blank=True, null=True)
    # Field name made lowercase.
    identidad = models.BigIntegerField(
        db_column='IdEntidad', blank=True, null=True)
    # Field name made lowercase.
    idalmacen = models.BigIntegerField(
        db_column='IdAlmacen', blank=True, null=True)
    # Field name made lowercase.
    idmoneda = models.BigIntegerField(
        db_column='IdMoneda', blank=True, null=True)
    # Field name made lowercase.
    iditemlistaprecios = models.BigIntegerField(
        db_column='IdItemListaPrecios', blank=True, null=True)
    # Field name made lowercase.
    idparent = models.BigIntegerField(
        db_column='IdParent', blank=True, null=True)
    idtipoprecioventaunitario = models.BigIntegerField(
        db_column='IdTipoPrecioVentaUnitario', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    idtipoafectacionigv = models.BigIntegerField(
        db_column='IdTipoAfectacionIGV', blank=True, null=True)
    # Field name made lowercase.
    idfamilia = models.BigIntegerField(
        db_column='IdFamilia', blank=True, null=True)
    # Field name made lowercase.
    idcategoria = models.BigIntegerField(
        db_column='IdCategoria', blank=True, null=True)
    # Field name made lowercase.
    tipoitem = models.IntegerField(db_column='TipoItem', blank=True, null=True)
    # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)
    # Field name made lowercase.
    controlarstock = models.IntegerField(
        db_column='ControlarStock', blank=True, null=True)
    # Field name made lowercase.
    nombreitem = models.CharField(
        db_column='NombreItem', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    descripcionitem = models.CharField(
        db_column='DescripcionItem', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    codigoitem = models.CharField(
        db_column='CodigoItem', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    codigobarras = models.CharField(
        db_column='CodigoBarras', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nombremarca = models.CharField(
        db_column='NombreMarca', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    descripcionmarca = models.CharField(
        db_column='DescripcionMarca', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    unidadiso = models.CharField(
        db_column='UnidadISO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    preciobase = models.DecimalField(
        db_column='PrecioBase', max_digits=18, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    preciolista = models.DecimalField(
        db_column='PrecioLista', max_digits=18, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)
    # Field name made lowercase.
    estadoitem = models.IntegerField(
        db_column='EstadoItem', blank=True, null=True)
    # Field name made lowercase.
    mostrardetallado = models.IntegerField(
        db_column='MostrarDetallado', blank=True, null=True)
    # Field name made lowercase.
    esfavorito = models.SmallIntegerField(
        db_column='EsFavorito', blank=True, null=True)
    # Field name made lowercase.
    imprimirlote = models.IntegerField(
        db_column='ImprimirLote', blank=True, null=True)
    # Field name made lowercase.
    controllotes = models.IntegerField(
        db_column='ControlLotes', blank=True, null=True)
    # Field name made lowercase.
    tieneimpuestobolsa = models.IntegerField(
        db_column='TieneImpuestoBolsa', blank=True, null=True)
    # Field name made lowercase.
    comentariopreciolista = models.CharField(
        db_column='ComentarioPrecioLista', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cantidadequivalencia = models.IntegerField(
        db_column='CantidadEquivalencia', blank=True, null=True)
    log_usercrea = models.CharField(max_length=50, blank=True, null=True)
    log_usermodif = models.CharField(max_length=50, blank=True, null=True)
    log_datecrea = models.DateTimeField(blank=True, null=True)
    log_datemodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'listaprecios'


class SerieFinanzas(models.Model):
    IdSerie = models.IntegerField(primary_key=True)
    IdEntidad = models.BigIntegerField(
        db_column='IdEntidad', blank=True, null=True)
    IdTipoDocumento = models.IntegerField(
        db_column='IdTipoDocumento', blank=True, null=True)
    Descripcion = models.CharField(max_length=50, blank=True, null=True)
    Abreviacion = models.CharField(max_length=10, blank=True, null=True)
    Correlativo = models.BigIntegerField(blank=True, null=True)
    Tipo_serie = models.IntegerField(
        db_column='Tipo_serie', blank=True, null=True)
    Orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)
    log_usuariocreacion = models.CharField(
        max_length=50, blank=True, null=True)
    log_usuariomodif = models.CharField(max_length=50, blank=True, null=True)
    log_fechacreacion = models.DateTimeField(blank=True, null=True)
    log_fechamodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'Serie'


class SerieLogistica(models.Model):
    IdSerie = models.IntegerField(primary_key=True)
    IdEntidad = models.BigIntegerField(
        db_column='IdEntidad', blank=True, null=True)
    Descripcion = models.CharField(max_length=50, blank=True, null=True)
    Abreviacion = models.CharField(max_length=10, blank=True, null=True)
    Correlativo = models.BigIntegerField(blank=True, null=True)
    Tipo_serie = models.IntegerField(
        db_column='Tipo_serie', blank=True, null=True)
    Orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)
    log_usuariocreacion = models.CharField(
        max_length=50, blank=True, null=True)
    log_usuariomodif = models.CharField(max_length=50, blank=True, null=True)
    log_fechacreacion = models.DateTimeField(blank=True, null=True)
    log_fechamodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'Serie'


class SerieContabilidad(models.Model):
    idserie = models.IntegerField(primary_key=True)
    identidad = models.BigIntegerField(
        db_column='identidad', blank=True, null=True)
    idtipo_documento = models.IntegerField(
        db_column='idtipo_documento', blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    abreviacion = models.CharField(max_length=10, blank=True, null=True)
    correlativo = models.BigIntegerField(blank=True, null=True)
    tipo_serie = models.IntegerField(
        db_column='tipo_serie', blank=True, null=True)
    orden = models.SmallIntegerField(db_column='orden', blank=True, null=True)
    log_usuariocreacion = models.CharField(
        max_length=50, blank=True, null=True)
    log_usuariomodif = models.CharField(max_length=50, blank=True, null=True)
    log_fechacreacion = models.DateTimeField(blank=True, null=True)
    log_fechamodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'serie'


class Serie(models.Model):
    idserie = models.IntegerField(primary_key=True)
    correlativo = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    identidad = models.BigIntegerField(blank=True, null=True)
    idtipodocumento = models.IntegerField(blank=True, null=True)
    tiposerie = models.IntegerField(blank=True, null=True)
    tipodocumento_descripcion = models.CharField(
        max_length=50, blank=True, null=True)
    tipodocumento_codigo = models.CharField(
        max_length=50, blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)
    log_usuariocreacion = models.CharField(
        max_length=50, blank=True, null=True)
    log_fechacreacion = models.DateTimeField(blank=True, null=True)
    log_usuariomodif = models.CharField(max_length=50, blank=True, null=True)
    log_fechamodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'serie'


class SerieSucursal(models.Model):
    idseriesucursal = models.BigIntegerField(primary_key=True)
    idserie = models.ForeignKey(
        Serie, models.DO_NOTHING, db_column='idserie', blank=True, null=True)
    idsucursal = models.IntegerField(blank=True, null=True)
    log_usuariocreacion = models.CharField(
        max_length=50, blank=True, null=True)
    log_fechacreacion = models.DateTimeField(blank=True, null=True)
    log_usuariomodif = models.CharField(max_length=50, blank=True, null=True)
    log_fechamodif = models.DateTimeField(blank=True, null=True)
    log_estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'serie_sucursal'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class TipoDocumento(models.Model):
    idtipo_documento = models.IntegerField(unique=True, primary_key=True)
    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=10)
    log_usuariocreacion = models.CharField(max_length=50)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=50)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        app_label = 'ERPQueryEntities'
        managed = False
        db_table = 'tipo_documento'
