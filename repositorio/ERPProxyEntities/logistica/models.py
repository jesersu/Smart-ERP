# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Serie(models.Model):
    idserie = models.BigAutoField(db_column='IdSerie', primary_key=True)  # Field name made lowercase.
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='IdEntidad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    abreviacion = models.CharField(db_column='Abreviacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    correlativo = models.BigIntegerField(db_column='Correlativo')  # Field name made lowercase.
    tipo_serie = models.IntegerField(db_column='Tipo_serie')  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    log_usuariocreacion = models.CharField(max_length=50)
    log_fechacreacion = models.DateTimeField()
    log_usuariomodif = models.CharField(max_length=50)
    log_fechamodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'Serie'


class Activofijo(models.Model):
    idactivo = models.BigAutoField(primary_key=True)
    iditem = models.ForeignKey('Item', models.DO_NOTHING, db_column='iditem')
    idarea = models.ForeignKey('Area', models.DO_NOTHING, db_column='idarea')
    idcentrocosto = models.ForeignKey('Centrocosto', models.DO_NOTHING, db_column='idcentrocosto', blank=True, null=True)
    idcategoria = models.ForeignKey('CategoriaactivoFijo', models.DO_NOTHING, db_column='idcategoria')
    esvaloractual = models.SmallIntegerField()
    costo = models.DecimalField(max_digits=18, decimal_places=4)
    tipobien = models.SmallIntegerField()
    anioadquisicion = models.IntegerField()
    vidautil = models.DecimalField(max_digits=18, decimal_places=2)
    depreciacionanual = models.DecimalField(max_digits=18, decimal_places=4)
    valorresidual = models.DecimalField(max_digits=18, decimal_places=4)
    depreciacionacumulada = models.DecimalField(max_digits=29, decimal_places=4, blank=True, null=True)
    vidarestante = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    modelo = models.CharField(max_length=250)
    numserie = models.CharField(max_length=250)
    motivoingreso = models.IntegerField()
    material = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    dimension = models.CharField(max_length=250)
    ubicacionlocal = models.CharField(max_length=250)
    ubicacionoficina = models.CharField(max_length=250)
    ambiente = models.CharField(max_length=250)
    observacion = models.CharField(max_length=250)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'activofijo'


class Almacen(models.Model):
    idalmacen = models.BigAutoField(primary_key=True)
    idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idsucursal')
    tipo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'almacen'


class Area(models.Model):
    idarea = models.BigIntegerField(primary_key=True)
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='identidad')
    descripcion = models.CharField(max_length=250)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'area'


class Categoria(models.Model):
    idcategoria = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='identidad')
    idfamilia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='idfamilia')
    prefijo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    idparent = models.BigIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'categoria'


class CategoriaactivoFijo(models.Model):
    idcategoria = models.BigAutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=500)
    prefijo = models.CharField(max_length=20)
    porcentajedepreciacion = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'categoriaactivo_fijo'


class Categoriaparametro(models.Model):
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria', primary_key=True)
    idparametro = models.ForeignKey('Parametro', models.DO_NOTHING, db_column='idparametro')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'categoriaparametro'
        unique_together = (('idcategoria', 'idparametro'),)


class Centrocosto(models.Model):
    idcentrocosto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    idarea = models.IntegerField()
    idcentrocostopadre = models.IntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'centrocosto'


class Codigoitem(models.Model):
    idcodigoitem = models.BigAutoField(primary_key=True)
    iditem = models.ForeignKey('Item', models.DO_NOTHING, db_column='iditem')
    idtipo = models.ForeignKey('Tipologistica', models.DO_NOTHING, db_column='idtipo')
    codigo = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'codigoitem'


class Codigosunat(models.Model):
    idcodigosunat = models.BigAutoField(primary_key=True)
    tipoestandar = models.SmallIntegerField()
    estandar = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    tipo = models.SmallIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'codigosunat'


class Columna(models.Model):
    idcolumna = models.BigAutoField(primary_key=True)
    idnivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='idnivel')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'columna'


class Comboitemprecio(models.Model):
    idcomboitemprecio = models.BigAutoField(primary_key=True)
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    idcomboitem = models.ForeignKey('Comboitems', models.DO_NOTHING, db_column='idcomboitem')
    precio = models.DecimalField(max_digits=18, decimal_places=4)
    descuento = models.DecimalField(max_digits=18, decimal_places=4)
    igvprecio = models.DecimalField(max_digits=18, decimal_places=4)
    valor = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'comboitemprecio'


