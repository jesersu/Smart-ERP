/*
Created		21/03/2018
Modified		26/07/2021
Project		
Model			
Company		
Author		
Version		
Database		MS SQL 2005 
*/


Create table [item]
(
	[iditem] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idmarca] Bigint NOT NULL,
	[idtipoitem] Bigint NOT NULL,
	[codigo] Varchar(50) NOT NULL,
	[codigobarras] Varchar(50) NOT NULL,
	[idunidad] Bigint NOT NULL,
	[idequivalencia] Bigint NULL,
	[idtipomoneda] Integer NOT NULL,
	[precio] Decimal(18,4) NOT NULL,
	[igvprecio] Numeric(18,4) NOT NULL,
	[presentacion] Varchar(50) NOT NULL,
	[descripcion] Varchar(500) NOT NULL,
	[tipovalorizacion] Smallint Default 2 NOT NULL,
	[tieneigv] Smallint Default 0 NOT NULL,
	[controlarstok] Smallint Default 0 NOT NULL,
	[stocknegativo] Smallint NOT NULL,
	[esobsequio] Smallint Default 0 NOT NULL,
	[controlporlote] Smallint Default 0 NOT NULL,
	[destinadopara] Smallint Default 0 NOT NULL,
	[peso] Numeric(8,2) NOT NULL,
	[volumen] Numeric(8,2) NOT NULL,
	[srcimagen] Varchar(240) NULL,
	[comentario] Varchar(240) NOT NULL,
	[desplegar] Smallint Default 1 NOT NULL,
	[idparent] Bigint Default 0 NOT NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[mermainformativa] Decimal(18,4) NOT NULL,
	[mermaautomatica] Decimal(18,4) NOT NULL,
	[stockminimo] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_item] Primary Key ([iditem])
) 
go

Create table [categoria]
(
	[idcategoria] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idfamilia] Bigint NOT NULL,
	[prefijo] Varchar(10) NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[idparent] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_categoria] Primary Key ([idcategoria])
) 
go

Create table [itemcategoria]
(
	[iditem] Bigint NOT NULL,
	[idcategoria] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemcategoria] Primary Key ([iditem],[idcategoria])
) 
go

Create table [entidad]
(
	[identidad] Bigint NOT NULL,
	[documento] Varchar(20) NOT NULL,
	[tipodocumento] Bigint NOT NULL,
	[razonsocial] Varchar(200) NOT NULL,
	[direccion] Varchar(200) NULL,
	[correo] Varchar(50) NULL,
	[telefono] Varchar(50) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_entidad] Primary Key ([identidad])
) 
go

Create table [parametro]
(
	[idparametro] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idtipodato] Bigint NOT NULL,
	[elementodom] Smallint NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_parametro] Primary Key ([idparametro])
) 
go

Create table [tipodato]
(
	[idtipodato] Bigint Identity NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_tipodato] Primary Key ([idtipodato])
) 
go

Create table [dominio]
(
	[iddominio] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idparametro] Bigint NOT NULL,
	[codigo] Varchar(5) NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_dominio] Primary Key ([iddominio])
) 
go

Create table [itemparametro]
(
	[iditemparametro] Bigint Identity NOT NULL,
	[iditem] Bigint NOT NULL,
	[idparametro] Bigint NOT NULL,
	[iddominio] Bigint NULL,
	[valor] Varchar(250) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemparametro] Primary Key ([iditemparametro])
) 
go

Create table [sucursal]
(
	[idsucursal] Bigint NOT NULL,
	[identidad] Bigint NOT NULL,
	[descripcion] Varchar(200) NOT NULL,
	[direccion] Varchar(200) NOT NULL,
	[telefono] Varchar(15) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_sucursal] Primary Key ([idsucursal])
) 
go

Create table [detallestockinventario]
(
	[iddetallestockinventario] Bigint Identity NOT NULL,
	[idstockinventario] Bigint NOT NULL,
	[iddetallemovimiento] Bigint NOT NULL,
	[fechamovimiento] Datetime NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_detallestockinventario] Primary Key ([iddetallestockinventario])
) 
go

Create table [tipoitem]
(
	[idtipoitem] Bigint Identity NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_tipoitem] Primary Key ([idtipoitem])
) 
go

Create table [movimiento]
(
	[idmovimiento] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[identidadcliente] Bigint NOT NULL,
	[idtipomovimiento] Bigint NOT NULL,
	[idmotivo] Bigint NULL,
	[idcomprobante] Bigint NULL,
	[idtipomoneda] Integer NOT NULL,
	[idorigen] Bigint NOT NULL,
	[iddestino] Bigint NOT NULL,
	[fechamovimiento] Datetime NOT NULL,
	[idmovimientopadre] Bigint NOT NULL,
	[iddocumentocontable] Bigint NOT NULL,
	[codigomovimiento] Varchar(50) NOT NULL,
	[estadomovimiento] Smallint NOT NULL,
	[idmoduloorigen] Integer NOT NULL,
	[esfacturado] Smallint NOT NULL,
	[usuario] Bigint NOT NULL,
	[flete] Decimal(18,4) NOT NULL,
	[total] Decimal(18,4) NOT NULL,
	[tipoclienteasociado] Smallint NOT NULL,
	[idclienteasociado] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_movimiento] Primary Key ([idmovimiento])
) 
go

Create table [tipocomprobante]
(
	[idtipocomprobante] Integer NOT NULL,
	[codigo] Varchar(10) NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_tipocomprobante] Primary Key ([idtipocomprobante])
) 
go

Create table [categoriaparametro]
(
	[idcategoria] Bigint NOT NULL,
	[idparametro] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_categoriaparametro] Primary Key ([idcategoria],[idparametro])
) 
go

