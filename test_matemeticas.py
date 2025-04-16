from matematicas import es_primo, factorial
import pytest

def test_esprimo():
    assert es_primo(2) == True
    assert es_primo(2) is True
    assert es_primo(4) is False
    assert es_primo(13) is True
    assert es_primo(1) is False
    assert es_primo(0) is False
    
def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-3)
    assert factorial(1) == 1

