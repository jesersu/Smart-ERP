from datetime import datetime
from rest_framework import serializers
from typing import Optional, List
from pydantic import BaseModel
from datetime import date


class TipoDocumentoDto:
    def __init__(self):
        self.Id = 0
        self.Codigo = ''
        self.Tipo = ''
        self.Descripcion = ''
        self.Abreviacion = ''
        self.LogUserCrea = ''
        self.LogDateCrea = datetime.now()
        self.LogUserModif = ''
        self.LogDateModif = datetime.now()
        self.LogEstado = 0


class TipoDocumentoDtoSerializer(serializers.Serializer):
    Id = serializers.IntegerField()
    Codigo = serializers.CharField(max_length=10)
    Tipo = serializers.CharField(max_length=100)
    Descripcion = serializers.CharField(max_length=50)
    Abreviacion = serializers.CharField(max_length=10)
    LogUserCrea = serializers.CharField(max_length=50)
    LogDateCrea = serializers.DateTimeField()
    LogUserModif = serializers.CharField(max_length=50)
    LogDateModif = serializers.DateTimeField()
    LogEstado = serializers.IntegerField()


class Parametros(BaseModel):
    IdDetalleDocumento:  int = 0
    IdDominio:  int = 0
    IdParametro:  int = 0
    Tipo: str = ""
    Valor: str = ""
    Auxiliar1: str = ""
    Auxiliar2: str = ""
    Auxiliar3: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Items(BaseModel):

    IdDocumentoContable:  int = 0
    Item:  int = 0
    ItemDescripcion: str = ""
    IdTipoAfectacionIGV: int = 0
    IdTipoPrecioVentaUnitario: int = 0

    CodigoItem: str = ""
    CodigoSunat: str = ""
    CodigoBarras: str = ""
    PrecioUnitario:  int = 0
    PrecioUnitarioVenta:  int = 0
    ValorUnitario: float = 0
    Cantidad:  int = 0
    IdReferencia:  int = 0
    IdAlmacen:  int = 0
    IdInventario:  int = 0
    IdUnidad:  int = 0
    Descuento:  int = 0
    SubTotal:  float = 0
    PrecioVentaItem:  int = 0
    Total:  int = 0
    IGV:  float = 0
    ValorIGV:  int = 0
    ValorVenta:  float = 0
    MontoISC:  int = 0
    CodigoUnidad: str = ""
    DescripcionUnidad: str = ""
    IdOrigen: str = ""
    IdDetalleOrigen: str = ""
    OtrosCargosItem:  int = 0
    OtrosTributos:  int = 0
    IdMSOrigen:  int = 0
    PesoBruto:  float = 0
    PesoNeto:  float = 0
    CodigoLote: str = ""
    IdLote:  int = 0
    IdMoneda:  int = 0
    FechaVencimiento: Optional[datetime] = None
    ICBPER:  int = 0
    IGVAFECTADO: float = 0
    Stock: float = 0
    PrecioBase: float = 0
    NombreMarca: str = ''
    ListaParametros: Optional[List[Parametros]] = []
    DescuentoPrecio:  int = 0
    DescuentoPorcentaje:  int = 0
    DescuentoPrecio:  float = 0
    Id:  int = 0
    TipoItem:  int = 0
    EsDeLista: bool = False
    UrlImagen: str = ""
    ControlarStock:  int = 0
    MostrarDetallado: str = ""
    EsFavorito:  int = 0
    ControlLotes:  int = 0
    TieneImpuestoBolsa:  int = 0

    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Parametro(BaseModel):
    IdComprobante:  int = 0
    IdParametro:  int = 0
    IdDominio:  int = 0
    Tipo: str = ""
    Valor: str = ""
    Auxiliar1: str = ""
    Auxiliar2: str = ""
    Auxiliar3: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Concepto(BaseModel):
    IdDocumentoContable:  int = 0
    IdConcepto:  int = 0
    Monto:  int = 0
    AuxiliarDecimal1:  int = 0
    AuxiliarDecimal2:  int = 0
    AuxiliarVarchar1: str = ""
    AuxiliarVarchar2: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class DescuentoPrecio(BaseModel):
    IdDocumentoContable:  int = 0
    IdConcepto:  int = 0
    Monto:  int = 0
    AuxiliarDecimal1:  int = 0
    AuxiliarDecimal2:  int = 0
    AuxiliarVarchar1: str = ""
    AuxiliarVarchar2: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Entidades(BaseModel):
    IdComprobante:  int = 0
    IdEntidad:  int = 0
    TipoEntidad:  int = 0
    RazonSocial: str = ""
    NumeroDocumento: str = ""
    Direccion: str = None
    TipoDocumentoDescripcion: str = ""
    CorreoEntidadReceptor: Optional[str] = None
    Telefono: str = ""
    IdTipoDocumento:  int = 0
    IdCliente:  int = 0
    Id:  int = 0
    CorreoEntidad: Optional[str] = None
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Referencias(BaseModel):
    IdComprobanteOrigen:  int = 0
    IdComprobnteDestino:  int = 0
    IdTipoComprobanteOrigen:  int = 0
    CodigoTipoComprobanteOrigen: str = ""
    DescTipoComprobanteOrigen: str = ""
    IdSerieOrigen:  int = 0
    SerieOrigen: str = ""
    Correlativo_Origen:  int = 0
    IdTipoDocumentoDestino:  int = 0
    CodigoTipoComprobanteDestino: str = ""
    DescTipoComprobanteDestino: str = ""
    IdSerieDestino:  int = 0
    SerieDestino: str = ""
    Correlativo_Destino:  int = 0
    FechaEmisionDestino: Optional[datetime] = None
    es_anticicpo: bool
    MonedaDestino: str = ""
    Monto_Anticipo:  int = 0
    Auxiliar1: str = ""
    Auxiliar2: str = ""
    Auxiliar3: str = ""
    MontoTotal:  int = 0
    IdEstadoDestino:  int = 0
    EstadoDestino: str = ""
    EstadoSunat:  int = 0
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Archivos(BaseModel):
    IdDocumentoContable:  int = 0
    Archivo: str = ""
    TipoArchivo: str = ""
    ArchivoBase64: str = ""
    Auxiliar1: str = ""
    Auxiliar2: str = ""
    Auxiliar3: str = ""
    RucEmisor: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Adicional(BaseModel):
    IdDocumentoContable:  int = 0
    TipoAdicional:  int = 0
    Descripcion: str = ""
    Auxiliar1: str = ""
    Auxiliar2: str = ""
    Auxiliar3: str = ""
    Auxiliar4: str = ""
    Auxiliar5: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Conductores(BaseModel):
    IdComprobante:  int = 0
    IdEntidad:  int = 0
    TipoEntidad:  int = 0
    RazonSocial: str = ""
    NumeroDocumento: str = ""
    Direccion: str = None
    TipoDocumentoDescripcion: str = ""
    CorreoEntidadReceptor: str = ""
    Telefono: str = ""
    IdTipoDocumento:  int = 0
    IdCliente:  int = 0
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Recibidos(BaseModel):
    IdreciboPago:  int = 0
    IdDocumentoContable:  int = 0
    NumeroCuota:  int = 0
    Monto:  int = 0
    FechaEmision: Optional[datetime] = None
    FechaVencimiento: Optional[datetime] = None
    Estado:  int = 0
    IdReciboFinanciero:  int = 0
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Receptor(BaseModel):
    RazonSocial: str = ""
    TipoDocumento: str = ""
    NumeroDocumento: str = ""


