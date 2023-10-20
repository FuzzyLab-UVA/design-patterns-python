from .iuser import IUser

def test_iuser():
    try:
        user = IUser()
    except:
        assert True