Create table [tipomovimiento]
(
	[idtipomovimiento] Bigint Identity NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[factor] Smallint NOT NULL,
	[tipoactividad] Smallint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_tipomovimiento] Primary Key ([idtipomovimiento])
) 
go

Create table [unidad]
(
	[idunidad] Bigint Identity NOT NULL,
	[descripcion] Varchar(100) NOT NULL,
	[descripcionlarga] Varchar(500) NULL,
	[codcliente] Varchar(10) NOT NULL,
	[codigoiso] Varchar(10) NOT NULL,
	[estadosunat] Smallint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_unidad] Primary Key ([idunidad])
) 
go

Create table [equivalencia]
(
	[idequivalencia] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idunidadsrc] Bigint NOT NULL,
	[idunidaddst] Bigint NOT NULL,
	[descripcion] Varchar(100) NOT NULL,
	[cantidad] Numeric(10,3) NOT NULL,
	[estadosunat] Smallint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_equivalencia] Primary Key ([idequivalencia])
) 
go

Create table [nivel]
(
	[idnivel] Bigint Identity NOT NULL,
	[descripcion] Varchar(50) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_nivel] Primary Key ([idnivel])
) 
go

Create table [columna]
(
	[idcolumna] Bigint Identity NOT NULL,
	[idnivel] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_columna] Primary Key ([idcolumna])
) 
go

Create table [pasillo]
(
	[idpasillo] Bigint Identity NOT NULL,
	[idalmacen] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[idcolumna] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_pasillo] Primary Key ([idpasillo])
) 
go

Create table [vehiculo]
(
	[idvehiculo] Bigint Identity NOT NULL,
	[idmarcavehiculo] Bigint NOT NULL,
	[identidad] Bigint NOT NULL,
	[descripcion] Varchar(100) NOT NULL,
	[placa] Varchar(20) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_vehiculo] Primary Key ([idvehiculo])
) 
go

Create table [marcavehiculo]
(
	[idmarcavehiculo] Bigint Identity NOT NULL,
	[nombre] Varchar(20) NOT NULL,
	[descripcion] Varchar(100) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_marcavehiculo] Primary Key ([idmarcavehiculo])
) 
go

Create table [familia]
(
	[idfamilia] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_familia] Primary Key ([idfamilia])
) 
go

Create table [marca]
(
	[idmarca] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_marca] Primary Key ([idmarca])
) 
go

Create table [tipomoneda]
(
	[idtipomoneda] Integer NOT NULL,
	[nombre] Varchar(50) NOT NULL,
	[simbolo] Varchar(5) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_tipomoneda] Primary Key ([idtipomoneda])
) 
go

Create table [comprobante]
(
	[idcomprobante] Bigint Identity NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[idtipocomprobante] Integer NOT NULL,
	[identidad] Bigint NOT NULL,
	[flete] Decimal(18,4) NULL,
	[numerocomprobante] Varchar(50) NOT NULL,
	[total] Decimal(18,4) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_comprobante] Primary Key ([idcomprobante])
) 
go

Create table [entidadcomprobante]
(
	[identidadcomprobante] Bigint Identity NOT NULL,
	[idcomprobante] Bigint NOT NULL,
	[identidad] Bigint NOT NULL,
	[tipo] Smallint NOT NULL,
	[log_usercera] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_entidadcomprobante] Primary Key ([identidadcomprobante])
) 
go

Create table [stockinventario]
(
	[idstockinventario] Bigint Identity NOT NULL,
	[iditem] Bigint NOT NULL,
	[idalmacen] Bigint NOT NULL,
	[idunidad] Bigint NOT NULL,
	[cantidadminima] Decimal(18,4) NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_stockinventario] Primary Key ([idstockinventario])
) 
go

Create table [movimientotransporte]
(
	[idmovimientotrasporte] Bigint Identity NOT NULL,
	[idmovimiento] Bigint NOT NULL,
	[idvehiculo] Bigint NULL,
	[idconductor] Bigint NULL,
	[nombreconductor] Varchar(150) NULL,
	[licenciaconducir] Varchar(20) NULL,
	[direccionpartida] Varchar(360) NULL,
	[direccionllegada] Varchar(360) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_movimientotransporte] Primary Key ([idmovimientotrasporte])
) 
go

Create table [almacen]
(
	[idalmacen] Bigint Identity NOT NULL,
	[idsucursal] Bigint NOT NULL,
	[tipo] Integer NOT NULL,
	[descripcion] Varchar(100) NOT NULL,
	[direccion] Varchar(200) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_almacen] Primary Key ([idalmacen])
) 
go

Create table [categoriaactivo_fijo]
(
	[idcategoria] Bigint Identity NOT NULL,
	[nombrecategoria] Varchar(500) NOT NULL,
	[prefijo] Varchar(20) NOT NULL,
	[porcentajedepreciacion] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_categoriaactivo_fijo] Primary Key ([idcategoria])
) 
go