class Emisor(BaseModel):
    RazonSocial: str = ""
    TipoDocumento: str = ""
    NumeroDocumento: str = ""


class GenerarDocumento(BaseModel):
    IdTipoDocumento:  int = 0
    IdTipoDocumento:  int = 0
    CentroCostos: str = ""
    IdCentroCostos:  int = 0
    IdEstadoComprobante:  int = 0
    IdMoneda:  int = 0
    IdCondicionPago:  int = 0
    IdSerie:  int = 0
    IdEmpresa:  int = 0
    TipoOperacion:  int = 0
    CorrelativoDocumento:  int = 0
    IdOrigen: str = ""
    CodigoPedido: str = ""
    SeriePedido: str = ""
    IdModulo:  int = 0
    IdEntidadEmisor:  int = 0
    IdEntidadReceptora:  int = 0
    MontoSubTotal: float = 0
    MontoIGV:  float = 0
    MontoIGVGratuito:  int = 0
    MontoISC:  int = 0
    MontoTotal:  int = 0
    SumatoriaIcbper:  int = 0
    OtrosCargos:  int = 0
    OtrosCargosSumatoria:  int = 0
    NotaCreditoSinReferencia: str = ""
    DescuentosGlobales:  int = 0
    DescuentosTotales:  int = 0
    TotalPrecioVenta:  int = 0
    Direccion: str = None
    ValorIGV: int = 0
    Observaciones: str = ""
    FechaEmision: Optional[date] = None
    FechaAnulacion: Optional[date] = None
    FechaVencimiento: Optional[date] = None
    PesoBruto:  int = 0
    PesoNeto:  int = 0
    SerieCompras: str = ""
    SumaDescuentosNoAfectanBase:  int = 0
    ListaItems: List[Items] = []
    ListaParametro: List[Parametro] = []
    ListaConcepto: List[Concepto]
    ListaEntidades: List[Entidades]
    ListaReferencia: Optional[List[Referencias]] = []
    ListaArchivos: List[Archivos]
    ListaAdicional: List[Adicional]
    ListaConductores: Optional[List[Conductores]] = []
    ListaRecibos: List[Recibidos]
    MinItem: Optional[List[int]] = []
    CodigoOrdenCompra: str = ""
    NumeroContrato: str = None
    MontoDescuento:  int = 0
    SerieDescripcion: str = ""
    MonedaDescripcion: str = ""
    OtrosTributos:  int = 0
    MonedaAbreviacion: str = ""
    MonedaCodigo: str = ""
    TipoDocCodigo: str = ""
    TipoDocDescripcion: str = ""
    EmisorRazonSocial: str = ""
    EmisorTipoDocumento: str = ""
    EmisorNumeroDocumento: str = ""
    EmisorCorreo: str = ""
    DireccionEmisor: str = ""
    Receptor: Optional[Receptor] = None
    Emisor: Optional[Emisor] = None
    ReceptorRazonSocial: str = ""
    ReceptorTipoDocumento: str = ""
    ReceptorNumeroDocumento: str = ""
    ReceptorCorreo: str = ""
    DireccionReceptor: str = None
    CondicionPago: str = ""
    EstadoDescripcion: str = ""
    RutaLogo: str = ""
    NumeroDocumentoFormateado: str = ""
    OperacionesGravadas:  float = 0
    OperacionesInafectas:  float = 0
    OperacionesExoneradas: float = 0
    OperacionesGratuitas:  float = 0
    OperacionesExportadas: float = 0
    MontoEnLetras: str = ""
    MontoAnticipo:  int = 0
    ValorVenta:  int = 0
    MotivoSustento: str = ""
    TipoDeNota: str = ""
    TicketComunicacionBaja: str = ""
    IdTipoNota:  int = 0
    DescripcionTipoDocumentoDestino: str = ""
    CorrelativoDocumentoDestino: str = ""
    FechaEmisionFormateada: str = ""
    FechaVencimientoFormateada: str = ""
    SerieDocumentoDestino: str = ""
    EstadoSunatDescripcion: str = ""
    IdestadoSunat:  int = 0
    DocumentoRegularizado: str = ""
    NumeroDocumentoFinanciero: str = ""
    TieneDocumentoFinanciero:  int = 0
    ValorResumen: str = ""
    TicketResumenBoletas: str = ""
    QRBase64: str = ""
    PedidoAtentido:  int = 0
    AtentidoCon: str = ""
    ListaPrecios: str = ""
    NombreArchivoMasivo: str = ""
    NombreArchivoMasivoAzure: str = ""
    SucursalCodigoDomiciliario: str = ""
    NombreSucursal: str = ""
    IdSucursal:  int = 0
    RutaQr: str = ""
    EsAdelanto: str = ""
    TotalAdelantos:  int = 0
    ClienteAsociado: str = ""
    ValidezOferta: str = ""
    NumeroOrdenCompra: str = ""
    TelefonoEmisor: str = ""
    TelefonoReceptor: str = ""
    TelefonoColaborador: str = ""
    CorreoColaborador: str = ""
    TransportistaRazonSocial: str = ""
    TransportistaNumeroDocumento: str = ""
    TercerosRazonSocial: str = ""
    TercerosNumeroDocumento: str = ""
    PuntoPartida: str = ""
    PuntoLlegada: str = ""
    FechaTraslado: str = ""
    MotivoTraslado: str = ""
    ModalidadTraslado: str = ""
    Idcliente:  int = 0
    ReceptorIdTipoDoc:  int = 0
    NumedoDocumentoColaborador: str = ""
    RazonSocialColaborador: str = ""
    TipoDocumentoColaborador: str = ""
    FechaEmisionAfectado: Optional[datetime] = None
    DescripcionEspecial1: str = ""
    DescripcionEspecial2: str = ""
    DescripcionEspecial3: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


