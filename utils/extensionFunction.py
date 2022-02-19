import base64
import os

""" cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
 """
def toBase64():
    with open("utils/pdfGenerados/generado.pdf", "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())
    return encoded_string