Create table [activofijo]
(
	[idactivo] Bigint Identity NOT NULL,
	[idarea] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[idcentrocosto] Integer NULL,
	[idcategoria] Bigint NOT NULL,
	[esvaloractual] Smallint NOT NULL,
	[costo] Decimal(18,4) NOT NULL,
	[tipobien] Smallint NOT NULL,
	[anioadquisicion] Integer NOT NULL,
	[vidautil] Decimal(18,2) NOT NULL,
	[depreciacionanual] Decimal(18,4) NOT NULL,
	[valorresidual] Decimal(18,4) NOT NULL,
	[depreciacionacumulada] Decimal(18,4) NULL,
	[vidarestante] Decimal(18,4) NULL,
	[modelo] Varchar(250) NOT NULL,
	[numserie] Varchar(250) NOT NULL,
	[motivoingreso] Integer NOT NULL,
	[material] Varchar(250) NOT NULL,
	[color] Varchar(250) NOT NULL,
	[dimension] Varchar(250) NOT NULL,
	[ambiente] Varchar(250) NOT NULL,
	[ubicacionlocal] Varchar(250) NOT NULL,
	[ubicacionoficina] Varchar(250) NOT NULL,
	[observacion] Varchar(250) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_activofijo] Primary Key ([idactivo])
) 
go

Create table [centrocosto]
(
	[idcentrocosto] Integer NOT NULL,
	[nombre] Varchar(100) NOT NULL,
	[idarea] Integer NOT NULL,
	[idcentrocostopadre] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_centrocosto] Primary Key ([idcentrocosto])
) 
go

Create table [area]
(
	[idarea] Bigint NOT NULL,
	[identidad] Bigint NOT NULL,
	[descripcion] Varchar(250) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_area] Primary Key ([idarea])
) 
go

Create table [listaprecios]
(
	[idlistaprecios] Bigint Identity NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[tipolista] Smallint NOT NULL,
	[nombrelista] Varchar(50) NOT NULL,
	[tipoajuste] Smallint NOT NULL,
	[tipoprecio] Smallint NOT NULL,
	[tieneigv] Smallint NOT NULL,
	[porcentaje] Decimal(18,4) NOT NULL,
	[insercionautomatica] Smallint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_listaprecios] Primary Key ([idlistaprecios])
) 
go

Create table [listaprecios_item]
(
	[idprecioitem] Bigint Identity NOT NULL,
	[idlistaprecios] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[precio] Decimal(18,4) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_listaprecios_item] Primary Key ([idprecioitem])
) 
go

Create table [motivomovimiento]
(
	[idmotivo] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idtipomovimiento] Bigint NOT NULL,
	[nombre] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_motivomovimiento] Primary Key ([idmotivo])
) 
go

Create table [detallemovimiento]
(
	[iddetallemovimiento] Bigint Identity NOT NULL,
	[idmovimiento] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[idunidad] Bigint NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[tipocambio] Decimal(18,4) NOT NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[factor] Smallint NOT NULL,
	[costounitario] Decimal(18,4) NOT NULL,
	[igv] Decimal(18,4) NOT NULL,
	[total] Decimal(18,4) NOT NULL,
	[lote] Varchar(50) NULL,
	[fechavencimiento] Datetime NULL,
	[descripcion] Varchar(200) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_detallemovimiento] Primary Key ([iddetallemovimiento])
) 
go

Create table [itemcuentacontable]
(
	[iditemcuenta] Bigint Identity NOT NULL,
	[idcuentaparticular] Integer NOT NULL,
	[iditem] Bigint NOT NULL,
	[tipocuenta] Smallint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemcuentacontable] Primary Key ([iditemcuenta])
) 
go

Create table [pedido]
(
	[idpedido] Bigint Identity NOT NULL,
	[idtipocomprobante] Integer NOT NULL,
	[idestado] Integer NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[codigopedido] Varchar(50) NOT NULL,
	[idempresa] Integer NOT NULL,
	[tipooperacion] Integer NOT NULL,
	[numerodocumento] Bigint NOT NULL,
	[identidademisor] Bigint NOT NULL,
	[identidadreceptora] Bigint NOT NULL,
	[monto_subtotal] Decimal(12,2) NOT NULL,
	[monto_igv] Decimal(12,2) NOT NULL,
	[monto_total] Decimal(12,2) NOT NULL,
	[valorigv] Decimal(12,2) NOT NULL,
	[fechaemision] Datetime NOT NULL,
	[fechaanulacion] Datetime NOT NULL,
	[fechavencimiento] Datetime NOT NULL,
	[observacion] Varchar(200) NOT NULL,
	[idcondicionpago] Integer NOT NULL,
	[nombrecondicionpago] Varchar(50) NOT NULL,
	[idtipocredito] Integer NOT NULL,
	[nombretipocredito] Varchar(50) NOT NULL,
	[idelementogasto] Integer NOT NULL,
	[nombreelementogasto] Varchar(100) NOT NULL,
	[iddocumentodestino] Bigint NOT NULL,
	[idmodulodestino] Integer NOT NULL,
	[iddocumentoorigen] Bigint NOT NULL,
	[idmoduloorigen] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_pedido] Primary Key ([idpedido])
) 
go

Create table [detallepedido]
(
	[iddetallepedido] Bigint Identity NOT NULL,
	[idpedido] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[codigoitem] Varchar(50) NOT NULL,
	[descripcionitem] Varchar(50) NOT NULL,
	[idunidad] Bigint NOT NULL,
	[descripcionunidad] Varchar(50) NOT NULL,
	[cantidad] Decimal(12,2) NOT NULL,
	[cantidadpendiente] Decimal(12,2) NOT NULL,
	[valorunitario] Decimal(12,2) NOT NULL,
	[igv] Decimal(12,2) NOT NULL,
	[preciounitario] Decimal(12,2) NOT NULL,
	[idalmacen] Bigint NOT NULL,
	[subtotal] Decimal(12,2) NOT NULL,
	[monto_igv] Decimal(12,2) NOT NULL,
	[descuento] Decimal(12,2) NOT NULL,
	[valorigv] Decimal(18,2) NOT NULL,
	[idpedidodestino] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_detallepedido] Primary Key ([iddetallepedido])
) 
go