"""Usuario"""


class ParamatrosEntidad(BaseModel):
    IdEntidad:  int = 0
    IdParametro:  int = 0
    Valor: str = ""
    Dato1: str = ""
    Dato2: str = ""
    Dato3: str = ""
    Documento: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class ParametrosFacturacion (BaseModel):
    IdEntidad:  int = 0
    IdParametro:  int = 0
    IdDominio:  int = 0
    Tipo: str = ""
    Valor: str = ""
    Auxiliar1: str = ""
    Auxiliar2: str = ""
    Auxiliar3: str = ""
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class Entidad(BaseModel):
    IdTipoDocumento:  int = 0
    IdUbigeo: str = ""
    Documento: str = ""
    RazonSocial: str = ""
    Nombre: str = ""
    ApePat: str = ""
    ApeMat: str = ""
    Correo: str = ""
    Telefono: str = ""
    Direccion: str = None
    TipoActualizacion:  int = 0
    ModoIngreso: str = ""
    TipoDocumentoDesc: str = ""
    ParamatrosEntidad: List[ParamatrosEntidad]
    ImagenURL: str = ""
    ParametrosFacturacion: List[ParametrosFacturacion]
    Id:  int = 0
    LogUsuariocrea: str = ""
    LogFechacrea: Optional[datetime] = None
    LogUsuariomodif: str = ""
    LogFechamodif: Optional[datetime] = None
    LogEstado:  int = 0


class PdfToBase64(BaseModel):
    Nombre: str = ""
    Base64: str = ""
    NumeroDocumentoEmisor: str = ""


class PlantillaResponse(BaseModel):
    Nombre: str = ""
    Base64: str = ""
