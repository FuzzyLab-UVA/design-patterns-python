from .itable import ITable

def test_itable():
    try:
        sofa = ITable()
    except:
        assert True