class Comboitems(models.Model):
    idcomboitem = models.BigAutoField(primary_key=True)
    iditempadre = models.ForeignKey('Item', models.DO_NOTHING, db_column='iditempadre')
    iditemhijo = models.ForeignKey('Item', models.DO_NOTHING, db_column='iditemhijo')
    precio = models.DecimalField(max_digits=18, decimal_places=4)
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    igvprecio = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'comboitems'


class Componenteactivo(models.Model):
    idcomponenteactivo = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='identidad')
    descripcion = models.CharField(max_length=250)
    codigo = models.CharField(max_length=50)
    formula = models.CharField(max_length=250)
    nomenclatura = models.CharField(max_length=250)
    comentario = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'componenteactivo'


class Comprobante(models.Model):
    idcomprobante = models.BigAutoField(primary_key=True)
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    idtipocomprobante = models.ForeignKey('Tipocomprobante', models.DO_NOTHING, db_column='idtipocomprobante')
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='identidad')
    flete = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    numerocomprobante = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'comprobante'


class Cuentaparticular(models.Model):
    idcuentaparticular = models.IntegerField(primary_key=True)
    identidad = models.BigIntegerField()
    idcuentapadre = models.IntegerField()
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    idpadre = models.IntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cuentaparticular'


class Detalleinventario(models.Model):
    iddetalleinventario = models.BigAutoField(primary_key=True)
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad')
    idinventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='idinventario')
    iditem = models.ForeignKey('Item', models.DO_NOTHING, db_column='iditem')
    cantidad = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    observacion = models.CharField(max_length=150, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'detalleinventario'


class Detallemovimiento(models.Model):
    iddetallemovimiento = models.BigAutoField(primary_key=True)
    idmovimiento = models.ForeignKey('Movimiento', models.DO_NOTHING, db_column='idmovimiento')
    iditem = models.ForeignKey('Item', models.DO_NOTHING, db_column='iditem')
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad')
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    tipocambio = models.DecimalField(max_digits=18, decimal_places=4)
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    factor = models.SmallIntegerField()
    costounitario = models.DecimalField(max_digits=18, decimal_places=4)
    igv = models.DecimalField(max_digits=18, decimal_places=4)
    total = models.DecimalField(max_digits=18, decimal_places=4)
    lote = models.CharField(max_length=50, blank=True, null=True)
    fechavencimiento = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    idlote = models.BigIntegerField()
    iditemparent = models.BigIntegerField()
    idunidadparent = models.BigIntegerField()
    cantidaditemparent = models.DecimalField(max_digits=18, decimal_places=4)
    otros_impuestos = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'detallemovimiento'


class Detallemovstocknivel(models.Model):
    iddetallestocknivel = models.BigAutoField(primary_key=True)
    idstocknivelinventario = models.ForeignKey('Stocknivelinventario', models.DO_NOTHING, db_column='idstocknivelinventario')
    iddetallemovimiento = models.ForeignKey(Detallemovimiento, models.DO_NOTHING, db_column='iddetallemovimiento')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'detallemovstocknivel'


class Detallepedido(models.Model):
    iddetallepedido = models.BigAutoField(primary_key=True)
    idpedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='idpedido')
    iditem = models.BigIntegerField()
    codigoitem = models.CharField(max_length=50)
    descripcionitem = models.CharField(max_length=50)
    idunidad = models.BigIntegerField()
    descripcionunidad = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    valorunitario = models.DecimalField(max_digits=12, decimal_places=2)
    igv = models.DecimalField(max_digits=12, decimal_places=2)
    preciounitario = models.DecimalField(max_digits=12, decimal_places=2)
    idalmacen = models.BigIntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    monto_igv = models.DecimalField(max_digits=12, decimal_places=2)
    descuento = models.DecimalField(max_digits=12, decimal_places=2)
    valorigv = models.DecimalField(max_digits=18, decimal_places=2)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    idpedidodestino = models.BigIntegerField()
    cantidadpendiente = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'detallepedido'


class Detallepedidocantidad(models.Model):
    iddetallepedidocantidad = models.BigAutoField(primary_key=True)
    iddetallepedido = models.ForeignKey(Detallepedido, models.DO_NOTHING, db_column='iddetallepedido')
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'detallepedidocantidad'


