from utilidades import formatear_nombre, es_correo_valido, contar_palabras

def test_formatear_nombre():
    assert formatear_nombre("juan perez") == "Juan Perez"
    assert formatear_nombre("maria lopez") == "Maria Lopez"
    assert formatear_nombre("   pedro    sanchez   ") == "Pedro Sanchez"
    
def test_es_correo_valido():
    assert es_correo_valido("velezalan34@gmail.com") is True
    assert es_correo_valido("velezalan34@gmail") is False
    
def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("Esta es una prueba") == 5
    assert contar_palabras("") == 0