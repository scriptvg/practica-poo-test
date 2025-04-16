
# Módulo para trabajar con expresiones regulares y cadenas de texto
import re

def formatear_nombre(nombre):
    return " ".join([palabra.capitalize() for palabra in nombre.split()])


def es_correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))

def contar_palabras(texto):
    return len(texto.split())