Create table [cuentaparticular]
(
	[idcuentaparticular] Integer NOT NULL,
	[identidad] Bigint NOT NULL,
	[idcuentapadre] Integer NOT NULL,
	[codigo] Varchar(20) NOT NULL,
	[descripcion] Varchar(250) NOT NULL,
	[idpadre] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_cuentaparticular] Primary Key ([idcuentaparticular])
) 
go

Create table [estadopedido]
(
	[idestado] Integer NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[etapa] Smallint NOT NULL,
	[idtipocomprobante] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_estadopedido] Primary Key ([idestado])
) 
go

Create table [pedidoarchivo]
(
	[idpedidoarchivo] Bigint Identity NOT NULL,
	[idpedido] Bigint NOT NULL,
	[archivo] Varchar(100) NOT NULL,
	[auxiliar1] Varchar(500) NOT NULL,
	[auxiliar2] Char(1) NOT NULL,
	[tipoarchivo] Varbinary(3) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_pedidoarchivo] Primary Key ([idpedidoarchivo])
) 
go

Create table [pedidoreferencia]
(
	[idpedidoreferencia] Bigint Identity NOT NULL,
	[idpedidodestino] Bigint NOT NULL,
	[idpedidoorigen] Bigint NOT NULL,
	[codigopedidoorigen] Varchar(50) NOT NULL,
	[codigopedidodestino] Varchar(50) NOT NULL,
	[correlativorigen] Bigint NOT NULL,
	[correlativodestino] Bigint NOT NULL,
	[montoanticipo] Decimal(12,2) NOT NULL,
	[monedadestino] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_pedidoreferencia] Primary Key ([idpedidoreferencia])
) 
go

Create table [pedidocentrocosto]
(
	[idpedidocentrocosto] Bigint Identity NOT NULL,
	[idpedido] Bigint NOT NULL,
	[idcentrocosto] Integer NOT NULL,
	[porcentaje] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_pedidocentrocosto] Primary Key ([idpedidocentrocosto])
) 
go

Create table [pedido_detallepedido]
(
	[idpedido_detallepedido] Bigint Identity NOT NULL,
	[idpedido] Bigint NOT NULL,
	[iddetallepedido] Bigint NOT NULL,
	[iddetallepedidodst] Bigint NOT NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_pedido_detallepedido] Primary Key ([idpedido_detallepedido])
) 
go

Create table [detallepedidocantidad]
(
	[iddetallepedidocantidad] Bigint Identity NOT NULL,
	[iddetallepedido] Bigint NOT NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_detallepedidocantidad] Primary Key ([iddetallepedidocantidad])
) 
go

Create table [movimientoactivo]
(
	[idmovimientoactivo] Bigint Identity NOT NULL,
	[idactivo] Bigint NOT NULL,
	[idresponsable] Bigint NOT NULL,
	[idareaorigen] Bigint NOT NULL,
	[idsucursalorigen] Bigint NOT NULL,
	[idareadestino] Bigint NOT NULL,
	[idsucursaldestino] Bigint NOT NULL,
	[fechamovimiento] Datetime NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_movimientoactivo] Primary Key ([idmovimientoactivo])
) 
go

Create table [comboitems]
(
	[idcomboitem] Bigint Identity NOT NULL,
	[iditempadre] Bigint NOT NULL,
	[iditemhijo] Bigint NOT NULL,
	[precio] Decimal(18,4) NOT NULL,
	[igvprecio] Decimal(18,4) NOT NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_comboitems] Primary Key ([idcomboitem])
) 
go

Create table [motivomovimientogeneral]
(
	[idmotivogeneral] Integer NOT NULL,
	[idtipomovimiento] Bigint NOT NULL,
	[descripcion] Varchar(200) NOT NULL,
	[modulo] Smallint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_motivomovimientogeneral] Primary Key ([idmotivogeneral])
) 
go

Create table [motivo_general_entidad]
(
	[idmotivogeneralentidad] Bigint Identity NOT NULL,
	[idmotivogeneral] Integer NOT NULL,
	[idmotivo] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_motivo_general_entidad] Primary Key ([idmotivogeneralentidad])
) 
go

Create table [listapreciosucursal]
(
	[idlistapreciosucursal] Bigint Identity NOT NULL,
	[idlistaprecios] Bigint NOT NULL,
	[idsucursal] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_listapreciosucursal] Primary Key ([idlistapreciosucursal])
) 
go

Create table [itemsucursal]
(
	[iditemsucursal] Bigint Identity NOT NULL,
	[idsucursal] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemsucursal] Primary Key ([iditemsucursal])
) 
go

Create table [parametrosapp]
(
	[idparametro] Integer NOT NULL,
	[descripcion] Varchar(200) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_parametrosapp] Primary Key ([idparametro])
) 
go

Create table [dominioapp]
(
	[iddominioapp] Integer NOT NULL,
	[idparametro] Integer NOT NULL,
	[codigo] Varchar(50) NOT NULL,
	[descripcion] Varchar(100) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_dominioapp] Primary Key ([iddominioapp])
) 
go

Create table [itemparametroapp]
(
	[iditemparametroapp] Bigint Identity NOT NULL,
	[idparametro] Integer NOT NULL,
	[iditem] Bigint NOT NULL,
	[tipo] Integer NOT NULL,
	[iddominio] Integer NOT NULL,
	[valor] Varchar(100) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemparametroapp] Primary Key ([iditemparametroapp])
) 
go