class Detallestockinventario(models.Model):
    iddetallestockinventario = models.BigAutoField(primary_key=True)
    idstockinventario = models.ForeignKey('Stockinventario', models.DO_NOTHING, db_column='idstockinventario')
    iddetallemovimiento = models.ForeignKey(Detallemovimiento, models.DO_NOTHING, db_column='iddetallemovimiento')
    fechamovimiento = models.DateTimeField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'detallestockinventario'


class Documentoreferenciamovimiento(models.Model):
    iddocrefmovimiento = models.BigAutoField(primary_key=True)
    idtipocomprobante = models.ForeignKey('Tipocomprobante', models.DO_NOTHING, db_column='idtipocomprobante')
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    idmovimiento = models.ForeignKey('Movimiento', models.DO_NOTHING, db_column='idmovimiento')
    idserie = models.IntegerField()
    correlativo = models.IntegerField()
    numerocomprobante = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    iddocumentocontable = models.BigIntegerField()
    serie = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'documentoreferenciamovimiento'


class Dominio(models.Model):
    iddominio = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='identidad')
    idparametro = models.ForeignKey('Parametro', models.DO_NOTHING, db_column='idparametro')
    descripcion = models.CharField(max_length=200)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    codigo = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'dominio'


class Dominioapp(models.Model):
    iddominioapp = models.IntegerField(primary_key=True)
    idparametro = models.ForeignKey('Parametrosapp', models.DO_NOTHING, db_column='idparametro')
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dominioapp'


class Entidad(models.Model):
    identidad = models.BigIntegerField(primary_key=True)
    documento = models.CharField(max_length=20)
    tipodocumento = models.BigIntegerField()
    razonsocial = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'entidad'


class Entidadcomprobante(models.Model):
    identidadcomprobante = models.BigAutoField(primary_key=True)
    idcomprobante = models.ForeignKey(Comprobante, models.DO_NOTHING, db_column='idcomprobante')
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    tipo = models.SmallIntegerField()
    log_usercera = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'entidadcomprobante'


class Entidadparametro(models.Model):
    identidadparametro = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    idparametro = models.ForeignKey('Parametrosapp', models.DO_NOTHING, db_column='idparametro')
    tipo = models.SmallIntegerField()
    iddominio = models.BigIntegerField()
    valor = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'entidadparametro'


class Equivalencia(models.Model):
    idequivalencia = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    idunidadsrc = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidadsrc')
    idunidaddst = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidaddst')
    descripcion = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=3)
    estadosunat = models.SmallIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'equivalencia'


class Estadopedido(models.Model):
    idestado = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    etapa = models.SmallIntegerField()
    idtipocomprobante = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estadopedido'


class Familia(models.Model):
    idfamilia = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'familia'


