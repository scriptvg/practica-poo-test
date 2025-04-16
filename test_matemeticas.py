from matematicas import es_primo

def test_esprimo():
    assert es_primo(2) == True
    assert es_primo(2) is True
    assert es_primo(4) is False
    assert es_primo(13) is True
    assert es_primo(1) is False
    assert es_primo(0) is False