Create table [seriesucursal]
(
	[idseriesucursal] Bigint NOT NULL,
	[idtipodocumento] Integer NOT NULL,
	[codigodocumento] Varchar(10) NOT NULL,
	[descripciondocumento] Varchar(50) NOT NULL,
	[abreviaciondocumento] Varchar(10) NOT NULL,
	[idserie] Integer NOT NULL,
	[idsucursal] Integer NOT NULL,
	[descripcionserie] Varchar(50) NULL,
	[abreviacionserie] Varchar(10) NULL,
	[correlativo] Bigint NOT NULL,
	[tiposerie] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_seriesucursal] Primary Key ([idseriesucursal])
) 
go

Create table [seriesalmacen]
(
	[idseriealmacen] Bigint Identity NOT NULL,
	[idseriesucursal] Bigint NOT NULL,
	[idalmacen] Bigint NOT NULL,
	[tipomovimiento] Integer NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_seriesalmacen] Primary Key ([idseriealmacen])
) 
go

Create table [itemprecioestandar]
(
	[iditempreciostandar] Bigint Identity NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[iditem] Bigint NOT NULL,
	[precio] Decimal(18,4) NOT NULL,
	[igvprecio] Decimal(18,4) NOT NULL,
	[valor] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemprecioestandar] Primary Key ([iditempreciostandar])
) 
go

Create table [entidadparametro]
(
	[identidadparametro] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[idparametro] Integer NOT NULL,
	[tipo] Smallint NOT NULL,
	[iddominio] Bigint NOT NULL,
	[valor] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_entidadparametro] Primary Key ([identidadparametro])
) 
go

Create table [nivelinventario]
(
	[idnivelinventario] Bigint Identity NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_nivelinventario] Primary Key ([idnivelinventario])
) 
go

Create table [comboitemprecio]
(
	[idcomboitemprecio] Bigint Identity NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[idcomboitem] Bigint NOT NULL,
	[precio] Decimal(18,4) NOT NULL,
	[descuento] Decimal(18,4) NOT NULL,
	[igvprecio] Decimal(18,4) NOT NULL,
	[valor] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_comboitemprecio] Primary Key ([idcomboitemprecio])
) 
go

Create table [stocknivelinventario]
(
	[idstocknivelinventario] Bigint Identity NOT NULL,
	[idstockinventario] Bigint NOT NULL,
	[idnivelinventario] Bigint NOT NULL,
	[idparent] Bigint NOT NULL,
	[tipo] Integer NOT NULL,
	[numero] Varchar(200) NOT NULL,
	[fechavencimiento] Datetime NOT NULL,
	[observacion] Varchar(200) NOT NULL,
	[aux1] Varchar(200) NOT NULL,
	[aux2] Varchar(200) NOT NULL,
	[aux3] Varchar(200) NOT NULL,
	[cantidadminima] Decimal(18,4) NOT NULL,
	[cantidad] Decimal(18,4) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_stocknivelinventario] Primary Key ([idstocknivelinventario])
) 
go

Create table [codigoitem]
(
	[idcodigoitem] Bigint Identity NOT NULL,
	[iditem] Bigint NOT NULL,
	[idtipo] Bigint NOT NULL,
	[codigo] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_codigoitem] Primary Key ([idcodigoitem])
) 
go

Create table [tipologistica]
(
	[idtipologistica] Bigint Identity NOT NULL,
	[iddominio] Integer NOT NULL,
	[valordominio] Varchar(50) NOT NULL,
	[descripcion] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_tipologistica] Primary Key ([idtipologistica])
) 
go

Create table [logcambios]
(
	[idlogcambios] Bigint Identity NOT NULL,
	[idtabla] Integer NOT NULL,
	[nombretabla] Varchar(50) NOT NULL,
	[idfila] Bigint NOT NULL,
	[idcampo] Integer NOT NULL,
	[nombrecampo] Varchar(50) NOT NULL,
	[valoranterior] Varchar(100) NOT NULL,
	[valorcambiado] Varchar(500) NOT NULL,
	[fecha_modificacion] Datetime NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_logcambios] Primary Key ([idlogcambios])
) 
go

Create table [documentoreferenciamovimiento]
(
	[iddocrefmovimiento] Bigint Identity NOT NULL,
	[idtipocomprobante] Integer NOT NULL,
	[idtipomoneda] Integer NOT NULL,
	[idmovimiento] Bigint NOT NULL,
	[idserie] Integer NOT NULL,
	[serie] Varchar(50) NOT NULL,
	[correlativo] Integer NOT NULL,
	[numerocomprobante] Varchar(50) NOT NULL,
	[total] Decimal(18,4) NOT NULL,
	[iddocumentocontable] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_documentoreferenciamovimiento] Primary Key ([iddocrefmovimiento])
) 
go

Create table [componenteactivo]
(
	[idcomponenteactivo] Bigint Identity NOT NULL,
	[identidad] Bigint NOT NULL,
	[descripcion] Varchar(250) NOT NULL,
	[formula] Varchar(250) NOT NULL,
	[nomenclatura] Varchar(250) NOT NULL,
	[comentario] Varchar(50) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_componenteactivo] Primary Key ([idcomponenteactivo])
) 
go

Create table [itemcomponenteactivo]
(
	[iditemcomponenteactivo] Bigint Identity NOT NULL,
	[idcomponenteactivo] Bigint NOT NULL,
	[iditem] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemcomponenteactivo] Primary Key ([iditemcomponenteactivo])
) 
go

Create table [detallemovstocknivel]
(
	[iddetallestocknivel] Bigint Identity NOT NULL,
	[idstocknivelinventario] Bigint NOT NULL,
	[iddetallemovimiento] Bigint NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_detallemovstocknivel] Primary Key ([iddetallestocknivel])
) 
go

