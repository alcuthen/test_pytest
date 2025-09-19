import pytest


@pytest.mark.login
def test_ct01_valido():
    assert True  


@pytest.mark.exec
def test_ct02_invalido():
    assert not True 


#Toda classe deve conter somente um método de teste
@pytest.mark.login
class TestLogin:
    def test_ct03_valido(self):
        assert True  

# Para executar marcadores específicos, use:
# pytest -v test_login.py::TestLogin
# pytest test_login.py -v -m login
# pytest test_login.py -vm login

# Para refinar os marcadores, crie um arquivo pytest.ini com:
# [pytest]
# markers = nome_do_marcador: 
#   marks tests nome_do_marcador (deselect with '-m "not nome_do_marcador"')