class Inventario(models.Model):
    idinventario = models.BigAutoField(primary_key=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    valorizacion = models.DecimalField(max_digits=18, decimal_places=4)
    tipoinventario = models.SmallIntegerField(blank=True, null=True)
    estado = models.IntegerField()
    observacion = models.CharField(max_length=150, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'


class Item(models.Model):
    iditem = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    idmarca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='idmarca')
    idtipoitem = models.ForeignKey('Tipoitem', models.DO_NOTHING, db_column='idtipoitem')
    codigo = models.CharField(max_length=50)
    codigobarras = models.CharField(max_length=50)
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad')
    idequivalencia = models.ForeignKey(Equivalencia, models.DO_NOTHING, db_column='idequivalencia', blank=True, null=True)
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    precio = models.DecimalField(max_digits=18, decimal_places=4)
    igvprecio = models.DecimalField(max_digits=18, decimal_places=4)
    presentacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    tipovalorizacion = models.SmallIntegerField()
    tieneigv = models.SmallIntegerField()
    controlarstok = models.SmallIntegerField()
    esobsequio = models.SmallIntegerField()
    controlporlote = models.SmallIntegerField()
    destinadopara = models.SmallIntegerField()
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    volumen = models.DecimalField(max_digits=8, decimal_places=2)
    srcimagen = models.CharField(max_length=240, blank=True, null=True)
    comentario = models.CharField(max_length=240)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    desplegar = models.SmallIntegerField()
    costopromedio = models.DecimalField(max_digits=18, decimal_places=4)
    idparent = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    stocknegativo = models.SmallIntegerField()
    mermainformativa = models.DecimalField(max_digits=18, decimal_places=4)
    mermaautomatica = models.DecimalField(max_digits=18, decimal_places=4)
    stockminimo = models.DecimalField(max_digits=18, decimal_places=4)
    esfavorito = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item'


class Itemcategoria(models.Model):
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem', primary_key=True)
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemcategoria'
        unique_together = (('iditem', 'idcategoria'),)


class Itemcodigosunat(models.Model):
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem', primary_key=True)
    idcodigosunat = models.ForeignKey(Codigosunat, models.DO_NOTHING, db_column='idcodigosunat')
    tipoestandar = models.SmallIntegerField()
    valor = models.CharField(max_length=150)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemcodigosunat'
        unique_together = (('iditem', 'idcodigosunat'),)


class Itemcomponenteactivo(models.Model):
    iditemcomponenteactivo = models.BigAutoField(primary_key=True)
    idcomponenteactivo = models.ForeignKey(Componenteactivo, models.DO_NOTHING, db_column='idcomponenteactivo')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemcomponenteactivo'


class Itemcuentacontable(models.Model):
    iditemcuenta = models.BigAutoField(primary_key=True)
    idcuentaparticular = models.ForeignKey(Cuentaparticular, models.DO_NOTHING, db_column='idcuentaparticular')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    tipocuenta = models.SmallIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemcuentacontable'


class Itemparametro(models.Model):
    iditemparametro = models.BigAutoField(primary_key=True)
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    idparametro = models.ForeignKey('Parametro', models.DO_NOTHING, db_column='idparametro')
    iddominio = models.BigIntegerField(blank=True, null=True)
    valor = models.CharField(max_length=250, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemparametro'


class Itemparametroapp(models.Model):
    iditemparametroapp = models.BigAutoField(primary_key=True)
    idparametro = models.ForeignKey('Parametrosapp', models.DO_NOTHING, db_column='idparametro')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    tipo = models.IntegerField()
    iddominio = models.IntegerField()
    valor = models.CharField(max_length=100)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemparametroapp'


class Itemprecioestandar(models.Model):
    iditempreciostandar = models.BigAutoField(primary_key=True)
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    precio = models.DecimalField(max_digits=18, decimal_places=4)
    igvprecio = models.DecimalField(max_digits=18, decimal_places=4)
    valor = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemprecioestandar'


class Itemsucursal(models.Model):
    iditemsucursal = models.BigAutoField(primary_key=True)
    idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idsucursal')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'itemsucursal'


class Listapreciomarca(models.Model):
    idlistapreciomarca = models.BigAutoField(primary_key=True)
    idmarca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='idmarca')
    idlistaprecios = models.ForeignKey('Listaprecios', models.DO_NOTHING, db_column='idlistaprecios')
    identidad = models.BigIntegerField()
    porcentaje = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'listapreciomarca'


class Listaprecios(models.Model):
    idlistaprecios = models.BigAutoField(primary_key=True)
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    tipolista = models.SmallIntegerField()
    nombrelista = models.CharField(max_length=50)
    tipoajuste = models.SmallIntegerField()
    tipoprecio = models.SmallIntegerField()
    tieneigv = models.SmallIntegerField()
    porcentaje = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    insercionautomatica = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'listaprecios'


class ListapreciosItem(models.Model):
    idprecioitem = models.BigAutoField(primary_key=True)
    idlistaprecios = models.ForeignKey(Listaprecios, models.DO_NOTHING, db_column='idlistaprecios')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    precio = models.DecimalField(max_digits=18, decimal_places=4)
    log_usermodif = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    comentario = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listaprecios_item'


class Listapreciosucursal(models.Model):
    idlistapreciosucursal = models.BigAutoField(primary_key=True)
    idlistaprecios = models.ForeignKey(Listaprecios, models.DO_NOTHING, db_column='idlistaprecios')
    idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idsucursal')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'listapreciosucursal'


class Logcambios(models.Model):
    idlogcambios = models.BigAutoField(primary_key=True)
    nombretabla = models.CharField(max_length=50)
    idfila = models.BigIntegerField()
    fecha_modificacion = models.DateTimeField()
    comentario = models.CharField(max_length=500)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'logcambios'


class Marca(models.Model):
    idmarca = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'marca'


class Marcavehiculo(models.Model):
    idmarcavehiculo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'marcavehiculo'


class MotivoGeneralEntidad(models.Model):
    idmotivogeneralentidad = models.BigAutoField(primary_key=True)
    idmotivogeneral = models.ForeignKey('Motivomovimientogeneral', models.DO_NOTHING, db_column='idmotivogeneral')
    idmotivo = models.ForeignKey('Motivomovimiento', models.DO_NOTHING, db_column='idmotivo')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'motivo_general_entidad'


class Motivomovimiento(models.Model):
    idmotivo = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    idtipomovimiento = models.ForeignKey('Tipomovimiento', models.DO_NOTHING, db_column='idtipomovimiento')
    nombre = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'motivomovimiento'


class Motivomovimientogeneral(models.Model):
    idmotivogeneral = models.IntegerField(primary_key=True)
    idtipomovimiento = models.ForeignKey('Tipomovimiento', models.DO_NOTHING, db_column='idtipomovimiento')
    descripcion = models.CharField(max_length=200)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    modulo = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'motivomovimientogeneral'


class Movimiento(models.Model):
    idmovimiento = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    idtipomovimiento = models.ForeignKey('Tipomovimiento', models.DO_NOTHING, db_column='idtipomovimiento')
    idmotivo = models.ForeignKey(Motivomovimiento, models.DO_NOTHING, db_column='idmotivo', blank=True, null=True)
    idcomprobante = models.ForeignKey(Comprobante, models.DO_NOTHING, db_column='idcomprobante', blank=True, null=True)
    idorigen = models.BigIntegerField()
    iddestino = models.BigIntegerField()
    fechamovimiento = models.DateTimeField()
    idmovimientopadre = models.BigIntegerField()
    iddocumentocontable = models.BigIntegerField()
    estadomovimiento = models.SmallIntegerField()
    usuario = models.BigIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    idmoduloorigen = models.IntegerField()
    esfacturado = models.SmallIntegerField()
    codigomovimiento = models.CharField(max_length=50)
    flete = models.DecimalField(max_digits=18, decimal_places=4)
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    total = models.DecimalField(max_digits=18, decimal_places=4)
    tipoclienteasociado = models.SmallIntegerField()
    idclienteasociado = models.BigIntegerField()
    identidadcliente = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidadcliente')
    idserie = models.IntegerField()
    correlativo = models.BigIntegerField()
    clienteasociado_rs = models.CharField(max_length=700)
    observacion = models.CharField(max_length=700)

    class Meta:
        managed = False
        db_table = 'movimiento'


class Movimientoactivo(models.Model):
    idmovimientoactivo = models.BigAutoField(primary_key=True)
    idactivo = models.ForeignKey(Activofijo, models.DO_NOTHING, db_column='idactivo')
    idresponsable = models.ForeignKey('Responsableentidad', models.DO_NOTHING, db_column='idresponsable')
    idareaorigen = models.ForeignKey(Area, models.DO_NOTHING, db_column='idareaorigen')
    idsucursalorigen = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idsucursalorigen')
    idareadestino = models.ForeignKey(Area, models.DO_NOTHING, db_column='idareadestino')
    idsucursaldestino = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idsucursaldestino')
    fechamovimiento = models.DateTimeField()
    personarecibe = models.CharField(max_length=200)
    personaentrega = models.CharField(max_length=200)
    motivomovimiento = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=300)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'movimientoactivo'


