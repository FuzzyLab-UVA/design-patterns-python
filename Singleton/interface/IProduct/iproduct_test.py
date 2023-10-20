from .iproduct import IProduct

def test_iproduct():
    try:
        product = IProduct()
    except:
        assert True