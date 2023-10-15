from .mysql_factory import MySqlFactory


def test_factory():
    factory = MySqlFactory()
    assert factory.create() is not None