class Movimientoentidad(models.Model):
    idmovimientoentidad = models.BigAutoField(primary_key=True)
    idmovimiento = models.ForeignKey(Movimiento, models.DO_NOTHING, db_column='idmovimiento')
    idrelacionentidad = models.BigIntegerField()
    idrelacionado = models.BigIntegerField()
    tipoentidad = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=500)
    apepat = models.CharField(max_length=500)
    apemat = models.CharField(max_length=500)
    tipodocumento = models.IntegerField()
    documento = models.CharField(max_length=50)
    razonsocial = models.CharField(max_length=500)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'movimientoentidad'


class Movimientotransporte(models.Model):
    idmovimientotrasporte = models.BigAutoField(primary_key=True)
    idmovimiento = models.ForeignKey(Movimiento, models.DO_NOTHING, db_column='idmovimiento')
    idvehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='idvehiculo', blank=True, null=True)
    idconductor = models.BigIntegerField(blank=True, null=True)
    nombreconductor = models.CharField(max_length=150, blank=True, null=True)
    licenciaconducir = models.CharField(max_length=20, blank=True, null=True)
    direccionpartida = models.CharField(max_length=360, blank=True, null=True)
    direccionllegada = models.CharField(max_length=360, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'movimientotransporte'


class Nivel(models.Model):
    idnivel = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'nivel'


class Nivelinventario(models.Model):
    idnivelinventario = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'nivelinventario'


class Parametro(models.Model):
    idparametro = models.BigAutoField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    idtipodato = models.ForeignKey('Tipodato', models.DO_NOTHING, db_column='idtipodato')
    elementodom = models.SmallIntegerField()
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'parametro'


class Parametrosapp(models.Model):
    idparametro = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'parametrosapp'


class Pasillo(models.Model):
    idpasillo = models.BigAutoField(primary_key=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    idcolumna = models.ForeignKey(Columna, models.DO_NOTHING, db_column='idcolumna')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'pasillo'


class Pedido(models.Model):
    idpedido = models.BigAutoField(primary_key=True)
    idtipocomprobante = models.ForeignKey('Tipocomprobante', models.DO_NOTHING, db_column='idtipocomprobante')
    idestado = models.ForeignKey(Estadopedido, models.DO_NOTHING, db_column='idestado')
    idtipomoneda = models.ForeignKey('Tipomoneda', models.DO_NOTHING, db_column='idtipomoneda')
    idempresa = models.IntegerField()
    tipooperacion = models.IntegerField()
    numerodocumento = models.BigIntegerField()
    identidademisor = models.BigIntegerField()
    identidadreceptora = models.BigIntegerField()
    monto_subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    monto_igv = models.DecimalField(max_digits=12, decimal_places=2)
    monto_total = models.DecimalField(max_digits=12, decimal_places=2)
    valorigv = models.DecimalField(max_digits=12, decimal_places=2)
    fechaemision = models.DateTimeField()
    fechaanulacion = models.DateTimeField()
    observacion = models.CharField(max_length=200)
    idcondicionpago = models.IntegerField()
    nombrecondicionpago = models.CharField(max_length=50)
    idtipocredito = models.IntegerField()
    nombretipocredito = models.CharField(max_length=50)
    idelementogasto = models.IntegerField()
    nombreelementogasto = models.CharField(max_length=100)
    log_usercrea = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_usermodif = models.CharField(max_length=50)
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    codigopedido = models.CharField(max_length=50)
    fechavencimiento = models.DateTimeField()
    iddocumentodestino = models.BigIntegerField()
    idmodulodestino = models.IntegerField()
    iddocumentoorigen = models.BigIntegerField()
    idmoduloorigen = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoDetallepedido(models.Model):
    idpedido_detallepedido = models.BigAutoField(primary_key=True)
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    iddetallepedido = models.ForeignKey(Detallepedido, models.DO_NOTHING, db_column='iddetallepedido')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    iddetallepedidodst = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_detallepedido'


class Pedidoarchivo(models.Model):
    idpedidoarchivo = models.BigAutoField(primary_key=True)
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    archivo = models.CharField(max_length=100)
    auxiliar1 = models.CharField(max_length=500)
    auxiliar2 = models.CharField(max_length=1)
    tipoarchivo = models.BinaryField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'pedidoarchivo'


class Pedidocentrocosto(models.Model):
    idpedidocentrocosto = models.BigAutoField(primary_key=True)
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido')
    idcentrocosto = models.ForeignKey(Centrocosto, models.DO_NOTHING, db_column='idcentrocosto')
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    porcentaje = models.DecimalField(max_digits=18, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'pedidocentrocosto'


class Pedidoreferencia(models.Model):
    idpedidoreferencia = models.BigAutoField(primary_key=True)
    idpedidodestino = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedidodestino')
    idpedidoorigen = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedidoorigen')
    correlativorigen = models.BigIntegerField()
    correlativodestino = models.BigIntegerField()
    montoanticipo = models.DecimalField(max_digits=12, decimal_places=2)
    monedadestino = models.IntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    codigopedidoorigen = models.CharField(max_length=50)
    codigopediddestino = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pedidoreferencia'


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    identidad = models.BigIntegerField()
    razonsocial = models.CharField(max_length=250)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'proveedor'


class Responsableentidad(models.Model):
    idresponsable = models.BigAutoField(primary_key=True)
    identidad = models.BigIntegerField()
    documento = models.CharField(max_length=20)
    tipodocumento = models.BigIntegerField()
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apaterno = models.CharField(max_length=50, blank=True, null=True)
    amaterno = models.CharField(max_length=50, blank=True, null=True)
    razonsocial = models.CharField(max_length=200)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'responsableentidad'


class Salidanivelinventario(models.Model):
    idtrasladonivelinventario = models.BigAutoField(primary_key=True)
    iddetallemovimiento = models.ForeignKey(Detallemovimiento, models.DO_NOTHING, db_column='iddetallemovimiento')
    idstocknivelinventario = models.ForeignKey('Stocknivelinventario', models.DO_NOTHING, db_column='idstocknivelinventario')
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    factor = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'salidanivelinventario'


class Seriesalmacen(models.Model):
    idseriealmacen = models.BigAutoField(primary_key=True)
    idseriesucursal = models.ForeignKey('Seriesucursal', models.DO_NOTHING, db_column='idseriesucursal')
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    tipomovimiento = models.IntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'seriesalmacen'


class Seriesucursal(models.Model):
    idseriesucursal = models.BigIntegerField(primary_key=True)
    idtipodocumento = models.IntegerField()
    codigodocumento = models.CharField(max_length=10)
    descripciondocumento = models.CharField(max_length=50)
    abreviaciondocumento = models.CharField(max_length=10)
    idserie = models.IntegerField()
    idsucursal = models.IntegerField()
    descripcionserie = models.CharField(max_length=50, blank=True, null=True)
    abreviacionserie = models.CharField(max_length=10, blank=True, null=True)
    correlativo = models.BigIntegerField()
    tiposerie = models.IntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'seriesucursal'


class Stockinventario(models.Model):
    idstockinventario = models.BigAutoField(primary_key=True)
    iditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='iditem')
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen')
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad')
    cantidadminima = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'stockinventario'


class Stocknivelinventario(models.Model):
    idstocknivelinventario = models.BigAutoField(primary_key=True)
    idstockinventario = models.ForeignKey(Stockinventario, models.DO_NOTHING, db_column='idstockinventario')
    idnivelinventario = models.ForeignKey(Nivelinventario, models.DO_NOTHING, db_column='idnivelinventario')
    idparent = models.BigIntegerField()
    tipo = models.IntegerField()
    numero = models.CharField(max_length=200)
    fechavencimiento = models.DateTimeField()
    observacion = models.CharField(max_length=200)
    aux1 = models.CharField(max_length=200)
    aux2 = models.CharField(max_length=200)
    aux3 = models.CharField(max_length=200)
    cantidadminima = models.DecimalField(max_digits=18, decimal_places=4)
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'stocknivelinventario'


class Sucursal(models.Model):
    idsucursal = models.BigIntegerField(primary_key=True)
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    descripcion = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tipocomprobante(models.Model):
    idtipocomprobante = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tipocomprobante'


class Tipodato(models.Model):
    idtipodato = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tipodato'


class Tipoitem(models.Model):
    idtipoitem = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tipoitem'


class Tipologistica(models.Model):
    idtipologistica = models.BigAutoField(primary_key=True)
    iddominio = models.IntegerField()
    valordominio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tipologistica'


class Tipomoneda(models.Model):
    idtipomoneda = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=5)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tipomoneda'


class Tipomovimiento(models.Model):
    idtipomovimiento = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    factor = models.SmallIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()
    tipoactividad = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tipomovimiento'


class Unidad(models.Model):
    idunidad = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    descripcionlarga = models.CharField(max_length=500, blank=True, null=True)
    codcliente = models.CharField(max_length=10)
    codigoiso = models.CharField(max_length=10)
    estadosunat = models.SmallIntegerField()
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'unidad'


class Vehiculo(models.Model):
    idvehiculo = models.BigAutoField(primary_key=True)
    idmarcavehiculo = models.ForeignKey(Marcavehiculo, models.DO_NOTHING, db_column='idmarcavehiculo')
    identidad = models.ForeignKey(Entidad, models.DO_NOTHING, db_column='identidad')
    descripcion = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    log_usercrea = models.CharField(max_length=50)
    log_usermodif = models.CharField(max_length=50)
    log_datecrea = models.DateTimeField()
    log_datemodif = models.DateTimeField()
    log_estado = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'vehiculo'
