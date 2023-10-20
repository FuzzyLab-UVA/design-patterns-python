from .owner_singleton import SingletonOwner

def test_owner_singleton():

    single = SingletonOwner()

    single2 = SingletonOwner()

    assert single == single2