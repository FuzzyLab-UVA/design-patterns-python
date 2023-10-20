from .owner_singleton import SingletonOwner
from interface import IOwner

def test_owner_singleton():

    single = SingletonOwner()

    single2 = SingletonOwner()

    assert isinstance(single, IOwner)
    assert isinstance(single2, IOwner)
    assert single == single2