from jinja2.environment import Template
import pdfkit
from jinja2 import Environment, FileSystemLoader
from entidades.models import PdfToBase64
from utils.constantes import BOLETA, FACTURA, NOTA_CREDITO, NOTA_VENTA
from utils.extensionFunction import toBase64


def generar_comprobante(comprobante):
    env = Environment(loader=FileSystemLoader("./templates"))
    print('_________________')

    print(comprobante.IdTipoDocumento)
    if comprobante.IdTipoDocumento == FACTURA:
        print('---------factura--------------')
        template = env.get_template("boleta_venta_electronica.html")

    elif comprobante.IdTipoDocumento == BOLETA:
        print('---------boleta--------------')
        template = env.get_template("prueba.html")

    elif comprobante.IdTipoDocumento == NOTA_CREDITO:
        template = env.get_template("prueba.html")

    elif comprobante.IdTipoDocumento == NOTA_VENTA:
        template = env.get_template("prueba.html")

    html = template.render(comprobante)

    pdfkit.from_string(html, 'utils/pdfGenerados/generado.pdf')

    file = open('utils/pdfGenerados/code.txt', 'wb')
    for line in open('utils/pdfGenerados/generado.pdf', 'rb').readlines():
        file.write(line)
    file.close()

    file = open('utils/pdfGenerados/pdfbinario.pdf', 'wb')
    for line in open('utils/pdfGenerados/code.txt', 'rb').readlines():
        file.write(line)
    file.close()

    pdftob64 = PdfToBase64(Nombre='00000000000/B003-00001296-633496-PDF.PDF',
                           NumeroDocumentoEmisor='000000000000',
                           Base64=toBase64())
    return pdftob64.json()