Create table [movimientoentidad]
(
	[idmovimientoentidad] Bigint Identity NOT NULL,
	[idmovimiento] Bigint NOT NULL,
	[idrelacionentidad] Bigint NOT NULL,
	[idrelacionado] Bigint NOT NULL,
	[tipoentidad] Integer NOT NULL,
	[descripcion] Varchar(500) NOT NULL,
	[codigo] Varchar(50) NOT NULL,
	[nombre] Varchar(500) NOT NULL,
	[apepat] Varchar(500) NOT NULL,
	[apemat] Varchar(500) NOT NULL,
	[tipodocumento] Integer NOT NULL,
	[documento] Varchar(50) NOT NULL,
	[razonsocial] Varchar(500) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_movimientoentidad] Primary Key ([idmovimientoentidad])
) 
go

Create table [codigosunat]
(
	[idcodigosunat] Bigint NOT NULL,
	[tipoestandar] Smallint NOT NULL,
	[estandar] Varchar(50) NOT NULL,
	[codigo] Varchar(50) NULL,
	[descripcion] Varchar(100) NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_codigosunat] Primary Key ([idcodigosunat])
) 
go

Create table [itemcodigosunat]
(
	[iditem] Bigint NOT NULL,
	[idcodigosunat] Bigint NOT NULL,
	[tipoestandar] Smallint NOT NULL,
	[valor] Varchar(150) NOT NULL,
	[log_usercrea] Varchar(50) NOT NULL,
	[log_usermodif] Varchar(50) NOT NULL,
	[log_datecrea] Datetime NOT NULL,
	[log_datemodif] Datetime NOT NULL,
	[log_estado] Smallint NOT NULL,
Constraint [pk_itemcodigosunat] Primary Key ([iditem],[idcodigosunat])
) 
go


