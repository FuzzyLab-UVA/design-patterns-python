from .iowner import IOwner

def test_owener():
    try:
        owner = IOwner()
    except:
        assert True