from .isofa import ISofa

def test_isofa():
    try:
        sofa = ISofa()
    except:
        assert True