Alter table [itemcategoria] add  foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [pasillo] add Constraint [Relationship41] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [activofijo] add Constraint [Relationship126] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [listaprecios_item] add Constraint [Relationship130] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [detallemovimiento] add Constraint [Relationship138] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [stockinventario] add Constraint [Relationship143] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemcuentacontable] add Constraint [Relationship147] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemparametro] add Constraint [Relationship156] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [comboitems] add Constraint [Relationship182] foreign key([iditempadre]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [comboitems] add Constraint [Relationship183] foreign key([iditemhijo]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemsucursal] add Constraint [Relationship190] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemparametroapp] add Constraint [Relationship193] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemprecioestandar] add Constraint [Relationship196] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [codigoitem] add Constraint [Relationship214] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemcomponenteactivo] add Constraint [Relationship225] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemcodigosunat] add Constraint [Relationship240] foreign key([iditem]) references [item] ([iditem])  on update no action on delete no action 
go
Alter table [itemcategoria] add  foreign key([idcategoria]) references [categoria] ([idcategoria])  on update no action on delete no action 
go
Alter table [categoriaparametro] add  foreign key([idcategoria]) references [categoria] ([idcategoria])  on update no action on delete no action 
go
Alter table [categoria] add  foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [sucursal] add Constraint [Relationship13] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [marca] add Constraint [Relationship54] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [equivalencia] add Constraint [Relationship67] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [vehiculo] add Constraint [Relationship72] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [entidadcomprobante] add Constraint [Relationship84] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [item] add Constraint [Relationship104] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [comprobante] add Constraint [Relationship113] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [area] add Constraint [Relationship125] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [familia] add Constraint [Relationship132] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [motivomovimiento] add Constraint [Relationship134] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [movimiento] add Constraint [Relationship139] foreign key([identidadcliente]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [parametro] add Constraint [Relationship154] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [dominio] add Constraint [Relationship155] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [movimientoactivo] add Constraint [Relationship179] foreign key([idresponsable]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [entidadparametro] add Constraint [Relationship199] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [movimiento] add Constraint [Relationship219] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [componenteactivo] add Constraint [Relationship223] foreign key([identidad]) references [entidad] ([identidad])  on update no action on delete no action 
go
Alter table [categoriaparametro] add  foreign key([idparametro]) references [parametro] ([idparametro])  on update no action on delete no action 
go
Alter table [dominio] add Constraint [Relationship153] foreign key([idparametro]) references [parametro] ([idparametro])  on update no action on delete no action 
go
Alter table [itemparametro] add Constraint [Relationship157] foreign key([idparametro]) references [parametro] ([idparametro])  on update no action on delete no action 
go
Alter table [parametro] add  foreign key([idtipodato]) references [tipodato] ([idtipodato])  on update no action on delete no action 
go
Alter table [almacen] add Constraint [Relationship117] foreign key([idsucursal]) references [sucursal] ([idsucursal])  on update no action on delete no action 
go
Alter table [movimientoactivo] add Constraint [Relationship178] foreign key([idsucursalorigen]) references [sucursal] ([idsucursal])  on update no action on delete no action 
go
Alter table [movimientoactivo] add Constraint [Relationship181] foreign key([idsucursaldestino]) references [sucursal] ([idsucursal])  on update no action on delete no action 
go
Alter table [listapreciosucursal] add Constraint [Relationship188] foreign key([idsucursal]) references [sucursal] ([idsucursal])  on update no action on delete no action 
go
Alter table [itemsucursal] add Constraint [Relationship189] foreign key([idsucursal]) references [sucursal] ([idsucursal])  on update no action on delete no action 
go
Alter table [item] add  foreign key([idtipoitem]) references [tipoitem] ([idtipoitem])  on update no action on delete no action 
go
Alter table [movimientotransporte] add Constraint [Relationship109] foreign key([idmovimiento]) references [movimiento] ([idmovimiento])  on update no action on delete no action 
go
Alter table [detallemovimiento] add Constraint [Relationship137] foreign key([idmovimiento]) references [movimiento] ([idmovimiento])  on update no action on delete no action 
go
Alter table [documentoreferenciamovimiento] add Constraint [Relationship215] foreign key([idmovimiento]) references [movimiento] ([idmovimiento])  on update no action on delete no action 
go
Alter table [movimientoentidad] add Constraint [Relationship229] foreign key([idmovimiento]) references [movimiento] ([idmovimiento])  on update no action on delete no action 
go
Alter table [comprobante] add Constraint [Relationship73] foreign key([idtipocomprobante]) references [tipocomprobante] ([idtipocomprobante])  on update no action on delete no action 
go
Alter table [pedido] add Constraint [Relationship159] foreign key([idtipocomprobante]) references [tipocomprobante] ([idtipocomprobante])  on update no action on delete no action 
go
Alter table [documentoreferenciamovimiento] add Constraint [Relationship217] foreign key([idtipocomprobante]) references [tipocomprobante] ([idtipocomprobante])  on update no action on delete no action 
go
Alter table [motivomovimiento] add Constraint [Relationship133] foreign key([idtipomovimiento]) references [tipomovimiento] ([idtipomovimiento])  on update no action on delete no action 
go
Alter table [movimiento] add Constraint [Relationship136] foreign key([idtipomovimiento]) references [tipomovimiento] ([idtipomovimiento])  on update no action on delete no action 
go
Alter table [motivomovimientogeneral] add Constraint [Relationship184] foreign key([idtipomovimiento]) references [tipomovimiento] ([idtipomovimiento])  on update no action on delete no action 
go
Alter table [equivalencia] add  foreign key([idunidadsrc]) references [unidad] ([idunidad])  on update no action on delete no action 
go
Alter table [equivalencia] add  foreign key([idunidaddst]) references [unidad] ([idunidad])  on update no action on delete no action 
go
Alter table [stockinventario] add Constraint [Relationship112] foreign key([idunidad]) references [unidad] ([idunidad])  on update no action on delete no action 
go
Alter table [item] add Constraint [Relationship127] foreign key([idunidad]) references [unidad] ([idunidad])  on update no action on delete no action 
go
Alter table [detallemovimiento] add Constraint [Relationship141] foreign key([idunidad]) references [unidad] ([idunidad])  on update no action on delete no action 
go
Alter table [item] add Constraint [Relationship96] foreign key([idequivalencia]) references [equivalencia] ([idequivalencia])  on update no action on delete no action 
go
Alter table [columna] add Constraint [Relationship233] foreign key([idnivel]) references [nivel] ([idnivel])  on update no action on delete no action 
go
Alter table [pasillo] add Constraint [Relationship232] foreign key([idcolumna]) references [columna] ([idcolumna])  on update no action on delete no action 
go
Alter table [movimientotransporte] add Constraint [Relationship110] foreign key([idvehiculo]) references [vehiculo] ([idvehiculo])  on update no action on delete no action 
go
Alter table [vehiculo] add Constraint [Relationship43] foreign key([idmarcavehiculo]) references [marcavehiculo] ([idmarcavehiculo])  on update no action on delete no action 
go
Alter table [categoria] add Constraint [Relationship52] foreign key([idfamilia]) references [familia] ([idfamilia])  on update no action on delete no action 
go
Alter table [item] add Constraint [Relationship53] foreign key([idmarca]) references [marca] ([idmarca])  on update no action on delete no action 
go
Alter table [comprobante] add Constraint [Relationship108] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [detallemovimiento] add Constraint [Relationship140] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [item] add Constraint [Relationship145] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [listaprecios] add Constraint [Relationship146] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [pedido] add Constraint [Relationship161] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [itemprecioestandar] add Constraint [Relationship197] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [comboitemprecio] add Constraint [Relationship206] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [documentoreferenciamovimiento] add Constraint [Relationship216] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [movimiento] add Constraint [Relationship218] foreign key([idtipomoneda]) references [tipomoneda] ([idtipomoneda])  on update no action on delete no action 
go
Alter table [movimiento] add Constraint [Relationship77] foreign key([idcomprobante]) references [comprobante] ([idcomprobante])  on update no action on delete no action 
go
Alter table [entidadcomprobante] add Constraint [Relationship85] foreign key([idcomprobante]) references [comprobante] ([idcomprobante])  on update no action on delete no action 
go
Alter table [detallestockinventario] add Constraint [Relationship171] foreign key([idstockinventario]) references [stockinventario] ([idstockinventario])  on update no action on delete no action 
go
Alter table [stocknivelinventario] add Constraint [Relationship222] foreign key([idstockinventario]) references [stockinventario] ([idstockinventario])  on update no action on delete no action 
go
Alter table [pasillo] add Constraint [Relationship118] foreign key([idalmacen]) references [almacen] ([idalmacen])  on update no action on delete no action 
go
Alter table [stockinventario] add Constraint [Relationship142] foreign key([idalmacen]) references [almacen] ([idalmacen])  on update no action on delete no action 
go
Alter table [seriesalmacen] add Constraint [Relationship195] foreign key([idalmacen]) references [almacen] ([idalmacen])  on update no action on delete no action 
go
Alter table [activofijo] add Constraint [Relationship123] foreign key([idcategoria]) references [categoriaactivo_fijo] ([idcategoria])  on update no action on delete no action 
go
Alter table [movimientoactivo] add Constraint [Relationship176] foreign key([idactivo]) references [activofijo] ([idactivo])  on update no action on delete no action 
go
Alter table [activofijo] add Constraint [Relationship124] foreign key([idcentrocosto]) references [centrocosto] ([idcentrocosto])  on update no action on delete no action 
go
Alter table [pedidocentrocosto] add Constraint [Relationship168] foreign key([idcentrocosto]) references [centrocosto] ([idcentrocosto])  on update no action on delete no action 
go
Alter table [movimientoactivo] add Constraint [Relationship177] foreign key([idareaorigen]) references [area] ([idarea])  on update no action on delete no action 
go
Alter table [movimientoactivo] add Constraint [Relationship180] foreign key([idareadestino]) references [area] ([idarea])  on update no action on delete no action 
go
Alter table [activofijo] add Constraint [Relationship220] foreign key([idarea]) references [area] ([idarea])  on update no action on delete no action 
go
Alter table [listaprecios_item] add Constraint [Relationship129] foreign key([idlistaprecios]) references [listaprecios] ([idlistaprecios])  on update no action on delete no action 
go
Alter table [listapreciosucursal] add Constraint [Relationship187] foreign key([idlistaprecios]) references [listaprecios] ([idlistaprecios])  on update no action on delete no action 
go
Alter table [movimiento] add Constraint [Relationship135] foreign key([idmotivo]) references [motivomovimiento] ([idmotivo])  on update no action on delete no action 
go
Alter table [motivo_general_entidad] add Constraint [Relationship186] foreign key([idmotivo]) references [motivomovimiento] ([idmotivo])  on update no action on delete no action 
go
Alter table [detallestockinventario] add Constraint [Relationship172] foreign key([iddetallemovimiento]) references [detallemovimiento] ([iddetallemovimiento])  on update no action on delete no action 
go
Alter table [detallemovstocknivel] add Constraint [Relationship228] foreign key([iddetallemovimiento]) references [detallemovimiento] ([iddetallemovimiento])  on update no action on delete no action 
go
Alter table [detallepedido] add Constraint [Relationship150] foreign key([idpedido]) references [pedido] ([idpedido])  on update no action on delete no action 
go
Alter table [pedidoarchivo] add Constraint [Relationship163] foreign key([idpedido]) references [pedido] ([idpedido])  on update no action on delete no action 
go
Alter table [pedidoreferencia] add Constraint [Relationship165] foreign key([idpedidoorigen]) references [pedido] ([idpedido])  on update no action on delete no action 
go
Alter table [pedidoreferencia] add Constraint [Relationship166] foreign key([idpedidodestino]) references [pedido] ([idpedido])  on update no action on delete no action 
go
Alter table [pedidocentrocosto] add Constraint [Relationship167] foreign key([idpedido]) references [pedido] ([idpedido])  on update no action on delete no action 
go
Alter table [pedido_detallepedido] add Constraint [Relationship173] foreign key([idpedido]) references [pedido] ([idpedido])  on update no action on delete no action 
go
Alter table [pedido_detallepedido] add Constraint [Relationship174] foreign key([iddetallepedido]) references [detallepedido] ([iddetallepedido])  on update no action on delete no action 
go
Alter table [detallepedidocantidad] add Constraint [Relationship175] foreign key([iddetallepedido]) references [detallepedido] ([iddetallepedido])  on update no action on delete no action 
go
Alter table [itemcuentacontable] add Constraint [Relationship152] foreign key([idcuentaparticular]) references [cuentaparticular] ([idcuentaparticular])  on update no action on delete no action 
go
Alter table [pedido] add Constraint [Relationship160] foreign key([idestado]) references [estadopedido] ([idestado])  on update no action on delete no action 
go
Alter table [comboitemprecio] add Constraint [Relationship205] foreign key([idcomboitem]) references [comboitems] ([idcomboitem])  on update no action on delete no action 
go
Alter table [motivo_general_entidad] add Constraint [Relationship185] foreign key([idmotivogeneral]) references [motivomovimientogeneral] ([idmotivogeneral])  on update no action on delete no action 
go
Alter table [dominioapp] add Constraint [Relationship191] foreign key([idparametro]) references [parametrosapp] ([idparametro])  on update no action on delete no action 
go
Alter table [itemparametroapp] add Constraint [Relationship192] foreign key([idparametro]) references [parametrosapp] ([idparametro])  on update no action on delete no action 
go
Alter table [entidadparametro] add Constraint [Relationship200] foreign key([idparametro]) references [parametrosapp] ([idparametro])  on update no action on delete no action 
go
Alter table [seriesalmacen] add Constraint [Relationship194] foreign key([idseriesucursal]) references [seriesucursal] ([idseriesucursal])  on update no action on delete no action 
go
Alter table [stocknivelinventario] add Constraint [Relationship207] foreign key([idnivelinventario]) references [nivelinventario] ([idnivelinventario])  on update no action on delete no action 
go
Alter table [detallemovstocknivel] add Constraint [Relationship227] foreign key([idstocknivelinventario]) references [stocknivelinventario] ([idstocknivelinventario])  on update no action on delete no action 
go
Alter table [codigoitem] add Constraint [Relationship213] foreign key([idtipo]) references [tipologistica] ([idtipologistica])  on update no action on delete no action 
go
Alter table [itemcomponenteactivo] add Constraint [Relationship224] foreign key([idcomponenteactivo]) references [componenteactivo] ([idcomponenteactivo])  on update no action on delete no action 
go
Alter table [itemcodigosunat] add Constraint [Relationship239] foreign key([idcodigosunat]) references [codigosunat] ([idcodigosunat])  on update no action on delete no action 
go


Set quoted_identifier on
go


Set quoted_identifier off
go


